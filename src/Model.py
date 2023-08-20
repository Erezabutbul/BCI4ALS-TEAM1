# Importing the required packages
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import pickle
import tkinter as tk
from tkinter import filedialog
from parameters import *
from Vote import main as vote


"""
get all the experiment folders
"""
def getEXPFoldersList(main_folder):
    # get all the experiment folders
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('EXP')]
    return exp_folders


def concatFeatures(condition_set_path):
    """
    Concatenate features and labels from multiple experiment folders.

    Args:
        condition_set_path (str or list): Path(s) to the experiment folders.

    Returns:
        pandas.DataFrame: Concatenated feature matrix.
        pandas.DataFrame: Concatenated label matrix.
        int: Index indicating the end of target condition features.

    """
    listOfEXP = condition_set_path
    if type(listOfEXP) == str:
        listOfEXP = [listOfEXP]
    # the outputs that will be concatenated
    outputDf_target_features = pd.DataFrame()
    outputDf_distractor_features = pd.DataFrame()
    outputDf_target_labels = pd.DataFrame()
    outputDf_distractor_labels = pd.DataFrame()

    for expFolder in listOfEXP:
        currExpPath = output_files + expFolder

        currTargetFeatures = pd.read_csv(currExpPath + "/" + target_train_features_file_name, header=None)
        currDistractorFeatures = pd.read_csv(currExpPath + "/" + distractor_train_features_file_name, header=None)
        currTargetLabels = pd.read_csv(currExpPath + "/" + target_label_file_name, header=None)
        currDistractorLabels = pd.read_csv(currExpPath + "/" + distractor_label_file_name, header=None)

        outputDf_target_features = pd.concat([outputDf_target_features, currTargetFeatures])
        outputDf_distractor_features = pd.concat([outputDf_distractor_features, currDistractorFeatures])
        outputDf_target_labels = pd.concat([outputDf_target_labels, currTargetLabels], axis=0)
        outputDf_distractor_labels = pd.concat([outputDf_distractor_labels, currDistractorLabels], axis=0)

    endOfcon1 = outputDf_target_features.shape[0]

    outputDf_features = pd.concat([outputDf_target_features, outputDf_distractor_features])
    outputDf_labels = pd.concat([outputDf_target_labels, outputDf_distractor_labels])

    return outputDf_features, outputDf_labels, endOfcon1


def main(gui_mode , exp_path=None):
    """
    Main function for model training and testing.

    Args:
        gui_mode (str): Mode of operation ("TRAIN" or "TEST").
        exp_path (str, optional): Path to the experiment folder for testing mode.

    Returns:
        None

    """
    if gui_mode == "TRAIN":

        listOfEXP = getEXPFoldersList(output_files)
        outputDf_features, outputDf_labels, endOfcon1 = concatFeatures(listOfEXP)
        train_features_folder_path = os.path.join(output_files, featuresAndModel_folder_name)
        createFolder(train_features_folder_path)
        outputDf_features.to_csv(train_features_folder_path + "newFeatures.csv", header=False, index=False)
        outputDf_labels.to_csv(train_features_folder_path + "newLabels.csv", header=False, index=False)

        #make SVC and RANDOM FOREST directories if doesn't exist
        models_folder_path = os.path.join(output_files + featuresAndModel_folder_name + train_model_folder_name)
        os.makedirs(models_folder_path, exist_ok=True)
        SVC_dir_path = models_folder_path + "SVC/"
        RandomForest_dir_path = models_folder_path + "RandomForest/"

        os.makedirs(SVC_dir_path, exist_ok=True)
        os.makedirs(RandomForest_dir_path, exist_ok=True)


        # load "featuresMatrix.csv" and "labels.csv"
        model_exp_path = output_files + featuresAndModel_folder_name + train_features_folder_name
        X = outputDf_features
        X = X.dropna(axis=1)

        y = outputDf_labels
        y = y.values.ravel()
        print(type(X))

        # separate to training and learning sets: X is the data by feature, y is the class vector(target, distractor, baseline)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

        # SVC (sklearn Support Vector Classification)
        model = LinearSVC()
        model.fit(X_train, y_train)
        print("SVC model")



        # Prediction
        y_pred = model.predict(X_test)
        print("LinearSVC Predicted values:")
        # print(y_pred)
        #
        # Prediction Factors
        # print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
        # print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
        # print("Report:", classification_report(y_test, y_pred))

        model = LinearSVC()
        model.fit(X, y)
        # save the SVCModel
        SVC_Model_filename = SVC_dir_path + f'finalized_SVC_Model_{date}.sav'
        pickle.dump(model, open(SVC_Model_filename, 'wb'))

        model = RandomForestClassifier()
        model.fit(X, y)

        # save the RandomForest model
        RandomForest_filename = RandomForest_dir_path + f'finalized_RandomForest_Model_{date}.sav'
        pickle.dump(model, open(RandomForest_filename, 'wb'))

        #test for evaluation - not needed for system functionality
        """
        # separate to training and learning sets: X is the data by feature, y is the class vector(target, distractor, baseline)
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)
        # SVC (sklearn Support Vector Classification)
        # model = LinearSVC()
        # model.fit(X_train, y_train)
        # print("SVC model")
        # Prediction
        # y_pred = model.predict(X_test)
        # print("LinearSVC Predicted values:")
        # print(y_pred)
        #
        # Prediction Factors
        # print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
        # print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
        # print("Report:", classification_report(y_test, y_pred))
        # Random Forest
        # model = RandomForestClassifier()
        # model.fit(X_train, y_train)
        # print("Random Forest model")
        # Prediction
        # y_pred = model.predict(X_test)
        # print("Random Forest Predicted values:")
        # print(y_pred)
        """


    if gui_mode == "TEST":
        # load models
        root = tk.Tk()
        root.withdraw()
        test_model_path = filedialog.askopenfilename() # filedialog.askopenfilename("Choose model")
        test_model = pickle.load(open(test_model_path, 'rb'))

        # programmer mode - if you want to do data science - you can choose feature matrix as well
            # # load test features
            # root = tk.Tk()
            # root.withdraw()
            # test_features_path = filedialog.askopenfilename() #filedialog.askopenfilename("Choose features")
            # # cut to feed the model
            # testFeatureMatrixRAW = pd.read_csv(test_features_path)
            # num_columns = len(testFeatureMatrixRAW.columns)
            # testFeatureMatrix = pd.read_csv(test_features_path, header=None, usecols=range(1, num_columns), skiprows=1)

        testFeatureMatrixRAW = pd.read_csv(exp_path + "/" + test_features_file_name)
        y_pred_proba = test_model.predict_proba(testFeatureMatrixRAW)
        print("Predicted values:")
        condition1_features = pd.read_csv(exp_path + "target_test_features_Matrix.csv", header=None)
        condition1_num_of_trials = condition1_features.shape[0]
        condition_1_AVG_TARGET_proba_precentage, condition_2_AVG_TARGET_proba_precentage, condition_1_voting_results_vec, condition_2_voting_results_vec = vote(y_pred_proba, condition1_num_of_trials, exp_path, "REAL TEST")
        # print("Accuracy:", accuracy_score(test_set_labels, y_pred) * 100)
        file = open(exp_path + "/pics_allocation.txt", "r")
        lines = file.readlines()
        #################### proba vote ##################################
        print("\n\nThe selected is: ")
        if condition_1_AVG_TARGET_proba_precentage > condition_2_AVG_TARGET_proba_precentage:
            print("prediction is 1 ")
            print(f"which means: {lines[1]}")
            print("precentage of confidence: ", condition_1_AVG_TARGET_proba_precentage)
        elif condition_1_AVG_TARGET_proba_precentage < condition_2_AVG_TARGET_proba_precentage:
            print("prediction is 0 ")
            print(f"which means: {lines[3]}")
            print("precentage of confidence: ", condition_2_AVG_TARGET_proba_precentage)

        else:
            print("DON'T HAVE VALID PREDICTION")

if __name__ == '__main__':
    main()
