from rf_jammer.core import SpectrumAnalyzer
sa = SpectrumAnalyzer(center_freq=2.437e9)
baseline = [0.1] * 1024
sa.set_baseline(baseline)
jammed = [10.0] * 1024
result = sa.detect_jamming(jammed)
print(f"Jamming detected: {result['jamming']}")
print(f"Power change: {result['power_change_db']} dB")
