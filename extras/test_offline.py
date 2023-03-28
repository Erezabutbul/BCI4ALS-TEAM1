# Importing the required packages
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

def getEXPFoldersList(main_folder):
    # get all the experiment folders
    # exp_folders = [f for f in os.listdir(main_folder) if
    #                os.path.isdir(os.path.join(main_folder, f)) and f.startswith('EXP')]
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('test')]
    return exp_folders


# see that this is before the input output of model
def main():
    listOfEXP = getEXPFoldersList(output_files + "/testSet")
    # the outputs that will be concatenated
    outputDf_target_features = pd.DataFrame()
    outputDf_distractor_features = pd.DataFrame()
    outputDf_target_labels = pd.DataFrame()
    outputDf_distractor_labels = pd.DataFrame()

    for expFolder in listOfEXP:
        currExpPath = output_files + "/testSet/" + expFolder
        # currFeatures = pd.read_csv(currExpPath + "/" + train_features_file_name, header=None)
        # currLabels = pd.read_csv(currExpPath + "/" + label_file_name, header=None)

        currTargetFeatures = pd.read_csv(currExpPath + "/" + target_train_features_file_name, header=None)
        currDistractorFeatures = pd.read_csv(currExpPath + "/" + distractor_train_features_file_name, header=None)
        # currTargetLabels = pd.read_csv(currExpPath + "/" + target_label_file_name, header=None)
        # currDistractorLabels = pd.read_csv(currExpPath + "/" + distractor_label_file_name, header=None)

        # outputDf_features = pd.concat([outputDf_features, currFeatures])
        # outputDf_labels = pd.concat([outputDf_labels, currLabels], axis=0)

        outputDf_target_features = pd.concat([outputDf_target_features, currTargetFeatures])
        outputDf_distractor_features = pd.concat([outputDf_distractor_features, currDistractorFeatures])
        # outputDf_target_labels = pd.concat([outputDf_target_labels, currTargetLabels], axis=0)
        # outputDf_distractor_labels = pd.concat([outputDf_distractor_labels, currDistractorLabels], axis=0)

    outputDf_features = pd.concat([outputDf_target_features, outputDf_distractor_features])
    # outputDf_labels = pd.concat([outputDf_target_labels, outputDf_distractor_labels])

    test_features_folder_path = output_files + "testSet/" #output_files + "testSet" #os.path.join(output_files, "testSet")
    outputDf_features.to_csv(test_features_folder_path + "newTESTFeatures.csv", header=False, index=False)
    # outputDf_labels.to_csv(test_features_folder_path + "newTESTLabels.csv", header=False, index=False)

    root = tk.Tk()
    root.withdraw()

    model_label = tk.Label(root, text="Please select a model to test:")
    model_label.pack()

    test_model_path = filedialog.askopenfilename()
    test_model = pickle.load(open(test_model_path, 'rb'))

    features_lable = tk.Label(root, text="Please select feauteres folder:")
    features_lable.pack()
    test_features_path = filedialog.askopenfilename()

    testFeatureMatrix = pd.read_csv(test_features_path, header=None)
    # test_set_labels_vec = np.loadtxt(
    #     "C:\\Users\\Erez\\Desktop\\BCI4ALS-TEAM1\\src\\output_files\\featuresAndModel\\features\\labels_vector_test.csv")
    # X_train, X_test, y_train, y_test = train_test_split(testFeatureMatrix, test_set_labels_vec, test_size=0.2, random_state=100)
    y_pred = test_model.predict(testFeatureMatrix)
    print(type(y_pred))
    print("Predicted values:")
    print(y_pred)
    print("\n\n")
    exp
    condition1_features = pd.read_csv(exp_path + target_test_features_file_name, header=False, index=False)
    condition1_num_of_trials = condition1_features.shape[0]
    vote(y_pred, condition1_num_of_trials, exp_path)
    # test_set_labels_vec = np.loadtxt("C:\\Users\\Erez\\Desktop\\BCI4ALS-TEAM1\\src\\output_files\\featuresAndModel\\features\\labels_vector_test.csv")
    # print("Accuracy:", accuracy_score(test_set_labels_vec, y_pred) * 100)



if __name__ == '__main__':
    main()
