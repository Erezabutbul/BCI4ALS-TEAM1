from parameters import *
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from featureExtractionMNE import main as extractFeatures
from Vote import main as Vote
from scipy.stats import zscore
import mne

"""
cross_validation.py - Perform cross-validation and testing using a trained classifier.

This script performs cross-validation and testing using a trained classifier on EEG data from different
experiment folders. It trains a classifier on one set of folders and tests on another, reporting the results.

"""

def getEXPFoldersList(main_folder):
    """
    Get a list of experiment folders from a main directory.

    Args:
        main_folder (str): Path to the main directory.

    Returns:
        list: List of experiment folder names.

    """
    # get all the experiment folders
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('EXP')]
    return exp_folders


def train_model_crossValidation(train_set_path):
    """
    Train a classifier using cross-validation.

    Args:
        train_set_path (str or list): Path to the training set experiment folders.

    Returns:
        RandomForestClassifier: Trained classifier model.

    """
    outputDf_features, outputDf_labels, endOfcon1 = concatFeatures(train_set_path)
    model = RandomForestClassifier()
    model.fit(outputDf_features.values, outputDf_labels.values.ravel())
    return model

def test_set_crossValidation(test_set_path):
    """
    Prepare the testing set for cross-validation.

    Args:
        test_set_path (str): Path to the testing set experiment folder.

    Returns:
        ndarray, ndarray, int: Feature matrix, true labels, and index representing the end of condition 1.

    """
    outputDf_features, outputDf_labels, endOfcon1 = concatFeatures(test_set_path)
    return outputDf_features.values, outputDf_labels.values, endOfcon1


def concatFeatures(condition_set_path):
    """
    Concatenate features and labels from different experiment folders.

    Args:
        condition_set_path (str or list): Path to the experiment folders.

    Returns:
        DataFrame, DataFrame, int: Concatenated features, concatenated labels, and index representing the end of condition 1.

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



def positivityFeature(path_to_exp):
    """
    Calculate and return the positivity feature based on EEG data.

    Args:
        path_to_exp (str): Path to the experiment folder.

    Returns:
        str, float: Winner (con1 or con2) and added chance.

    """
    path_to_exp += "/"
    # need to consider a way to add it externally to the model
    con1_epochs = mne.read_epochs(path_to_exp + filtered_EEG_folder_path + "target_epochs.fif")
    con2_epochs = mne.read_epochs(path_to_exp + filtered_EEG_folder_path + "distractor_epochs.fif")

    AVG_con1 = con1_epochs.average()
    AVG_con2 = con2_epochs.average()
    diff = mne.combine_evoked((AVG_con1,-AVG_con2), weights='equal')
    subStactionFeature = diff.get_data(tmin=0.335, tmax=0.40)
    feature = np.sum(subStactionFeature)

    if feature > 0:
        # con1 is the target
        winner = "con1"# return the precentage that you want to add

    else:
        winner = "con2"# return the precentage that you want to add
    # con2 is the target

    return winner, 0.01


def main():
    """
    Main function for performing cross-validation and testing.

    Returns:
        None: Displays prediction results and accuracy.

    """
    listOfCorrect = list()

    allFolder = getEXPFoldersList(output_files)

    for folder in allFolder:
        extractFeatures(output_files + folder+"/")

    for i, file_to_exclude in enumerate(allFolder):
        print("Iteration:", i)
        files_to_train = allFolder[:i] + allFolder[i + 1:]
        print("Files to train:", files_to_train)
        print("test file:", file_to_exclude)

        # train model
        model = train_model_crossValidation(files_to_train)
        # extract feature from the test set
        test_feature_matrix, test_true_labels_before_vote, endOfcon1TEST = test_set_crossValidation(file_to_exclude)

        winner, added_chance = positivityFeature(output_files + file_to_exclude)

        # predict using the trained model
        test_predicted_labels_before_vote = model.predict_proba(test_feature_matrix)

        # get the voting result
        # target_voting_result = Vote(0, endOfcon1TEST, test_predicted_labels_before_vote) # correlates to target
        # distractor_voting_result = Vote(endOfcon1TEST, len(test_predicted_labels_before_vote), test_predicted_labels_before_vote) # correlates to distractor
        print("----------------------------------------- New Fold -----------------------------------------")
        target_AVG_voting_result, distractor_AVG_voting_result, target_voting_results_vec, distractor_voting_results_vec = Vote(test_predicted_labels_before_vote, endOfcon1TEST)


        print("The general list of prediction per trial is: ", target_voting_results_vec, "", distractor_voting_results_vec)
        print("target proba ", target_AVG_voting_result)
        print("distractor proba", distractor_AVG_voting_result)

        if winner == "con1":
            target_AVG_voting_result += added_chance
        else:
            distractor_AVG_voting_result += added_chance

        #################### proba vote ##################################
        # if target_proba_precentage - distractor_proba_precentage > 0.005:
        print("The selected is: ")
        if target_AVG_voting_result > distractor_AVG_voting_result:
            print("prediction is 1 ")
            print("which means: YES")
            print("precentage of confidence: ", target_AVG_voting_result)
            listOfCorrect.append(1)
        elif target_AVG_voting_result < distractor_AVG_voting_result:
            print("prediction is 0 ")
            print("which means: NO")
            print("precentage of confidence: ", distractor_AVG_voting_result)
        # else:
        #     # decide by AVG
        #     print("deciding by avg param")




        ################################# regular vote #######################################
        # each one of the idexes is trial
        # print("The selected is: ")
        # if precentage_of_con1 > precentage_of_con2:
        #     print("prediction is 1 ")
        #     print("which means: YES")
        #     print("precentage of confidence: " + str(precentage_of_con1))
        #     listOfCorrect.append(1)
        # elif precentage_of_con1 < precentage_of_con2:
        #     print("prediction is 0 ")
        #     print("which means: NO")
        #     print("precentage of confidence: " + str(precentage_of_con2))
        #
        # else:
        #     print("It's a TIE")


        # print("Accuracy:", accuracy_score(test_true_labels, test_predicted_labels) * 100)


        # accuracy my nadavs team
        # accuracy = (precentage_of_con1 * len(target_voting_result) + (1 - precentage_of_con2)
        #             * len(distractor_voting_result)) / (len(target_voting_result) + len(distractor_voting_result))
        #
        # print("\nAccuracy is: " + str(accuracy))
        # print("chance of first con of being the target: " + str(precentage_of_con1))
        # print("num of con1 trials: " + str(len(target_voting_result)))
        # print("chance of second con of being the target: " + str(precentage_of_con2))
        # # print("chance of second con of being the distractor: " + str(1 - precentage_of_con2))
        # print("num of con2 trials: " + str(len(distractor_voting_result)))
        #
        # total_accuracy += accuracy

    # print("\n\ntotal accuracy", total_accuracy / k)
    print("\nwins", sum(listOfCorrect), "out of", len(allFolder))


if __name__ == '__main__':
    main()
