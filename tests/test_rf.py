import unittest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from rf_jammer.core import SpectrumAnalyzer

class TestSpectrum(unittest.TestCase):
    def test_fft(self):
        sa = SpectrumAnalyzer()
        power = sa.compute_fft([1.0, 2.0, 3.0, 4.0])
        self.assertEqual(len(power), 4)
    def test_no_baseline(self):
        sa = SpectrumAnalyzer()
        r = sa.detect_jamming([1.0]*100)
        self.assertFalse(r["jamming"])

if __name__ == "__main__": unittest.main()
