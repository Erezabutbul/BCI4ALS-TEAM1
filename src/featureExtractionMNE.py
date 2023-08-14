import pandas as pd

from parameters import *
import numpy as np
import mne

"""
featureExtraction.py - Feature extraction from EEG data using MNE.

This script defines functions for extracting features from EEG data using MNE. It includes functions for reshaping trials,
extracting positivity feature, Cz sum feature, power sum feature, and the main feature extraction process.

"""


def trialFlowFearture(epochs_data, epochs_shape):
    """
    Reshape the epochs data to a trial flow feature matrix.

    Args:
        epochs_data (numpy.ndarray): EEG data from epochs.
        epochs_shape (tuple): Shape of the epochs data.

    Returns:
        numpy.ndarray: Trial flow feature matrix.

    """
    trialFlowFeatureMatrix = epochs_data.reshape([epochs_shape[0] * epochs_shape[1], epochs_shape[2]])
    return trialFlowFeatureMatrix

def positivityFeature():
    # need to consider a way to add it externally to the model
    """
    AVG_TARGET = epochs["target"].average()
    AVG_DISTRACTOR = epochs["distractor"].average()
    diff = mne.combine_evoked((AVG_TARGET,-AVG_DISTRACTOR), weights='equal')
    subStactionFeature = diff.get_data(tmin=0.335, tmax=0.40)
    feature = np.sum(subStactionFeature)
    if feature > 0
    :return: TARGET
    """
    return

def CzSumFeature(epochs_object, shape_of_matrix_to_resize):
    """
    Calculate Cz sum feature.

    Args:
        epochs_object (mne.Epochs): Epochs object containing EEG data.
        shape_of_matrix_to_resize (int): Shape of the matrix to resize.

    Returns:
        numpy.ndarray: Resized Cz sum feature vector.

    """
    Cz_data = epochs_object.get_data(tmin=0.30, tmax=0.39, picks=epochs_object.ch_names.index("Cz"))
    Cz_sum = np.sum(Cz_data)
    Cz_sum_resizes = np.array([Cz_sum] * shape_of_matrix_to_resize)
    Cz_sum_resizes = Cz_sum_resizes.reshape([Cz_sum_resizes.shape[0], 1])
    return Cz_sum_resizes

def powerSum(epochs_object, shape_of_matrix_to_resize):
    """
    Calculate power sum feature.

    Args:
        epochs_object (mne.Epochs): Epochs object containing EEG data.
        shape_of_matrix_to_resize (int): Shape of the matrix to resize.

    Returns:
        numpy.ndarray: Resized power sum feature vector.

    """
    elec_data = epochs_object.get_data(tmin=0.30, tmax=0.39, picks=selected_channels)
    sum_elec_data = np.sum(elec_data, axis=2)
    elec_sum_resizes = np.reshape(sum_elec_data, [sum_elec_data.shape[0]*sum_elec_data.shape[1],1])

    return elec_sum_resizes

def extractFeatures(epochs_object, epochs_data):
    """
    Extract features from EEG data.

    Args:
        epochs_object (mne.Epochs): Epochs object containing EEG data.
        epochs_data (numpy.ndarray): EEG data from epochs.

    Returns:
        numpy.ndarray: Final feature matrix.

    """
    epochs_shape = epochs_data.shape
    # Flow feature
    trialFlowFeatureMatrix = trialFlowFearture(epochs_data, epochs_shape)
    # Cz sum feature
    # Cz_sum_vector = CzSumFeature(epochs_object, trialFlowFeatureMatrix.shape[0])
    #
    # total sum feature
    total_sum_vector = powerSum(epochs_object, trialFlowFeatureMatrix.shape[0])

    # final_feature_matrix = np.concatenate([trialFlowFeatureMatrix, Cz_sum_vector], axis=1)
    final_feature_matrix = np.concatenate([trialFlowFeatureMatrix, total_sum_vector], axis=1)

    # return trialFlowFeatureMatrix
    return final_feature_matrix


def main(exp_path, state="TRAIN", target_epochs=None, distractor_epochs=None):
    """
    Main function for feature extraction.

    Args:
        exp_path (str): Path to the experiment directory.
        state (str): Mode of operation, "TRAIN" or other.
        target_epochs (mne.Epochs): Epochs object containing target EEG data.
        distractor_epochs (mne.Epochs): Epochs object containing distractor EEG data.

    Returns:
        None: Feature extraction results are saved to files.

    """
    if target_epochs is None and distractor_epochs is None:
        target_epochs = mne.read_epochs(exp_path + filtered_EEG_folder_path + "target_epochs.fif")
        distractor_epochs = mne.read_epochs(exp_path + filtered_EEG_folder_path + "distractor_epochs.fif")

    if state == "TRAIN":
        print("train")
        targetData = target_epochs.get_data(picks=selected_channels)
        distractorData = distractor_epochs.get_data(picks=selected_channels)

        target_features = extractFeatures(target_epochs, targetData)
        distractor_features = extractFeatures(distractor_epochs, distractorData)

        # create labels vector
        num_target = target_features.shape[0]
        num_distractor = distractor_features.shape[0]
        # labels_vec = np.concatenate((np.ones(num_target, dtype=int), np.zeros(num_distractor, dtype=int)))
        target_labels = np.ones(num_target, dtype=int)
        distractor_labels = np.zeros(num_distractor, dtype=int)

        # save features matrix for all EXP available
        train_features_folder_path = exp_path
        # np.savetxt(train_features_folder_path + label_file_name, labels_vec, delimiter=",")
        np.savetxt(train_features_folder_path + target_label_file_name, target_labels, delimiter=",")
        np.savetxt(train_features_folder_path + distractor_label_file_name, distractor_labels, delimiter=",")

        # can add mne features for fun

        targetDF = pd.DataFrame(target_features)
        distractorDF = pd.DataFrame(distractor_features)
        # finalFeatureMatrix = pd.concat([targetDF, distractorDF])
        # finalFeatureMatrix.to_csv(train_features_folder_path + train_features_file_name, header=False, index=False)
        targetDF.to_csv(train_features_folder_path + target_train_features_file_name, header=False, index=False)
        distractorDF.to_csv(train_features_folder_path + distractor_train_features_file_name, header=False, index=False)

    # test condition
    else:
        print("test")
        targetData = target_epochs.get_data(picks=selected_channels)
        distractorData = distractor_epochs.get_data(picks=selected_channels)

        condition1Arr = extractFeatures(target_epochs, targetData)
        condition2Arr = extractFeatures(distractor_epochs, distractorData)

        condition1DF = pd.DataFrame(condition1Arr)
        condition2DF = pd.DataFrame(condition2Arr)

        condition1DF.to_csv(exp_path + "/" + target_test_features_file_name, header=False, index=False)
        condition2DF.to_csv(exp_path + "/" + distractor_test_features_file_name, header=False, index=False)

        finalTestFeatureMatrix = pd.concat([condition1DF, condition2DF])
        finalTestFeatureMatrix.to_csv(exp_path + "/" + test_features_file_name, index=False)


if __name__ == '__main__':
    main()
