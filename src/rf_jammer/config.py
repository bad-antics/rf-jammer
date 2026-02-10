"""RF Jammer Config"""
FREQUENCY_BANDS = {"wifi_24": (2400e6, 2500e6), "wifi_5": (5150e6, 5850e6), "bluetooth": (2402e6, 2480e6), "gps_l1": (1575.42e6, 1575.42e6), "cellular_lte": (700e6, 2600e6), "ism_433": (433e6, 434e6), "ism_868": (868e6, 870e6), "ism_915": (902e6, 928e6)}
SAMPLE_RATE = 2e6
GAIN = 40
SDR_DEVICE = "rtlsdr"
SAFE_MODE = True  # Detection only, no transmission
