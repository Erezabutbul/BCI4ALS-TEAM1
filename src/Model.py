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
from votingEXP import main as vote

def getEXPFoldersList(main_folder):
    # get all the experiment folders
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('EXP')]
    return exp_folders

# def main(exp_path):
def main():
    if modes[mode] == "TRAIN":

        listOfEXP = getEXPFoldersList(output_files)
        # the outputs that will be concatenated
        outputDf_target_features = pd.DataFrame()
        outputDf_distractor_features = pd.DataFrame()
        outputDf_target_labels = pd.DataFrame()
        outputDf_distractor_labels = pd.DataFrame()


        for expFolder in listOfEXP:
            currExpPath = output_files + expFolder
            # currFeatures = pd.read_csv(currExpPath + "/" + train_features_file_name, header=None)
            # currLabels = pd.read_csv(currExpPath + "/" + label_file_name, header=None)

            currTargetFeatures = pd.read_csv(currExpPath + "/" + target_train_features_file_name, header=None)
            currDistractorFeatures = pd.read_csv(currExpPath + "/" + distractor_train_features_file_name, header=None)
            currTargetLabels = pd.read_csv(currExpPath + "/" + target_label_file_name, header=None)
            currDistractorLabels = pd.read_csv(currExpPath + "/" + distractor_label_file_name, header=None)

            # outputDf_features = pd.concat([outputDf_features, currFeatures])
            # outputDf_labels = pd.concat([outputDf_labels, currLabels], axis=0)

            outputDf_target_features = pd.concat([outputDf_target_features, currTargetFeatures])
            outputDf_distractor_features = pd.concat([outputDf_distractor_features, currDistractorFeatures])
            outputDf_target_labels = pd.concat([outputDf_target_labels, currTargetLabels], axis=0)
            outputDf_distractor_labels = pd.concat([outputDf_distractor_labels, currDistractorLabels], axis=0)

        outputDf_features = pd.concat([outputDf_target_features, outputDf_distractor_features])
        outputDf_labels = pd.concat([outputDf_target_labels, outputDf_distractor_labels])

        train_features_folder_path = os.path.join(output_files, featuresAndModel_folder_name)
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
        # # fixing file to be only numbers
        # full_X = pd.read_csv(model_exp_path + train_features_file_name)
        # full_X = full_X.iloc[:, 1:]
        # full_X.to_csv(model_exp_path + train_features_file_name, index=False)
        # X = np.loadtxt(model_exp_path + train_features_file_name, delimiter=',')
        # y = np.loadtxt(model_exp_path + label_file_name, delimiter=',')



        X = outputDf_features
        y = outputDf_labels

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
        print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
        print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
        # print("Report:", classification_report(y_test, y_pred))

        model = LinearSVC()
        model.fit(X, y)
        # save the SVCModel
        SVC_Model_filename = SVC_dir_path + f'finalized_SVC_Model_{date}.sav'
        pickle.dump(model, open(SVC_Model_filename, 'wb'))

        # Random Forest
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        print("Random Forest model")

        # Prediction
        y_pred = model.predict(X_test)
        print("Random Forest Predicted values:")
        # print(y_pred)

        # Prediction Factors
        print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
        print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
        # print("Report:", classification_report(y_test, y_pred))

        model = RandomForestClassifier()
        model.fit(X, y)

        # save the RandomForest model
        RandomForest_filename = RandomForest_dir_path + f'finalized_RandomForest_Model_{date}.sav'
        pickle.dump(model, open(RandomForest_filename, 'wb'))
    
    if modes[mode] == "TEST":
        # load models
        root = tk.Tk()
        root.withdraw()
        test_model_path = filedialog.askopenfilename() # filedialog.askopenfilename("Choose model")
        test_model = pickle.load(open(test_model_path, 'rb'))
        # load test features
        root = tk.Tk()
        root.withdraw()
        test_features_path = filedialog.askopenfilename() #filedialog.askopenfilename("Choose features")
        # cut to feed the model
        testFeatureMatrixRAW = pd.read_csv(test_features_path)
        num_columns = len(testFeatureMatrixRAW.columns)
        # testFeatureMatrix = pd.read_csv(test_features_path, header=None, usecols=range(1, num_columns), skiprows=1)
        y_pred = test_model.predict(testFeatureMatrixRAW)
        print("Predicted values:")
        print(y_pred)
        print("\n\n")
        exp_path = output_files + "testSet/test_21_05_2023 at 02_47_41_PM/"
        condition1_features = pd.read_csv(exp_path + "target_test_features_Matrix.csv", header=None)
        condition1_num_of_trials = condition1_features.shape[0]
        vote(y_pred, condition1_num_of_trials, exp_path)
        # print("Accuracy:", accuracy_score(test_set_labels, y_pred) * 100)

if __name__ == '__main__':
    main()
