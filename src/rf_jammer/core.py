"""RF Jamming Detection Engine"""
import os, json, time, struct, math
from datetime import datetime

class SpectrumAnalyzer:
    def __init__(self, sample_rate=2e6, center_freq=2.437e9):
        self.sample_rate = sample_rate
        self.center_freq = center_freq
        self.baseline = None
    
    def compute_fft(self, samples, fft_size=1024):
        """Compute power spectrum (simplified)"""
        # In production, use numpy.fft
        power = []
        for i in range(min(fft_size, len(samples))):
            power.append(abs(samples[i]) ** 2 if isinstance(samples[i], complex) else samples[i] ** 2)
        return power
    
    def set_baseline(self, samples):
        self.baseline = self.compute_fft(samples)
        return self.baseline
    
    def detect_jamming(self, samples, threshold_db=20):
        current = self.compute_fft(samples)
        if not self.baseline:
            return {"jamming": False, "reason": "No baseline set"}
        
        avg_baseline = sum(self.baseline) / max(1, len(self.baseline))
        avg_current = sum(current) / max(1, len(current))
        
        if avg_baseline > 0:
            ratio = avg_current / avg_baseline
            db_change = 10 * math.log10(max(1e-10, ratio))
        else:
            db_change = 0
        
        return {"jamming": db_change > threshold_db, "power_change_db": round(db_change, 2),
                "threshold_db": threshold_db, "timestamp": datetime.now().isoformat()}

class JamDetector:
    def __init__(self):
        self.alerts = []
    
    def monitor_wifi(self, interface="wlan0"):
        """Monitor WiFi for jamming indicators"""
        import subprocess
        findings = []
        try:
            result = subprocess.check_output(["iwconfig", interface], text=True)
            for line in result.split("\n"):
                if "Signal level" in line:
                    parts = line.split("Signal level=")
                    if len(parts) > 1:
                        signal = int(parts[1].split(" ")[0].replace("dBm",""))
                        if signal < -80:
                            findings.append({"type": "weak_signal", "signal": signal, "severity": "MEDIUM"})
                if "Noise level" in line:
                    parts = line.split("Noise level=")
                    if len(parts) > 1:
                        noise = int(parts[1].split(" ")[0].replace("dBm",""))
                        if noise > -50:
                            findings.append({"type": "high_noise", "noise": noise, "severity": "HIGH"})
        except: pass
        return findings
    
    def detect_deauth_flood(self, interface="wlan0", duration=10):
        """Check for deauth flood (jamming companion attack)"""
        return {"method": "monitor_mode", "interface": interface, "status": "requires_monitor_mode"}
