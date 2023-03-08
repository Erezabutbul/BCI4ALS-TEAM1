# Importing the required packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from parameters import *


def saveFeatures(exp_path, X, y):
    # save to "EXP_{date}" directory
    featureDir = exp_path + feature_folder_path
    os.makedirs(featureDir, exist_ok=True)
    # X.to_csv(featuresDir + feature_file_name)
    np.savetxt(featureDir + feature_file_name, X, delimiter=",")
    # Save the array to a CSV file
    np.savetxt(featureDir + label_file_name, y, delimiter=",")


def getAmplitude(df_marker, elec_num):
    amp = df_marker.iloc[elec_num, 1:] - np.mean(df_marker.iloc[elec_num, 1:])
    start_ind = round(samplingRate * 0.4)
    end_ind = round(samplingRate * 0.55)
    return max(amp[start_ind:end_ind])


def getArea(df_marker, elec_num):
    amp = df_marker.iloc[elec_num, 1:] - np.mean(df_marker.iloc[elec_num, 1:])
    ind = round(samplingRate * 0.3)
    return np.sum(amp[ind:])


def getSTD(df_marker, elec_num):
    x = df_marker.iloc[elec_num, 1:] - np.mean(df_marker.iloc[elec_num, 1:])
    standiv = np.std(x)
    std = pow(standiv, 2)
    return std


def getLatency(df_marker, elec_num):
    amp = df_marker.iloc[elec_num, 1:] - np.mean(df_marker.iloc[elec_num, 1:])
    start_ind = round(samplingRate * 0.4)
    end_ind = round(samplingRate * 0.55)
    return np.argmax(amp[start_ind:end_ind]) / samplingRate


def main(exp_path):
    # load block by block and extract features
    # concat all the features into one futureMatrix and save it
    # TODO - need to find a way to select the experiment
    # maybe read from a txt file that has the paths row by row
    file_exp_path = exp_path + "/featuresAndModel/"
    # that we want to extract features from
    experiment = ["output_files/EXP_02_01_2023 at 12_12_58_PM/", "output_files/EXP_02_01_2023 at 12_22_52_PM/"]
    blocks = np.arange(0, 5)
    electrodes = np.array([0, 2, 6, 7, 9, 10, 11, 12])
    markers = ["target", "distractor"]
    listOfMatrix = list()
    labelsList = list()
    featureNum = 4
    colOfMatrix = len(electrodes) * featureNum
    j = 0
    for exp_num in np.arange(len(experiment)):
        featureMatrix = pd.DataFrame(np.zeros((2 * len(blocks), colOfMatrix)))
        for block_num in blocks:
            for elec_num in electrodes:
                for label in np.arange(len(markers)):
                    if label == 0:
                        df = pd.read_csv(
                            f"{experiment[exp_num]}" + f"cut_data_by_class/{markers[label]}/Mean_EEG_Signal_{markers[label]}/" + f"AVG_block_num_{block_num}.csv")
                        featureMatrix.loc[2 * block_num, featureNum * j] = getAmplitude(df, elec_num)
                        featureMatrix.loc[2 * block_num, featureNum * j + 1] = getArea(df, elec_num)
                        featureMatrix.loc[2 * block_num, featureNum * j + 2] = getLatency(df, elec_num)
                        featureMatrix.loc[2 * block_num, featureNum * j + 3] = getSTD(df, elec_num)
                    else:
                        df = pd.read_csv(
                            f"{experiment[exp_num]}" + f"cut_data_by_class/{markers[label]}/Mean_EEG_Signal_{markers[label]}/" + f"AVG_block_num_{block_num}.csv")
                        featureMatrix.loc[2 * block_num + 1, featureNum * j] = getAmplitude(df, elec_num)
                        featureMatrix.loc[2 * block_num + 1, featureNum * j + 1] = getArea(df, elec_num)
                        featureMatrix.loc[2 * block_num + 1, featureNum * j + 2] = getLatency(df, elec_num)
                        featureMatrix.loc[2 * block_num + 1, featureNum * j + 3] = getSTD(df, elec_num)
                j = j + 1
            j = 0
            labelsList.append(0)
            labelsList.append(1)
        listOfMatrix.append(featureMatrix)
    # TODO -
    # concatenate features with loop
    # create a labels vector from original samples

    # print(listOfMatrix)
    # currMatrix = listOfMatrix[0]
    # for i in range(1, len(listOfMatrix)-1):
    #     currMatrix = np.concatenate((currMatrix, listOfMatrix[i]))
    print(listOfMatrix[0])
    finalMatrix = np.concatenate((listOfMatrix[0], listOfMatrix[1]))
    labelsVec = np.array(labelsList)
    labelsVec = labelsVec.reshape(-1, 1)
    saveFeatures(file_exp_path, finalMatrix, labelsVec)
    # print(labelsVec.shape)


if __name__ == '__main__':
    main()
