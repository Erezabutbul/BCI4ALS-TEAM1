# import numpy as np
# import pandas as pd
from parameters import *






# def getPredictionPrecentage(firstTrial, lastTrial, prediction):
#     voting_zeros = list()  # Initialize an empty list to store voting results
#     voting_ones = list()  # Initialize an empty list to store voting results
#     voting_results = list()
#     num_of_electrodes = len(selected_channels)
#     for i in range(firstTrial, lastTrial, num_of_electrodes):
#         subarray = prediction[i:i + num_of_electrodes]  # Get a subarray of num_of_electrodes elements
#         total = np.sum(subarray)
#         if total > num_of_electrodes // 2:
#             voting_ones.append(1)
#             voting_results.append(1)
#         else:
#             voting_zeros.append(1)
#             voting_results.append(0)
#
#     winner = -1
#     if len(voting_ones) > len(voting_zeros):
#         total = np.sum(voting_ones)
#         winner = 1
#     else:
#         total = np.sum(voting_zeros)
#         winner = 0
#
#     return float((total / ((lastTrial - firstTrial))) * 100), voting_results ,winner



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



def main(prediction, endOfCondition1, exp_path):

    file = open(exp_path + "/pics_allocation.txt", "r")
    lines_list = file.readlines()
    # TODO - find the number of first condition
    condition_1_voting_result = probaVote(0, endOfCondition1, prediction) # correlates to target
    condition_2_voting_result = probaVote(endOfCondition1, len(prediction), prediction) # correlates to distractor

    cond2num = {1: lines_list[1], 0: lines_list[3]}

    print("The general list of prediction per trial is: " + str(condition_1_voting_result) + str(condition_2_voting_result))
    condition_1_proba_precentage = sum(condition_1_voting_result) / len(condition_1_voting_result)
    condition_2_proba_precentage = sum(condition_2_voting_result) / len(condition_2_voting_result)

    print("The selected is: ")
    if condition_1_proba_precentage > condition_2_proba_precentage:
        print("prediction is ", cond2num[1])
        print("which means: YES")
        print("precentage of confidence: ", condition_1_proba_precentage)
    elif condition_1_proba_precentage < condition_2_proba_precentage:
        print("prediction is ", cond2num[0])
        print("which means: NO")
        print("precentage of confidence: ", condition_2_proba_precentage)



    # print("\n\npercentage: ")
    # print(max(precentage_of_target, precentage_of_distractor))



if __name__=='__main__':
    main()



