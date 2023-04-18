import ast
import os.path
import random

import numpy as np

from parameters import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from localVote import main as vote
# import os
# import pandas as pd

def getEXPFoldersList(main_folder):
    # get all the experiment folders
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('EXP')]
    return exp_folders

def getTrialsFoldersList(main_folder):
    # get all the experiment folders
    trial_folders = [f for f in os.listdir(main_folder) if f.startswith('Trial_num_')]
    return trial_folders


def generateRandomExpAndBlock():
    expFoldersList = getEXPFoldersList(output_files)
    # get random EXP
    random_EXP_index = random.randrange(len(expFoldersList))
    # print(expFoldersList[random_index])
    return expFoldersList[random_EXP_index]


def getIndexOfBlockInFile(pathOfRandomEXP, random_block_num):
    indexesOfmarkerTypeInFile = list()
    for marker_type in marker_types:
        if marker_type == "baseLine":
            continue
        df = pd.read_csv(
            output_files + pathOfRandomEXP + f"/cut_data_by_class/{marker_type}/class{marker_type}.csv")
        # removing indexes
        # cut the index column, and
        # according to the number of samples that supposed to see in the current sampling rate
        df = df.iloc[:, 1:(numOfSamplesToCut + 1)]
        start_block_indices = df.index[df['0'] == 'startBlock'].tolist()
        random_block_index_in_file = start_block_indices[random_block_num]
        indexesOfmarkerTypeInFile.append(random_block_index_in_file)
        if random_block_num + 1 < len(start_block_indices):
            indexesOfmarkerTypeInFile.append(start_block_indices[random_block_num + 1])
        else:
            indexesOfmarkerTypeInFile.append(None)
        # print("the random block is num: " + str(random_block_num))
    return indexesOfmarkerTypeInFile


def getRandomBlockNum(exp_random_path):
    # get random block
    # read file - OF TARGET
    df = pd.read_csv(
        output_files + exp_random_path + f"/cut_data_by_class/target/classtarget.csv")
    # removing indexes
    # cut the index column, and
    # according to the number of samples that supposed to see in the current sampling rate
    df = df.iloc[:, 1:(numOfSamplesToCut + 1)]

    # Find the indices of the rows containing the startBlock markers
    start_block_indices = df.index[df['0'] == 'startBlock'].tolist()
    random_block_index = random.randrange(len(start_block_indices))
    return random_block_index


def cutBlockFromFile(random_exp_path, startIndex, EndIndex, marker_type, channels):
    main_folder = output_files + random_exp_path + f"/cut_data_by_class/{marker_type}/Trial_EEG_Signal_{marker_type}/"
    trial_list = getTrialsFoldersList(main_folder)

    if EndIndex is not None:
        trialFilesList = range(startIndex+1, EndIndex)
    else:
        trialFilesList = range(startIndex+1, len(trial_list))

    outputDf_exp = pd.DataFrame()

    for trial in trialFilesList:
        trial_path = main_folder + "Trial_num_" + str(trial) + ".csv"
        currDf = pd.read_csv(trial_path)
        # extract selected channels from trial
        currDf = currDf.iloc[channels, :]
        outputDf_exp = pd.concat([outputDf_exp, currDf])
    # os.makedirs(main_folder + "testBLOCK", exist_ok=True)
    # outputDf_exp.to_csv(main_folder + "testBLOCK/" + f"test_BLOCK_{marker_type}.csv", index=False)

    return outputDf_exp



def is_array_in_2d_array(array_1d, array_2d):
    for row in array_2d:
        if np.array_equal(array_1d, row):
            return True
    return False



def main(channels):
    sum_all_test_results = 0
    for i in range(100):
        pathOfRandomEXP = generateRandomExpAndBlock()
        # pathOfRandomEXP = "EXP_13_03_2023 at 11_03_00_AM"
        random_block_num = getRandomBlockNum(pathOfRandomEXP)
        # random_block_num = 3
        indexesOfMarkerTypeInFile = getIndexOfBlockInFile(pathOfRandomEXP, random_block_num)
        startIndexOfTarget, endIndexOfTarget, startIndexOfDistractor, endIndexOfDistractor = indexesOfMarkerTypeInFile
        # print(pathOfRandomEXP)
        # print("the BLOCK IS: "+str(random_block_num))
        # print(indexesOfMarkerTypeInFile)

        # cut the current blocks from files
        targetDF = cutBlockFromFile(pathOfRandomEXP, startIndexOfTarget, endIndexOfTarget, "target", channels)
        distractorDF = cutBlockFromFile(pathOfRandomEXP, startIndexOfDistractor, endIndexOfDistractor, "distractor", channels)
        # print(targetDF)
        # print(type(targetDF))
        # print(type(distractorDF))
        # print(distractorDF)

        # concatenate , save and make labels matrix
        x_test = pd.concat([targetDF, distractorDF])
        x_test = x_test.iloc[:, 1:]
        num_target = targetDF.shape[0]
        num_distractor = distractorDF.shape[0]
        y_test = np.concatenate((np.ones(num_target, dtype=int), np.zeros(num_distractor, dtype=int)))

        # load feature matrix and cut out these blocks, save
        model_exp_path = output_files + featuresAndModel_folder_name + train_features_folder_name
        # fixing file to be only numbers
        full_X = pd.read_csv(model_exp_path + train_features_file_name, header=None)
        # print(full_X)
        # Reset the index of both dataframes
        full_X = full_X.reset_index(drop=True)
        # print(full_X)
        x_test = x_test.reset_index(drop=True)
        # Get the index values from x_test
        # test_index = x_test.index

        # Drop the rows from full_x that also exist in x_test
        # full_X.drop(test_index, inplace=True)
        # print(full_X)
        # print(x_test)

        # make the same columns names for both DF's
        # distinct_df = full_X.set_axis(list(x_test.columns), axis=1, inplace=False)
        # columns_names = list(x_test.columns)
        # merged_df = pd.merge(distinct_df, x_test, how='outer', indicator=True, on=columns_names)
        # result_df = merged_df[merged_df['_merge'].isin(['left_only', 'right_only'])]


        full_X_arr = full_X.values

        # print("FULL FEATUREMATRIX SIZE "+str(len(full_X_arr)))
        # print(len(full_X_arr[0]))
        x_test_arr = x_test.values
        # print("TOTAL BLOCK TRIALS: "+ len(x_test_arr))
        # print(len(x_test_arr[0]))

        n = len(full_X_arr) - len(x_test_arr)

        result_arr = np.zeros((n, len(full_X_arr[0])))
        index = 0
        for array in full_X_arr:
            if not is_array_in_2d_array(array, x_test_arr) and index < n:
                result_arr[index] = array
                index += 1
        # print("the diduction of the block is competble with the size of matrix: " + str((len(full_X_arr) - len(x_test_arr)) == len(result_arr)))
        # print(len(result_arr[0]))
        #############################################
        # distinct_df = full_X.set_axis(list(x_test.columns), axis=1, inplace=False)
        # columns_names = list(x_test.columns)
        # merged_df = pd.merge(distinct_df, x_test, how='outer', indicator=True, on=columns_names)
        # result_df = merged_df[(merged_df['_merge'] == 'left_only') | (merged_df['_merge'] == 'right_only')]
        # print(result_df)
        # Drop the 'merge' column
        # result_df = result_df.drop(columns=['_merge'])

        ####################################################################
        label_vec = np.loadtxt(model_exp_path + label_file_name)
        # print(result_df)
        # Remove the rows
        y_train = label_vec[num_target:-num_distractor]
        # Remove the rows using np.delete()
        # label_vec = np.delete(label_vec, slice(0, num_target), axis=0)
        # y_train = np.delete(label_vec, slice(-num_distractor, None), axis=0)

        # print(y_train)
        # print(len(y_train))
        # print(result_df)
        # print(result_df)
        # print(y_train)

        # save
        # dir_path = pathOfRandomEXP + "K_fold_test"
        # os.makedirs(dir_path, exist_ok=True)


        # train model with this data
        model = RandomForestClassifier()
        model.fit(result_arr, y_train)
        # print("Random Forest model")
        #
        # Prediction
        y_pred = model.predict(x_test_arr)
        # print("Random Forest Predicted values:")
        # print("numbers of targets: "+ str(num_target))
        # print("numbers of distractors: "+ str(num_distractor))
        # print("num of trial in y_pred: "+str(len(y_pred)/5))
        sum_all_test_results += vote(y_pred, y_test, num_target)
        # print(type(x_test))

        # Prediction Factors
        # print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
        # print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
    print("\n\nfinal result in percentage: " + str(sum_all_test_results/100))
    print("number of success : " + str(sum_all_test_results))

    return sum_all_test_results




if __name__ == '__main__':
    main()
