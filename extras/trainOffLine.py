# Importing the required packages
from datetime import datetime

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
# from parameters import *
import os

def main():
    # date & time
    date = datetime.now().strftime("%d_%m_%Y at %I_%M_%S_%p")
    # make SVC and RANDOM FOREST directories if doesn't exist
    SVC_dir_path = "../src/output_files/" + "featuresAndModel/" + "models/" + "SVC/"
    RandomForest_dir_path = "../src/output_files/" + "featuresAndModel/" + "models/" + "RandomForest/"
    os.makedirs(SVC_dir_path, exist_ok=True)
    os.makedirs(RandomForest_dir_path, exist_ok=True)

    # load "featuresMatrix.csv" and "labels.csv"
    model_exp_path = "../src/output_files/" + "featuresAndModel/"
    X = np.loadtxt(model_exp_path + "/features/" + "features_matrix.csv", delimiter=',')
    y = np.loadtxt(model_exp_path + "/features/" + "labels_vector_test.csv", delimiter=',')

    # print("number of rows of y " + str(y.shape))
    # print("number of rows of X " + str(X.shape[0]))
    # print("number of cols of X " + str(X.shape[1]))
    # separate to training and learning sets: X is the data by feature, y is the class vector(target, distractor, baseline)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

    # SVC (sklearn Support Vector Classification)
    model = LinearSVC()
    model.fit(X_train, y_train)
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
    print("Report:", classification_report(y_test, y_pred))


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
    print("Report:", classification_report(y_test, y_pred))

    # save the RandomForest model
    RandomForest_filename = RandomForest_dir_path + f'finalized_RandomForest_Model_{date}.sav'
    pickle.dump(model, open(RandomForest_filename, 'wb'))

if __name__ == '__main__':
    main()