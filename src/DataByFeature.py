# Importing the required packages
import pandas as pd
from FeatureExtraction import Amplitude, Slope, Latency, PeakWidth


fueatures = {'Amplitude': Amplitude, 'Slope':  Slope, 'Latency':  Latency, 'Peak width':  PeakWidth}
X = pd.DataFrame(data=fueatures)
print(X)

