from parameters import *
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from featureExtractionMNE import main as extractFeatures

def getPredictionPrecentage(firstTrial, lastTrial, prediction):
    voting_zeros = list()  # Initialize an empty list to store voting results
    voting_ones = list()  # Initialize an empty list to store voting results
    voting_results = list()
    num_of_electrodes = len(selected_channels)
    for i in range(firstTrial, lastTrial, num_of_electrodes):
        subarray = prediction[i:i + num_of_electrodes]  # Get a subarray of num_of_electrodes elements
        total = np.sum(subarray)
        if total > num_of_electrodes // 2:
            voting_ones.append(1)
            voting_results.append(1)
        else:
            voting_zeros.append(1)
            voting_results.append(0)

    winner = -1
    if len(voting_ones) > len(voting_zeros):
        total = np.sum(voting_ones)
        winner = 1
    else:
        total = np.sum(voting_zeros)
        winner = 0

    return float((total / ((lastTrial - firstTrial))) * 100), voting_results ,winner

def getEXPFoldersList(main_folder):
    # get all the experiment folders
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('EXP')]
    return exp_folders


# def generateRandomExpAndBlock():
#     expFoldersList = getEXPFoldersList(output_files)
#     # get random EXP
#     random_EXP_index = random.randrange(len(expFoldersList))
#     # print(expFoldersList[random_index])
#     test_set = expFoldersList[random_EXP_index]
#     expFoldersList.remove(expFoldersList[random_EXP_index])
#
#     # after removal of test set
#     train_set = expFoldersList
#     return train_set, test_set


def train_model_crossValidation(train_set_path):

    outputDf_features, outputDf_labels, endOfcon1 = concatFeatures(train_set_path)
    model = RandomForestClassifier()
    model.fit(outputDf_features.values, outputDf_labels.values.ravel())
    return model

def test_set_crossValidation(test_set_path):

    outputDf_features, outputDf_labels, endOfcon1 = concatFeatures(test_set_path)
    return outputDf_features.values, outputDf_labels.values, endOfcon1
#
# def test_set_crossValidation(test_set_path):
#     # the outputs that will be concatenated
#     outputDf_target_features = pd.DataFrame()
#     outputDf_distractor_features = pd.DataFrame()
#     outputDf_target_labels = pd.DataFrame()
#     outputDf_distractor_labels = pd.DataFrame()
#
#
#     currExpPath = output_files + test_set_path
#     currTargetFeatures = pd.read_csv(currExpPath + "/" + target_train_features_file_name, header=None)
#     currDistractorFeatures = pd.read_csv(currExpPath + "/" + distractor_train_features_file_name, header=None)
#     currTargetLabels = pd.read_csv(currExpPath + "/" + target_label_file_name, header=None)
#     currDistractorLabels = pd.read_csv(currExpPath + "/" + distractor_label_file_name, header=None)
#
#
#     outputDf_target_features = pd.concat([outputDf_target_features, currTargetFeatures])
#     outputDf_distractor_features = pd.concat([outputDf_distractor_features, currDistractorFeatures])
#     outputDf_target_labels = pd.concat([outputDf_target_labels, currTargetLabels], axis=0)
#     outputDf_distractor_labels = pd.concat([outputDf_distractor_labels, currDistractorLabels], axis=0)
#
#     endOfcon1 = outputDf_target_features.shape[0]
#
#     outputDf_features = pd.concat([outputDf_target_features, outputDf_distractor_features])
#     outputDf_labels = pd.concat([outputDf_target_labels, outputDf_distractor_labels])
#
#     return outputDf_features.values, outputDf_labels.values, endOfcon1



def voteONES(firstTrial, lastTrial, test_predicted):
    voting_zeros = list()  # Initialize an empty list to store voting results
    voting_ones = list()  # Initialize an empty list to store voting results
    voting_results = list()
    num_of_electrodes = len(selected_channels)
    for i in range(firstTrial, lastTrial, num_of_electrodes):
        subarray = test_predicted[i:i + num_of_electrodes]  # Get a subarray of num_of_electrodes elements
        total = np.sum(subarray)
        if total > num_of_electrodes // 2:
            voting_ones.append(1)
            voting_results.append(1)
        else:
            voting_zeros.append(1)
            voting_results.append(0)

    total = np.sum(voting_ones)

    return (total / ((lastTrial - firstTrial) / num_of_electrodes)), voting_results



def probaVote(firstTrial, lastTrial, test_predicted):
    voting_results = list()
    num_of_electrodes = len(selected_channels)
    for i in range(firstTrial, lastTrial, num_of_electrodes):
        subarray = test_predicted[i:i + num_of_electrodes]  # Get a subarray of num_of_electrodes elements
        trial_target_proba = 0
        for j in range(num_of_electrodes):
            trial_target_proba += subarray[j][0]
        trial_target_proba = trial_target_proba / num_of_electrodes
        voting_results.append(trial_target_proba)

    return voting_results





def concatFeatures(condition_set_path):
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












def main():

    # test_set_path = "EXP_21_05_2023 at 02_22_20_PM"
    # train_set_path = getEXPFoldersList(output_files)
    # train_set_path.remove(test_set_path)

    k = 0
    total_accuracy = 0
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

        # predict using the trained model
        test_predicted_labels_before_vote = model.predict_proba(test_feature_matrix)

        # get the voting result
        target_voting_result = probaVote(0, endOfcon1TEST, test_predicted_labels_before_vote) # correlates to target
        distractor_voting_result = probaVote(endOfcon1TEST, len(test_predicted_labels_before_vote), test_predicted_labels_before_vote) # correlates to distractor



        print("----------------------------------------- New Fold -----------------------------------------")
        print("The general list of prediction per trial is: " + str(target_voting_result) + str(distractor_voting_result))
        target_proba_precentage = sum(target_voting_result) / len(target_voting_result)
        distractor_proba_precentage = sum(distractor_voting_result) / len(distractor_voting_result)
        print("target proba sum", target_proba_precentage)
        print("distractor proba sum", distractor_proba_precentage)

        #################### proba vote ##################################
        # if target_proba_precentage - distractor_proba_precentage > 0.005:
        print("The selected is: ")
        if target_proba_precentage > distractor_proba_precentage:
            print("prediction is 1 ")
            print("which means: YES")
            print("precentage of confidence: ", target_proba_precentage)
            listOfCorrect.append(1)
        elif target_proba_precentage < distractor_proba_precentage:
            print("prediction is 0 ")
            print("which means: NO")
            print("precentage of confidence: ", distractor_proba_precentage)
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
