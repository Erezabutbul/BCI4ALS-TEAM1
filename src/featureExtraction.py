from dict2Mat import main as dict2Mat_main
# import os
from parameters import *
# import pandas as pd
# import numpy as np


def getEXPFoldersList(main_folder):
    # get all the experiment folders
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('EXP')]
    return exp_folders


def getTrialFilesList(currTrialEEGSignalPath):
    trialFilesList = [f for f in os.listdir(currTrialEEGSignalPath) if f.endswith('.csv')]
    return trialFilesList


def concatAllTrialsByClass(marker_type, currTrialEEGSignalPath):
    trialFilesList = getTrialFilesList(currTrialEEGSignalPath)
    outputDf_exp = pd.DataFrame()
    for trial in trialFilesList:
        trial_path = os.path.join(currTrialEEGSignalPath, trial)
        currDf = pd.read_csv(trial_path)
        # TODO - trial and electrode rejection, electrodes are hardcoded here
        channels = [0, 2, 3, 5, 9]
        # iterate over indexList and extract matching rows
        for i in channels:
            row_df = currDf.iloc[i:i + 1, :]
            outputDf_exp = pd.concat([outputDf_exp, row_df])
    outputDf_exp.to_csv(currTrialEEGSignalPath + f"All_Trials_{marker_type}.csv", index=False)
    return outputDf_exp


def main(exp_path, state):

    if state == 'train':
        # the outputs that will be concatenated
        outputDf_target = pd.DataFrame()
        outputDf_distractor = pd.DataFrame()
        # go over every exp and activate dict2Mat & concat all the trials
        expFoldersList = getEXPFoldersList(output_files)
        for expFolder in expFoldersList:
            currExpPath = output_files + expFolder
            dict2Mat_main(currExpPath)
            # for each marker_type concat all the trial together
            for marker_type in marker_types:
                if marker_type == "baseLine":
                    continue
                currTrialEEGSignalPath = currExpPath + f"/cut_data_by_class/{marker_type}/Trial_EEG_Signal_{marker_type}/"
                concateneted_trials = concatAllTrialsByClass(marker_type, currTrialEEGSignalPath)
                if marker_type == 'target':
                    outputDf_target = pd.concat([outputDf_target, concateneted_trials])
                if marker_type == 'distractor':
                    outputDf_distractor = pd.concat([outputDf_distractor, concateneted_trials])

        # save features matrix for all EXP available
        train_features_folder_path = os.path.join(output_files, featuresAndModel_folder_name, train_features_folder_name)
        outputDf_target.to_csv(train_features_folder_path + f"Features_target.csv")
        outputDf_distractor.to_csv(train_features_folder_path + f"Features_distractor.csv")

        # create labels vector
        num_target = outputDf_target.shape[0]
        num_distractor = outputDf_distractor.shape[0]
        labels_vec = np.concatenate((np.ones(num_target), np.zeros(num_distractor)))
        np.savetxt(train_features_folder_path + label_file_name, labels_vec, delimiter=",")
        finalFeatureMatrix = pd.concat([outputDf_target, outputDf_distractor])
        finalFeatureMatrix.to_csv(train_features_folder_path + train_features_file_name)


    # test condition
    else:
        # go over curr test exp and activate dict2Mat
        dict2Mat_main(exp_path)
        outputDf_condition1 = pd.DataFrame()
        outputDf_condition2 = pd.DataFrame()
        # save the features in feature folder at exp_path (for example: "testSet/test_03_01_2023 at 06_45_20_PM")
        for marker_type in marker_types:
            if marker_type == "baseLine":
                    continue
            currTrialEEGSignalPath = exp_path + f"/cut_data_by_class/{marker_type}/Trial_EEG_Signal_{marker_type}/"
            concateneted_trials = concatAllTrialsByClass(marker_type, currTrialEEGSignalPath)
            if marker_type == 'target':
                outputDf_condition1 = pd.concat([outputDf_condition1, concateneted_trials])
            if marker_type == 'distractor':
                outputDf_condition2 = pd.concat([outputDf_condition2, concateneted_trials])
        
        test_feature_folder_path = os.path.join(exp_path, test_features_folder_name)
        print(test_feature_folder_path)
        os.makedirs(test_feature_folder_path, exist_ok=False)
        finalTestFeatureMatrix = pd.concat([outputDf_condition1, outputDf_condition2])
        finalTestFeatureMatrix.to_csv(test_feature_folder_path + test_features_file_name, index=False)

if __name__ == '__main__':
    main()
