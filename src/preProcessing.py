# Import the necessary modules
import numpy as np
from scipy.signal import butter, lfilter
from parameters import *
import pandas as pd
# Set the low and high cutoff frequencies for the bandpass filter
lowcut = 5
highcut = 40

# Sampling frequency of the data (in Hz)
fs = 250

# Compute the order of the Butterworth filter
order = 6

# Compute the Butterworth filter coefficients
nyq = 0.5 * fs
low = lowcut / nyq
high = highcut / nyq
b, a = butter(order, [low, high], btype='band')

eeg_data = pd.read_csv(EEG_file_name)
eeg_data_to_filter = eeg_data.drop(['index', 'timeStamp'], axis=1)
timeStamp = eeg_data['timeStamp']
indexes = eeg_data['index']

# Apply the Butterworth filter to the EEG data
eeg_filtered = lfilter(b, a, eeg_data_to_filter)

eeg_filtered_hole = pd.DataFrame(eeg_filtered)
eeg_filtered_hole = pd.concat([indexes, timeStamp, eeg_filtered_hole],axis=1)


file = pd.DataFrame(eeg_filtered_hole)
file.to_csv(Filtered_EEG_file_name, index=False)
