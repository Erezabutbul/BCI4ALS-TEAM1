import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from parameters import *


def saveFeatures(exp_path, X, y):
    # save to "EXP_{date}" directory
    featuresDir = exp_path + feature_folder_path
    os.makedirs(featuresDir, exist_ok=True)
    # X.to_csv(featuresDir + feature_file_name)
    np.savetxt(featuresDir + feature_of_test_file_name, X, delimiter=",")
    # Save the array to a CSV file
    np.savetxt(featuresDir + "test_" + label_file_name, y, delimiter=",")


# height feature extraction
def getHight(df_marker, condition, elec_num):
    x = df_marker.iloc[elec_num, 1:] - np.mean(df_marker.iloc[elec_num, 1:])
    # if condition == 'target':
    #     peaks, _ = find_peaks(x, height=2)
    # elif condition == 'distractor':
    #     peaks, _ = find_peaks(x, distance=12)
    # if elec_num == 12:
    #     time = pd.DataFrame(np.linspace(0, numOfSamplesToCut / samplingRate, numOfSamplesToCut))  # 75 samples, fs=125Hz
    #     plt.plot(time, x)
    # if len(peaks) == 0:
    #     peaks, _ = find_peaks(x, height=0.5)
    # p = abs((peaks/samplingRate)-0.5)
    # ind = np.argmin(p)
    limleft = round(0.45 * samplingRate)
    limright = round(0.55 * samplingRate)

    return max(x[limleft:limright])


# distance feature extraction
def getDistance(df_marker, elec_num):
    x = df_marker.iloc[elec_num, 1:] - np.mean(df_marker.iloc[elec_num, 1:])
    # peaks, _ = find_peaks(x, distance=12)
    # p5 = abs((peaks / samplingRate) - 0.5)
    # ind5 = np.argmin(p5)
    # p2 = abs((peaks / samplingRate) - 0.2)
    # ind2 = np.argmin(p2)
    # dydx = (x[peaks[ind5]] - x[peaks[ind2]]) / ((peaks[ind5] / samplingRate) - (peaks[ind2] / samplingRate))
    # if len(peaks) < 2:
    #     dydx = 0
    limleft5 = round(0.45 * samplingRate)
    limright5 = round(0.55 * samplingRate)
    limleft2 = round(0.15 * samplingRate)
    limright2 = round(0.25 * samplingRate)

    y2 = max(x[limleft5:limright5])
    y1 = min(x[limleft2:limright2])
    x2 = 0.5
    x1 = 0.2
    dydx = (y2 - y1) / (x2 - x1)

    return dydx


# Latency feature extraction
def getLatency(df_marker, condition, elec_num):
    x = df_marker.iloc[elec_num, 1:] - np.mean(df_marker.iloc[elec_num, 1:])
    # if condition == 'target':
    #     peaks, _ = find_peaks(x, height=2)
    # elif condition == 'distractor':
    #     peaks, _ = find_peaks(x, distance=12)
    # p = abs((peaks / samplingRate) - 0.4)
    # ind = np.argmin(p)
    limleft = round(0.35 * samplingRate)
    limright = round(0.45 * samplingRate)

    return max(x[limleft:limright])


def getWidth(df_marker, elec_num):
    # width
    x = df_marker.iloc[elec_num, 1:] - np.mean(df_marker.iloc[elec_num, 1:])
    # peaks, properties = find_peaks(x, distance=12, width=2)
    # p = abs((peaks / samplingRate) - 0.5)
    # ind = np.argmin(p)
    # r = properties["right_ips"]
    # l = properties["left_ips"]
    # w = (r[ind] - l[ind]) / samplingRate

    # signal sum
    w = np.sum(x)
    return w


def getSTD(df_marker, elec_num):
    x = df_marker.iloc[elec_num, 1:] - np.mean(df_marker.iloc[elec_num, 1:])
    standiv = np.std(x)
    std = pow(standiv, 2)
    return std


def main(exp_path):
# def main():
    # Testing
    # exp_path = "output_files/testSet/test_03_01_2023 at 06_45_20_PM/"

    blocks = np.arange(0, 5)
    electrodes = np.arange(0, 13)
    markers = ["target", "distractor"]
    listOfMatrix = list()
    # labelsList = list()

    featureMatrix = pd.DataFrame(np.zeros((2 * len(blocks), 65)))
    for block_num in blocks:
        for elec_num in electrodes:
            for label in np.arange(len(markers)):
                if label == 0:
                    df = pd.read_csv(
                        exp_path + f"cut_data_by_class/{markers[label]}/Mean_EEG_Signal_{markers[label]}/" + f"AVG_block_num_{block_num}.csv")
                    featureMatrix.loc[2 * block_num, 5 * elec_num] = getHight(df, markers[label], elec_num )
                    featureMatrix.loc[2 * block_num, 5 * elec_num + 1] = getDistance(df, elec_num)
                    featureMatrix.loc[2 * block_num, 5 * elec_num + 2] = getLatency(df, markers[label], elec_num)
                    featureMatrix.loc[2 * block_num, 5 * elec_num + 3] = getWidth(df, elec_num )
                    featureMatrix.loc[2 * block_num, 5 * elec_num + 4] = getSTD(df, elec_num)
                else:
                    df = pd.read_csv(
                        exp_path + f"cut_data_by_class/{markers[label]}/Mean_EEG_Signal_{markers[label]}/" + f"AVG_block_num_{block_num}.csv")
                    featureMatrix.loc[2 * block_num + 1, 5 * elec_num] = getHight(df, markers[label], elec_num )
                    featureMatrix.loc[2 * block_num + 1, 5 * elec_num + 1] = getDistance(df, elec_num)
                    featureMatrix.loc[2 * block_num + 1, 5 * elec_num + 2] = getLatency(df, markers[label],
                                                                                        elec_num)
                    featureMatrix.loc[2 * block_num + 1, 5 * elec_num + 3] = getWidth(df, elec_num)
                    featureMatrix.loc[2 * block_num + 1, 5 * elec_num + 4] = getSTD(df, elec_num)
    listOfMatrix.append(featureMatrix)

    finalMatrix = listOfMatrix[0]
    # labelsVec = np.array([0, 1, 1, 0, 0, 1, 1, 0, 0, 1])
    # labelsVec = labelsVec.reshape(-1, 1)
    saveFeatures(exp_path, finalMatrix, labelsVec)


if __name__ == '__main__':
    main()
