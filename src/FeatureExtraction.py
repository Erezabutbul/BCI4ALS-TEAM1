# Importing the required packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from parameters import *


def saveFeatures(exp_path, Amplitude, Slope, Latency, PeakWidth, y):
    features = {'Amplitude': Amplitude, 'Slope': Slope, 'Latency': Latency, 'Peak width': PeakWidth}
    featureMatrix = pd.DataFrame(data=features)
    # save to "EXP_{date}" directory
    featuresDir = exp_path + feature_folder_path
    os.makedirs(featuresDir, exist_ok=True)
    featureMatrix.to_csv(featuresDir + feature_file_name)
    # Save the array to a CSV file
    np.savetxt(featuresDir + "labels.csv", y, delimiter=",")

# def main(exp_path):
def main():
    # Loading data by classes
    # df_baseline = pd.read_csv(exp_path + allClasses + mean_EEG_baseLine_folder_path + "baseLine_AVG_all_the_EXP.csv")
    # df_target = pd.read_csv(exp_path + allClasses + mean_EEG_target_folder_path + "target_AVG_all_the_EXP.csv")
    # df_distractor = pd.read_csv(exp_path + allClasses + mean_EEG_distractor_folder_path + "distractor_AVG_all_the_EXP.csv")
    # TODO - remove exp_path
    exp_path = "output_files/EXP_02_01_2023 at 12_12_58_PM/"
    df_baseline = pd.read_csv(exp_path + allClasses + "baseLine/" + mean_EEG_baseLine_folder_path + "baseLine_AVG_all_the_EXP.csv")
    df_target = pd.read_csv(exp_path + allClasses + "target/" + mean_EEG_target_folder_path + "target_AVG_all_the_EXP.csv")
    df_distractor = pd.read_csv(exp_path + allClasses + "distractor/" + mean_EEG_distractor_folder_path + "distractor_AVG_all_the_EXP.csv")


    time = pd.DataFrame(np.linspace(0, numOfSamplesToCut/samplingRate, numOfSamplesToCut))  # 75 samples, fs=125Hz
    # for elec_num in np.arange(1, 14):
    #     plt.subplot(4, 4, elec_num)
    #     plt.plot(time, df_target.iloc[elec_num + 1, 1:]-np.mean(df_target.iloc[elec_num + 1, 1:]))
    #     plt.plot(time, df_distractor.iloc[elec_num + 1, 1:]-np.mean(df_distractor.iloc[elec_num + 1, 1:]))
    #     plt.plot(time, df_baseline.iloc[elec_num + 1, 1:]-np.mean(df_baseline.iloc[elec_num + 1, 1:]))
    #     plt.title(df_target.iloc[elec_num + 1, 0])
    #     plt.xticks(np.arange(0, 0.7, 0.2))
    # plt.show()

    # target features
    # for elec_num in np.arange(1, 14):
    #     plt.subplot(4, 4, elec_num)
    #     x = df_target.iloc[elec_num + 1, 1:]-np.mean(df_target.iloc[elec_num + 1, 1:])
    #     peaks, properties = find_peaks(x, height=2, width=2)
    #     # print(peaks/125)
    #     plt.plot(time, x)
    #     plt.plot(peaks/125, x[peaks], "x")
    #     plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"]/125,
    #                xmax=properties["right_ips"]/125, color="C1")
    #     # plt.plot(time, np.zeros_like(x), "--", color="gray")
    #     plt.axvline(x=0.2, color='r', label='axvline - full height')
    #     plt.axvline(x=0.5, color='b', label='axvline - full height')
    #     plt.xticks(np.arange(0, 0.7, 0.2))
    # plt.show()

    # height
    height = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_target.iloc[elec_num + 1, 1:]-np.mean(df_target.iloc[elec_num + 1, 1:])
        peaks, _ = find_peaks(x, height=2)
        p = abs((peaks/125)-0.5)
        ind = np.argmin(p)
        height = np.concatenate((height, [x[peaks[ind]]]))
    AmplitudeT = height[2:]

    # distance
    distance = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_target.iloc[elec_num + 1, 1:]-np.mean(df_target.iloc[elec_num + 1, 1:])
        peaks, _ = find_peaks(x, distance=12)
        p5 = abs((peaks / 125) - 0.5)
        ind5 = np.argmin(p5)
        p2 = abs((peaks / 125) - 0.2)
        ind2 = np.argmin(p2)
        dydx = (x[peaks[ind5]]-x[peaks[ind2]])/(peaks[ind5]/125-peaks[ind2]/125)
        if len(peaks) < 2:
            dydx = 0
        distance = np.concatenate((distance, [dydx]))
    SlopeT = distance[2:]

    # prominence
    prominence = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_target.iloc[elec_num + 1, 1:]-np.mean(df_target.iloc[elec_num + 1, 1:])
        peaks, _ = find_peaks(x, height=2)
        p = abs((peaks / 125) - 0.5)
        ind = np.argmin(p)
        prominence = np.concatenate((prominence, [peaks[ind]/125]))
    LatencyT = prominence[2:]

    # width
    width = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_target.iloc[elec_num + 1, 1:]-np.mean(df_target.iloc[elec_num + 1, 1:])
        peaks, properties = find_peaks(x, height=2, width=2)
        p = abs((peaks / 125) - 0.5)
        ind = np.argmin(p)
        r = properties["right_ips"]
        l = properties["left_ips"]
        w = (r[ind]-l[ind])/125
        width = np.concatenate((width, [w]))
    PeakWidthT = width[2:]

    # distractor features
    # for elec_num in np.arange(1, 14):
    #     plt.subplot(4, 4, elec_num)
    #     x = df_distractor.iloc[elec_num + 1, 1:]-np.mean(df_distractor.iloc[elec_num + 1, 1:])
    #     peaks, properties = find_peaks(x, distance=12)
    #     # print(peaks/125)
    #     plt.plot(time, x)
    #     plt.plot(peaks/125, x[peaks], "x")
    #     # plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"]/125,
    #     #            xmax=properties["right_ips"]/125, color="C1")
    #     # plt.plot(time, np.zeros_like(x), "--", color="gray")
    #     plt.axvline(x=0.2, color='r', label='axvline - full height')
    #     plt.axvline(x=0.5, color='b', label='axvline - full height')
    #     plt.xticks(np.arange(0, 0.7, 0.2))
    # plt.show()

    # height
    height = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_distractor.iloc[elec_num + 1, 1:]-np.mean(df_distractor.iloc[elec_num + 1, 1:])
        peaks, _ = find_peaks(x, distance=12)
        p = abs((peaks / 125) - 0.5)
        ind = np.argmin(p)
        height = np.concatenate((height, [x[peaks[ind]]]))
    AmplitudeD = height[2:]

    # distance
    distance = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_distractor.iloc[elec_num + 1, 1:]-np.mean(df_distractor.iloc[elec_num + 1, 1:])
        peaks, _ = find_peaks(x, distance=12)
        p5 = abs((peaks / 125) - 0.5)
        ind5 = np.argmin(p5)
        p2 = abs((peaks / 125) - 0.2)
        ind2 = np.argmin(p2)
        dydx = (x[peaks[ind5]] - x[peaks[ind2]]) / (peaks[ind5] / 125 - peaks[ind2] / 125)
        if len(peaks) < 2:
            dydx = 0
        distance = np.concatenate((distance, [dydx]))
    SlopeD = distance[2:]

    # prominence
    prominence = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_distractor.iloc[elec_num + 1, 1:]-np.mean(df_distractor.iloc[elec_num + 1, 1:])
        peaks, _ = find_peaks(x, distance=12)
        p = abs((peaks / 125) - 0.4)
        ind = np.argmin(p)
        prominence = np.concatenate((prominence, [peaks[ind] / 125]))
    LatencyD = prominence[2:]

    # width
    width = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_distractor.iloc[elec_num + 1, 1:]-np.mean(df_distractor.iloc[elec_num + 1, 1:])
        peaks, properties = find_peaks(x, distance=12, width=2)
        p = abs((peaks / 125) - 0.5)
        ind = np.argmin(p)
        r = properties["right_ips"]
        l = properties["left_ips"]
        w = (r[ind] - l[ind]) / 125
        width = np.concatenate((width, [w]))
    PeakWidthD = width[2:]

    # baseline features
    # for elec_num in np.arange(1, 14):
    #     plt.subplot(4, 4, elec_num)
    #     x = df_baseline.iloc[elec_num + 1, 1:]-np.mean(df_baseline.iloc[elec_num + 1, 1:])
    #     peaks, properties = find_peaks(x, distance=12)
    #     # print(peaks)
    #     plt.plot(time, x)
    #     plt.plot(peaks/125, x[peaks], "x")
    #     # plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"]/125,
    #     #            xmax=properties["right_ips"]/125, color="C1")
    #     # plt.plot(time, np.zeros_like(x), "--", color="gray")
    #     plt.axvline(x=0.2, color='r', label='axvline - full height')
    #     plt.axvline(x=0.5, color='b', label='axvline - full height')
    #     plt.xticks(np.arange(0, 0.7, 0.2))
    # plt.show()

    # height
    height = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_baseline.iloc[elec_num + 1, 1:]-np.mean(df_baseline.iloc[elec_num + 1, 1:])
        peaks, _ = find_peaks(x, height=0)
        p = abs((peaks / 125) - 0.5)
        ind = np.argmin(p)
        height = np.concatenate((height, [x[peaks[ind]]]))
    AmplitudeB = height[2:]

    # distance
    distance = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_baseline.iloc[elec_num + 1, 1:]-np.mean(df_baseline.iloc[elec_num + 1, 1:])
        peaks, _ = find_peaks(x, distance=12)
        p5 = abs((peaks / 125) - 0.5)
        ind5 = np.argmin(p5)
        p2 = abs((peaks / 125) - 0.2)
        ind2 = np.argmin(p2)
        dydx = (x[peaks[ind5]] - x[peaks[ind2]]) / (peaks[ind5] / 125 - peaks[ind2] / 125)
        if len(peaks) < 2:
            dydx = 0
        distance = np.concatenate((distance, [dydx]))
    SlopeB = distance[2:]

    # prominence
    prominence = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_baseline.iloc[elec_num + 1, 1:]-np.mean(df_baseline.iloc[elec_num + 1, 1:])
        peaks, _ = find_peaks(x, distance=12)
        p = abs((peaks / 125) - 0.2)
        ind = np.argmin(p)
        prominence = np.concatenate((prominence, [peaks[ind] / 125]))
    LatencyB = prominence[2:]

    # width
    width = np.array([0, 0])
    for elec_num in np.arange(1, 14):
        x = df_baseline.iloc[elec_num + 1, 1:]-np.mean(df_baseline.iloc[elec_num + 1, 1:])
        peaks, properties = find_peaks(x, width=2)
        p = abs((peaks / 125) - 0.5)
        ind = np.argmin(p)
        r = properties["right_ips"]
        l = properties["left_ips"]
        w = (r[ind] - l[ind]) / 125
        width = np.concatenate((width, [w]))
    PeakWidthB = width[2:]

    # concat all classes
    Amplitude = np.concatenate((AmplitudeT, AmplitudeD, AmplitudeB))
    Slope = np.concatenate((SlopeT, SlopeD, SlopeB))
    Latency = np.concatenate((LatencyT, LatencyD, LatencyB))
    PeakWidth = np.concatenate((PeakWidthT, PeakWidthD, PeakWidthB))
    features = {'Amplitude': Amplitude, 'Slope': Slope, 'Latency': Latency, 'Peak width': PeakWidth}
    X = pd.DataFrame(data=features)

    # labels vector
    Tnum = 13 # Target is labeled as 0
    Dnum = 13 # Distractor is labeled as 1
    Bnum = 13 # Baseline is labeled as 2
    y = np.concatenate((np.zeros((Tnum,), dtype=int), np.ones((Dnum,), dtype=int), 2*np.ones((Bnum,), dtype=int)), axis=0)

    # saveFeatures(exp_path, Amplitude, Slope, Latency, PeakWidth, y)

    # Amplitude - distractor is higher than target
    # Slope - distractor is higher than target
    # Latency - distractor is lower than target
    # Peak width - distractor is lower than target

if __name__ == '__main__':
    main()