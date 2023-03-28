# Import the necessary modules
# import numpy as np
from scipy.signal import butter, lfilter, filtfilt
from parameters import *
# import pandas as pd


def main(exp_path):
    # Set the low and high cutoff frequencies for the bandpass filter
    lowcut = 1
    highcut = 30

    # Sampling frequency of the data (in Hz)
    fs = 125

    # Compute the order of the Butterworth filter
    order = 4

    # Compute the Butterworth filter coefficients
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')

    filename = exp_path + EEG_folder_path + EEG_file_name
    eeg_data = pd.read_csv(filename)
    eeg_data_to_filter = eeg_data.drop(['index', 'timeStamp'], axis=1)
    timeStamp = eeg_data['timeStamp']
    indexes = eeg_data['index']

    # Apply the Butterworth filter to the EEG data
    eeg_data_to_filter['channel_1'] = filtfilt(b, a, eeg_data_to_filter['channel_1'].values)
    eeg_data_to_filter['channel_2'] = filtfilt(b, a, eeg_data_to_filter['channel_2'].values)
    eeg_data_to_filter['channel_3'] = filtfilt(b, a, eeg_data_to_filter['channel_3'].values)
    eeg_data_to_filter['channel_4'] = filtfilt(b, a, eeg_data_to_filter['channel_4'].values)
    eeg_data_to_filter['channel_5'] = filtfilt(b, a, eeg_data_to_filter['channel_5'].values)
    eeg_data_to_filter['channel_6'] = filtfilt(b, a, eeg_data_to_filter['channel_6'].values)
    eeg_data_to_filter['channel_7'] = filtfilt(b, a, eeg_data_to_filter['channel_7'].values)
    eeg_data_to_filter['channel_8'] = filtfilt(b, a, eeg_data_to_filter['channel_8'].values)
    eeg_data_to_filter['channel_9'] = filtfilt(b, a, eeg_data_to_filter['channel_9'].values)
    eeg_data_to_filter['channel_10'] = filtfilt(b, a, eeg_data_to_filter['channel_10'].values)
    eeg_data_to_filter['channel_11'] = filtfilt(b, a, eeg_data_to_filter['channel_11'].values)
    eeg_data_to_filter['channel_12'] = filtfilt(b, a, eeg_data_to_filter['channel_12'].values)
    eeg_data_to_filter['channel_13'] = filtfilt(b, a, eeg_data_to_filter['channel_13'].values)
    eeg_data_to_filter['channel_14'] = filtfilt(b, a, eeg_data_to_filter['channel_14'].values)
    eeg_data_to_filter['channel_15'] = filtfilt(b, a, eeg_data_to_filter['channel_15'].values)

    eeg_filtered_hole = pd.concat([indexes, timeStamp, eeg_data_to_filter], axis=1)



    ###########################################################
    # save to "EXP_{date}" directory
    filtered_EEG_dir = exp_path + "filtered_EEG_Recordings"
    os.makedirs(filtered_EEG_dir, exist_ok=True)
    #########################################################
    file = pd.DataFrame(eeg_filtered_hole)
    file.to_csv(filtered_EEG_dir + "/" + Filtered_EEG_file_name, index=False)



if __name__ == '__main__':
    main()
