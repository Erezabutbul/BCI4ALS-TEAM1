import scipy
import matplotlib.pyplot as plt
from src.parameters import *
import pandas as pd
import mne
import numpy as np

def main():
    path = "C:\\Users\\Erez\\Desktop\\BCI4ALS-TEAM1\\src\\output_files\\EXP_30_04_2023 at 02_51_37_PM\\EEG_Recordings\\EEG_Recording_unprocessed.csv"
    data = np.loadtxt(path,delimiter=',', skiprows=1)
    EEG_data = pd.read_csv(path)
    EEG_data = EEG_data.drop(columns=['timeStamp', 'index', 'channel_14', 'channel_15', 'channel_16'])
    ch_names = ['C3', 'C4', 'Cz', 'FC1', 'FC2', 'FC5', 'FC6', 'CP1', 'CP2', 'CP5', 'CP6', 'O1', 'O2']
    info = mne.create_info(ch_names=ch_names, ch_types=["eeg"]*13, sfreq=samplingRate)
    raw = mne.io.RawArray(EEG_data.values.T,info)
    raw.filter(l_freq=3,h_freq=33)
    raw.notch_filter(freqs=25)
    # raw.plot()
    # mne.viz.utils.plt_show()
    f, psd_array = scipy.signal.welch(raw.get_data(), fs=samplingRate)
    for i in range(len(ch_names)):
        plt.plot(f,psd_array[i])
    plt.show()

if __name__ == '__main__':
    main()