# import numpy as np
# import pandas as pd
from parameters import *






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




# def getPredictionPrecentage(firstTrial, lastTrial, prediction):
#     voting_results = []  # Initialize an empty list to store voting results
#     num_of_electrodes = len(selected_channels)
#     #*5 because each trial is 5 electrodes
#     startIndex = firstTrial*num_of_electrodes
#     EndIndex = lastTrial*num_of_electrodes-1
#     for i in range(startIndex, EndIndex, num_of_electrodes):
#         subarray = prediction[i:i + num_of_electrodes]  # Get a subarray of num_of_electrodes elements
#         total = np.sum(subarray)
#         if total > 2:
#             voting_results.append(1)
#         else:
#             voting_results.append(0)
#     totalOnes = np.sum(voting_results)
#     return (totalOnes / (lastTrial - firstTrial)) * 100

# Example input array
# arr = np.array([1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1])
# num_of_target_trials_path = "../src/output_files/" + "featuresAndModel/" + "features/"
# filename = 'num_tails_elecs_conditions.csv'
# df = pd.read_csv(num_of_target_trials_path+filename, header=None)
# endOfTarget = int(df.iloc[0, 0])
# def main():
def main(prediction, endOfCondition1, exp_path):
    # test_feature_folder_path = os.path.join(exp_path, test_features_folder_name)
    # df = pd.read_csv(test_feature_folder_path + num_trails_elecs_conditions_file_name, header=None)
    # endOfCondition1 = int(df.iloc[0, 0])
    # endOfCondition1 = endOfCondition1
    # prediction = np.array([0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1])
    file = open(exp_path + "/pics_allocation.txt", "r")
    lines_list = file.readlines()
    # TODO - find the number of first condition
    precentage_of_con1, target_voting_result, winner_con1 = getPredictionPrecentage(0, endOfCondition1, prediction) # correlates to target
    precentage_of_con2, distractor_voting_result, winner_con2 = getPredictionPrecentage(endOfCondition1, len(prediction), prediction) # correlates to distractor

    cond2num = {1 : lines_list[1], 0 : lines_list[3]}
    print("The general list of prediction per trial is: " + str(target_voting_result) + str(distractor_voting_result))
    # each one of the idexes is trial
    print("The selected is: ")
    if precentage_of_con1 > precentage_of_con2:
        print("prediction is  " + str(cond2num[winner_con1]))
        print("which means: YES")
        print("precentage: " + str(precentage_of_con1))
    elif precentage_of_con1 < precentage_of_con2:
        print("prediction is  " + str(cond2num[winner_con2]))
        print("which means: NO")
        print("precentage: " + str(precentage_of_con2))

    else:
        print("It's a TIE")

    # print("\n\npercentage: ")
    # print(max(precentage_of_target, precentage_of_distractor))



if __name__=='__main__':
    main()



