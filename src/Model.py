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

def main(exp_path,date):
    if modes[mode] == "TRAIN":
        #make SVC and RANDOM FOREST directories if doesn't exist
        SVC_dir_path = "output_files/" + "featuresAndModel/" + "models/" + "SVC/"
        RandomForest_dir_path = "output_files/" + "featuresAndModel/" + "models/" + "RandomForest/"
        os.makedirs(SVC_dir_path, exist_ok=True)
        os.makedirs(RandomForest_dir_path, exist_ok=True)


        # load "featuresMatrix.csv" and "labels.csv"
        model_exp_path = "output_files/" + "featuresAndModel/"
        X = np.loadtxt(model_exp_path + feature_folder_path + feature_file_name, delimiter=',')
        y = np.loadtxt(model_exp_path + feature_folder_path + label_file_name, delimiter=',')

        # print("number of rows of y " + str(y.shape))
        # print("number of rows of X " + str(X.shape[0]))
        # print("number of cols of X " + str(X.shape[1]))
        # separate to training and learning sets: X is the data by feature, y is the class vector(target, distractor, baseline)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

        # SVC (sklearn Support Vector Classification)
        model = LinearSVC()
        model.fit(X, y)
        print("SVC model")

        # Create the "EXP_{date}" directory
        currModelPath = model_exp_path + model_folder_path
        # os.makedirs(currModelPath, exist_ok=True)
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



        # # Decision Tree
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        print("Decision Tree model")
        #
        # # Prediction
        # y_pred = model.predict(X_test)
        # print("Predicted values:")
        # print(y_pred)
        #
        # # Prediction Factors
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

        test_features_path = exp_path + feature_folder_path

        testFeatureMatrix = pd.read_csv(test_features_path + feature_of_test_file_name, header=None)
        y_pred = test_model.predict(testFeatureMatrix)
        print("Predicted values:")
        print(y_pred)
        print("\n\n")
        # print("Accuracy:", accuracy_score(test_set_labels, y_pred) * 100)






        ######################################## PREVIOUS LIVE MODEL

        # liveModle_exp_path = exp_path + "/featuresAndModel/"
        # currModelPath = liveModle_exp_path + feature_folder_path + model_folder_path
        # SVC_Model_filename = currModelPath + 'finalized_SVC_Model.sav'
        # SVC_model = pickle.load(open(SVC_Model_filename, 'rb'))
        # # labels_path = "output_files/featuresAndModel/features/"
        # # test_set_labels = np.loadtxt(labels_path + "test_labels.csv", delimiter=',')

        # # SVC Prediction
        # testFeatureMatrix = pd.read_csv(liveModle_exp_path + feature_folder_path + feature_of_test_file_name, header=None)
        # y_SVC_pred = SVC_model.predict(testFeatureMatrix)
        # print("Predicted values:")
        # print(y_SVC_pred)
        # print("\n\n")
        # # print("Accuracy:", accuracy_score(test_set_labels, y_SVC_pred) * 100)
        # print("RandomForest")
        # print("\n\n")


        # # save the RandomForest model
        # RandomForest_filename = currModelPath + 'finalized_RandomForest_Model.sav'
        # RandomForest_model = pickle.load(open(RandomForest_filename, 'rb'))

        # # RandomForest Prediction
        # y_RandomForest_pred = RandomForest_model.predict(testFeatureMatrix)
        # print("Predicted values:")
        # print(y_RandomForest_pred)
        # print("\n\n")
        # # print("Accuracy:", accuracy_score(test_set_labels, y_RandomForest_pred) * 100)










# def main(exp_path):
#     # load "featuresMatrix.csv" and "labels.csv"
#     model_exp_path = exp_path + "/featuresAndModel/"
#     X = np.loadtxt(model_exp_path + feature_folder_path + feature_file_name, delimiter=',')
#     y = np.loadtxt(model_exp_path + feature_folder_path + label_file_name, delimiter=',')

#     # print("number of rows of y " + str(y.shape))
#     # print("number of rows of X " + str(X.shape[0]))
#     # print("number of cols of X " + str(X.shape[1]))
#     # separate to training and learning sets: X is the data by feature, y is the class vector(target, distractor, baseline)
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

#     # SVC (sklearn Support Vector Classification)
#     model = LinearSVC()
#     model.fit(X, y)
#     print("SVC model")

#     # Create the "EXP_{date}" directory
#     currModelPath = model_exp_path + model_folder_path
#     os.makedirs(currModelPath, exist_ok=True)
#     # save the SVCModel
#     SVC_Model_filename = currModelPath + 'finalized_SVC_Model.sav'
#     pickle.dump(model, open(SVC_Model_filename, 'wb'))

#     # Prediction
#     y_pred = model.predict(X_test)
#     print("LinearSVC Predicted values:")
#     # print(y_pred)
#     #
#     # Prediction Factors
#     print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
#     print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
#     # print("Report:", classification_report(y_test, y_pred))



#     # # Decision Tree
#     model = DecisionTreeClassifier()
#     model.fit(X_train, y_train)
#     print("Decision Tree model")
#     #
#     # # Prediction
#     # y_pred = model.predict(X_test)
#     # print("Predicted values:")
#     # print(y_pred)
#     #
#     # # Prediction Factors
#     print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
#     print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
#     # print("Report:", classification_report(y_test, y_pred))

#     # Random Forest
#     model = RandomForestClassifier()
#     model.fit(X, y)
#     print("Random Forest model")

#     # Prediction
#     y_pred = model.predict(X_test)
#     print("Random Forest Predicted values:")
#     # print(y_pred)

#     # Prediction Factors
#     print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
#     print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
#     # print("Report:", classification_report(y_test, y_pred))

#     # save the RandomForest model
#     RandomForest_filename = currModelPath + 'finalized_RandomForest_Model.sav'
#     pickle.dump(model, open(RandomForest_filename, 'wb'))


if __name__ == '__main__':
    main()
