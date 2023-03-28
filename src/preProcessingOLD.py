# Import the necessary modules
import numpy as np
from scipy.signal import butter, lfilter, filtfilt
from parameters import *
import pandas as pd
import numpy as np
import mne as mne
from scipy.signal import firwin2
from mne.preprocessing import (ICA, corrmap, create_ecg_epochs,
                               create_eog_epochs)

def filter_data(raw):
    sfreq = samplingRate  # sampling frequency
    power_noise = (25, 50)
    # Apply filter to data
    # band pass 1-28 Hz
    filtered_data = mne.filter.filter_data(raw.get_data(), sfreq=sfreq, l_freq=1, h_freq=28, method='fir',
                                           fir_design='firwin', phase='zero-double', fir_window='blackman')
    # notch 25, 50 Hz
    filtered_data = mne.filter.notch_filter(filtered_data, sfreq, power_noise, method='fir', fir_design='firwin',
                                            phase='zero-double', fir_window='blackman')
    return filtered_data


def create_mne_raw(EEG_data, bad_channels):

    # unit conversion for uV to V
    EEG_data = EEG_data.div(1000000)

    # Define the sampling frequency
    sfreq = samplingRate

    # Define the channel names
    ch_names = ['C3', 'C4', 'Cz', 'FC1', 'FC2', 'FC5', 'FC6', 'CP1', 'CP2', 'CP5', 'CP6', 'O1', 'O2']

    # Define a dictionary mapping channel names to classical positions
    channel_positions = {
        'ch1': 'C3',
        'ch2': 'C4',
        'ch3': 'Cz',
        'ch4': 'FC1',
        'ch5': 'FC2',
        'ch6': 'FC5',
        'ch7': 'FC6',
        'ch8': 'CP1',
        'ch9': 'CP2',
        'ch10': 'CP5',
        'ch11': 'CP6',
        'ch12': 'O1',
        'ch13': 'O2'
    }

    # Define the channel types
    ch_types = ['eeg'] * 13

    # Create an MNE Info object
    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)

    # Set the electrode positions using a standard 10-20 system
    montage = mne.channels.make_standard_montage('standard_1020')
    info.set_montage(montage)

    # Rename the channels in the data DataFrame using the dictionary
    EEG_data.rename(columns=channel_positions, inplace=True)
    # Create an MNE Raw object
    raw = mne.io.RawArray(EEG_data.values.T, info)

    # mark bad channels - parameter files
    raw.info['bads'] = bad_channels
    # picks are what is not bad
    pick = mne.pick_types(raw.info, eeg=True, exclude=raw.info['bads'])

    return raw, pick, info


def create_epoch(filtered_data_eeg, tmin, tmax, min_for_basline, max_for_baseline, annotations):
    # create events and event id from epoch
    event_id_erp = {"baseLine": 1, "distractor": 2, "target": 3}
    events, event_id = mne.events_from_annotations(filtered_data_eeg, event_id=event_id_erp)
    # events, event_id = mne.events_from_annotations(annotations)
    baseline = (min_for_basline, max_for_baseline)
    # The time interval to consider as “baseline” when applying baseline correction. If None, do not apply baseline correction.
    # If a tuple (a, b), the interval is between a and b (in seconds), including the endpoints. If a is None, the beginning of the data is used;
    # and if b is None, it is set to the end of the interval. If (None, None), the entire time interval is used.

    # windowing
    epochs = mne.Epochs(filtered_data_eeg, events, event_id=event_id_erp, tmin=tmin, tmax=tmax, baseline=baseline, preload=True)
    # epochs = mne.Epochs(filtered_data_eeg, tmin=tmin, tmax=tmax, baseline=baseline, preload=True)
    return epochs


def set_annotations_from_event_table(event_table, raw):
    # Calculate the offset
    offset = event_table['timeStamp'][0]

    # Subtract the offset from all of the timestamps
    event_table['timeStamp'] = event_table['timeStamp'] - offset

    # convert the timestamp column to a list of event times
    event_times = event_table['timeStamp'].tolist()

    # create a list of event descriptions
    event_descriptions = event_table['description'].tolist()
    # create an mne.Annotations object - check duration
    annotations = mne.Annotations(onset=event_times, duration=[StimOnset] * len(event_times), description=event_descriptions)
    # set the annotations for the Raw object
    raw.set_annotations(annotations)

    return annotations

def main(exp_path):
    # creating relevant paths for pre-processing
    EEG_Path = exp_path + EEG_folder_path + EEG_file_name
    labels_Path = exp_path + markers_arranged_folder_path + markers_arranged_file_name

    # reading relevant files for pre-processing
    EEG_data = pd.read_csv(EEG_Path)
    event_table = pd.read_csv(labels_Path)

    # saving variables for format later on
    timeStamp = EEG_data['timeStamp']
    channel_14 = EEG_data['channel_14']
    channel_15 = EEG_data['channel_15']
    channel_16 = EEG_data['channel_16']
    index = EEG_data['index']
    og_ch_names = {
        'C3': 'channel_1',
        'C4': 'channel_2',
        'Cz': 'channel_3',
        'FC1': 'channel_4',
        'FC2': 'channel_5',
        'FC5': 'channel_6',
        'FC6': 'channel_7',
        'CP1': 'channel_8',
        'CP2': 'channel_9',
        'CP5': 'channel_10',
        'CP6': 'channel_11',
        'O1': 'channel_12',
        'O2': 'channel_13'
    }
    EEG_data = EEG_data.drop(columns=['timeStamp', 'index', 'channel_14', 'channel_15', 'channel_16'])

    raw, picks, info = create_mne_raw(EEG_data, bad_channels)
    filtered_data = filter_data(raw)

    # Create an MNE filtered object
    filtered_data_eeg = mne.io.RawArray(filtered_data, info)
    # re-mark bad channels
    filtered_data_eeg.info['bads'] = bad_channels

    annotations = set_annotations_from_event_table(event_table, filtered_data_eeg)
    filtered_data_eeg.set_annotations(annotations)
    epochs = create_epoch(filtered_data_eeg, durationBeforeStimuli, durationAfterStimuli, baseline_min, baseline_max, annotations)
    epochs.drop_bad(reject=reject_criteria)


    # save the filtered file in the original form
    filtered_eeg_df = filtered_data_eeg.to_data_frame()
    filtered_eeg_df.rename(columns=og_ch_names, inplace=True)
    filtered_eeg_df = filtered_eeg_df.drop(columns=['time'])

    filtered_eeg_df.insert(0, column='timeStamp', value=timeStamp)
    filtered_eeg_df.insert(0, column='index', value=index)

    filtered_eeg_df['channel_14'] = channel_14
    filtered_eeg_df['channel_15'] = channel_15
    filtered_eeg_df['channel_16'] = channel_16

    # dividing the epoch per markers - mne objects
    epoch_target = epochs['target']
    epoch_distractor = epochs['distractor']
    epoch_baseLine = epochs['baseLine']

    # dividing the epoch per markers - dataframes
    epoch_erp = epochs.to_data_frame()
    epoch_target_df = epoch_erp[epoch_erp['condition'] == 'target']
    epoch_distractor_df = epoch_erp[epoch_erp['condition'] == 'distractor']
    epoch_baseLine_df = epoch_erp[epoch_erp['condition'] == 'baseLine']

    ###########################################################
    # save to "EXP_{date}" directory
    filtered_EEG_dir = exp_path + "filtered_EEG_Recordings/"
    os.makedirs(filtered_EEG_dir, exist_ok=True)
    #########################################################
    filtered_eeg_df.to_csv(filtered_EEG_dir + Filtered_EEG_file_name, index=False)
    epoch_target.save(filtered_EEG_dir + "target_epochs.fif", overwrite=True)
    epoch_distractor.save(filtered_EEG_dir + "distractor_epochs.fif", overwrite=True)
    return epoch_target, epoch_distractor, epoch_baseLine, epoch_target_df, epoch_distractor_df, epoch_baseLine_df

if __name__ == '__main__':
    main()