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
from parameters import *



def main(exp_path):
    # load "featuresMatrix.csv" and "labels.csv"
    # X = pd.read_csv(exp_path + "featuresMatrix.csv")
    X = np.loadtxt(exp_path + feature_folder_path + feature_file_name, delimiter=',')
    y = np.loadtxt(exp_path + feature_folder_path + label_file_name, delimiter=',')

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
    currModelPath = exp_path + model_folder_path
    os.makedirs(currModelPath, exist_ok=True)
    # save the SVCModel
    SVC_Model_filename = currModelPath + 'finalized_SVC_Model.sav'
    pickle.dump(model, open(SVC_Model_filename, 'wb'))

    # Prediction
    y_pred = model.predict(X_test)
    print("LinearSVC Predicted values:")
    # print(y_pred)
    #
    # Prediction Factors
    # print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
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
    # print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
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
    # print("Confusion_Matrix:", confusion_matrix(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred) * 100)
    # print("Report:", classification_report(y_test, y_pred))

    # save the RandomForest model
    RandomForest_filename = currModelPath + 'finalized_RandomForest_Model.sav'
    pickle.dump(model, open(RandomForest_filename, 'wb'))


if __name__ == '__main__':
    main()
