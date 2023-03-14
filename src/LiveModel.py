# Importing the required packages
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
# from Model import svc, DecisionTree
# from DataByFeature import X
import pickle
import numpy as np
from parameters import *


def main(exp_path):
    # load models
    liveModle_exp_path = exp_path + "/featuresAndModel/"
    currModelPath = liveModle_exp_path + feature_folder_path + model_folder_path
    SVC_Model_filename = currModelPath + 'finalized_SVC_Model.sav'
    SVC_model = pickle.load(open(SVC_Model_filename, 'rb'))
    # labels_path = "output_files/featuresAndModel/features/"
    # test_set_labels = np.loadtxt(labels_path + "test_labels.csv", delimiter=',')

    # SVC Prediction
    testFeatureMatrix = pd.read_csv(liveModle_exp_path + feature_folder_path + feature_of_test_file_name, header=None)
    y_SVC_pred = SVC_model.predict(testFeatureMatrix)
    print("Predicted values:")
    print(y_SVC_pred)
    print("\n\n")
    # print("Accuracy:", accuracy_score(test_set_labels, y_SVC_pred) * 100)
    print("RandomForest")
    print("\n\n")


    # save the RandomForest model
    RandomForest_filename = currModelPath + 'finalized_RandomForest_Model.sav'
    RandomForest_model = pickle.load(open(RandomForest_filename, 'rb'))

    # RandomForest Prediction
    y_RandomForest_pred = RandomForest_model.predict(testFeatureMatrix)
    print("Predicted values:")
    print(y_RandomForest_pred)
    print("\n\n")
    # print("Accuracy:", accuracy_score(test_set_labels, y_RandomForest_pred) * 100)



if __name__ == '__main__':
    main()