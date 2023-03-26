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

def main():
    if modes[mode] == "TRAIN":
        #make SVC and RANDOM FOREST directories if doesn't exist

        SVC_dir_path = output_files + featuresAndModel_folder_name + train_model_folder_name + "SVC/"
        RandomForest_dir_path = output_files + featuresAndModel_folder_name + train_model_folder_name + "RandomForest/"

        os.makedirs(SVC_dir_path, exist_ok=True)
        os.makedirs(RandomForest_dir_path, exist_ok=True)


        # load "featuresMatrix.csv" and "labels.csv"
        model_exp_path = output_files + featuresAndModel_folder_name
        X = np.loadtxt(model_exp_path + train_features_file_name, delimiter=',')
        y = np.loadtxt(model_exp_path + label_file_name, delimiter=',')

        # separate to training and learning sets: X is the data by feature, y is the class vector(target, distractor, baseline)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

        # SVC (sklearn Support Vector Classification)
        model = LinearSVC()
        model.fit(X, y)
        print("SVC model")

        # save the SVCModel
        SVC_Model_filename = SVC_dir_path + f'finalized_SVC_Model_{date}.sav'
        pickle.dump(model, open(SVC_Model_filename, 'wb'))

        # Prediction
        y_pred = model.predict(X_test)
        print("LinearSVC Predicted values:")
        # print(y_pred)
        #
        # Prediction Factors
        print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
        print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
        # print("Report:", classification_report(y_test, y_pred))

        # Random Forest
        model = RandomForestClassifier()
        model.fit(X, y)
        print("Random Forest model")

        # Prediction
        y_pred = model.predict(X_test)
        print("Random Forest Predicted values:")
        # print(y_pred)

        # Prediction Factors
        print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
        print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
        # print("Report:", classification_report(y_test, y_pred))

        # save the RandomForest model
        RandomForest_filename = RandomForest_dir_path + f'finalized_RandomForest_Model_{date}.sav'
        pickle.dump(model, open(RandomForest_filename, 'wb'))
    
    if modes[mode]=="TEST":
        # load models
        root = tk.Tk()
        root.withdraw()
        test_model_path = filedialog.askopenfilename()
        test_model = pickle.load(open(test_model_path, 'rb'))
        # load test features
        root = tk.Tk()
        root.withdraw()
        test_features_path = filedialog.askopenfilename()
        # cut to feed the model
        testFeatureMatrixRAW = pd.read_csv(test_features_path)
        num_columns = len(testFeatureMatrixRAW.columns)
        testFeatureMatrix = pd.read_csv(test_features_path, header=None, usecols=range(1, num_columns), skiprows=1)
        y_pred = test_model.predict(testFeatureMatrix)
        print("Predicted values:")
        print(y_pred)
        print("\n\n")
        vote(y_pred)
        # print("Accuracy:", accuracy_score(test_set_labels, y_pred) * 100)

if __name__ == '__main__':
    main()
