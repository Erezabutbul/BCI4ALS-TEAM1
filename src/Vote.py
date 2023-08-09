# import numpy as np
# import pandas as pd
from parameters import *



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
    voting_proba_TARGET_results = list()
    voting_proba_DISTRACTOR_results = list()
    voting_results_vec = list()
    num_of_electrodes = len(selected_channels)
    for i in range(firstTrial, lastTrial, num_of_electrodes):
        subarray = test_predicted[i:i + num_of_electrodes]  # Get a subarray of num_of_electrodes elements
        trial_target_proba = 0
        trial_distractor_proba = 0

        # calculate the AVG proba decision of all the selected electrodes for each condition
        for j in range(num_of_electrodes):
            trial_target_proba += subarray[j][0]
        trial_target_proba = trial_target_proba / num_of_electrodes

        for j in range(num_of_electrodes):
            trial_distractor_proba += subarray[j][1]
        trial_distractor_proba = trial_distractor_proba / num_of_electrodes

        # logic in order to make the decision
        # TODO - take into consideration different sizes, and bias for distractor
        if trial_target_proba - trial_distractor_proba > 0.02 and trial_target_proba > trial_distractor_proba: #and trial_target_proba > 0.51:
        # if trial_target_proba > trial_distractor_proba: #and trial_target_proba > 0.51:
            voting_proba_TARGET_results.append(trial_target_proba)
            voting_results_vec.append(1)
        elif trial_distractor_proba - trial_target_proba > 0.02 and trial_distractor_proba > trial_target_proba:
            voting_proba_DISTRACTOR_results.append(trial_distractor_proba)
            voting_results_vec.append(0)
        # elif trial_distractor_proba - trial_target_proba > 0.03 and trial_distractor_proba > trial_target_proba: #and trial_distractor_proba > 0.55:
            # voting_proba_results.append(trial_distractor_proba)
            # voting_results_vec.append(0)

    # precentageTOBETarget = sum(voting_results_vec) / len(voting_results_vec)
    precentageTOBETarget =None

    # return voting_proba_results, voting_results_vec, precentageTOBETarget
    return voting_proba_TARGET_results, voting_proba_DISTRACTOR_results, voting_results_vec, precentageTOBETarget


def calculate_average_percentage(voting_result):
    if len(voting_result) == 0:
        return 0
    else:
        return sum(voting_result) / len(voting_result)

# 2 modes - "REAL TEST": when making live prediction
#           "None mode": when using vote for cross validation purpose
def main(prediction, endOfCondition1, exp_path=None, state=None):

    # condition_1_voting_proba_result, condition_1_voting_results_vec, precentageTOBETarget_condition1 = probaVote(0, endOfCondition1, prediction)  # correlates to target
    # condition_2_voting_proba_result, condition_2_voting_results_vec, precentageTOBETarget_condition2 = probaVote(endOfCondition1, len(prediction), prediction)  # correlates to distractor
    condition_1_voting_TARGET_proba_result, condition_1_voting_DISTRACTOR_proba_result, condition_1_voting_results_vec, precentageTOBETarget_condition1 = probaVote(0, endOfCondition1, prediction)  # correlates to target
    condition_2_voting_TARGET_proba_result, condition_2_voting_DISTRACTOR_proba_result, condition_2_voting_results_vec, precentageTOBETarget_condition2 = probaVote(endOfCondition1, len(prediction), prediction)  # correlates to distractor


    # condition_1_AVG_proba_precentage = sum(condition_1_voting_proba_result) / len(condition_1_voting_proba_result)
    # condition_2_AVG_proba_precentage = sum(condition_2_voting_proba_result) / len(condition_2_voting_proba_result)

    print("condition_1_voting_TARGET_proba_result", condition_1_voting_TARGET_proba_result)
    print("condition_1_voting_DISTRACTOR_proba_result", condition_1_voting_DISTRACTOR_proba_result)
    print("condition_2_voting_TARGET_proba_result", condition_2_voting_TARGET_proba_result)
    print("condition_2_voting_DISTRACTOR_proba_result", condition_2_voting_DISTRACTOR_proba_result)

    condition_1_AVG_TARGET_proba_precentage = calculate_average_percentage(condition_1_voting_TARGET_proba_result)
    condition_2_AVG_TARGET_proba_precentage = calculate_average_percentage(condition_2_voting_TARGET_proba_result)
    condition_1_AVG_DISTRACTOR_proba_precentage = calculate_average_percentage(condition_1_voting_DISTRACTOR_proba_result)
    condition_2_AVG_DISTRACTOR_proba_precentage = calculate_average_percentage(condition_2_voting_DISTRACTOR_proba_result)

    print("condition_1_AVG_TARGET_proba_precentage", condition_1_AVG_TARGET_proba_precentage)
    print("condition_1_AVG_DISTRACTOR_proba_precentage", condition_1_AVG_DISTRACTOR_proba_precentage)
    print("condition_2_AVG_TARGET_proba_precentage", condition_2_AVG_TARGET_proba_precentage)
    print("condition_2_AVG_DISTRACTOR_proba_precentage", condition_2_AVG_DISTRACTOR_proba_precentage)

    condition_1_AVG_proba_precentage = condition_1_AVG_TARGET_proba_precentage - condition_1_AVG_DISTRACTOR_proba_precentage
    condition_2_AVG_proba_precentage = condition_2_AVG_TARGET_proba_precentage - condition_2_AVG_DISTRACTOR_proba_precentage
    return condition_1_AVG_TARGET_proba_precentage, condition_2_AVG_TARGET_proba_precentage, condition_1_voting_results_vec, condition_2_voting_results_vec



    # if state is not None:
    #     file = open(exp_path + "/pics_allocation.txt", "r")
    #     lines_list = file.readlines()
    #     # TODO - sanity check with nadav
    #     cond2num = {1: lines_list[1], 0: lines_list[3]}
    #     print("The selected is: ")
    #     if condition_1_AVG_proba_precentage > condition_2_AVG_proba_precentage:
    #         print("prediction is ", cond2num[1])
    #         print("which means: YES")
    #         print("precentage of confidence: ", condition_1_AVG_proba_precentage)
    #     elif condition_1_AVG_proba_precentage < condition_2_AVG_proba_precentage:
    #         print("prediction is ", cond2num[0])
    #         print("which means: NO")
    #         print("precentage of confidence: ", condition_2_AVG_proba_precentage)
    #
    # else:
    #     return condition_1_AVG_proba_precentage, condition_2_AVG_proba_precentage, condition_1_voting_results_vec, condition_2_voting_results_vec




if __name__=='__main__':
    main()



