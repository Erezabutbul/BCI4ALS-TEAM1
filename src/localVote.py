# import numpy as np
# import pandas as pd
from parameters import *

def getPredictionPrecentage(firstTrial,lastTrial,arr):
    voting_results = []  # Initialize an empty list to store voting results
    for i in range(firstTrial, lastTrial+1, 5):
        subarray = arr[i:i + 5]  # Get a subarray of 5 elements
        total = np.sum(subarray)
        if total > 2:
            voting_results.append(1)
        else:
            voting_results.append(0)
    totalOnes = np.sum(voting_results)
    # print("TOTAL ONEs: " + str(totalOnes))
    totalTrials = (lastTrial - firstTrial)/len(selected_channels)
    # print("TOTAL trials: " + str(totalTrials))
    print("TOTAL ones over total: " + str(((totalOnes/totalTrials) * 100)))
    return (totalOnes / totalTrials) * 100

# Example input array
# arr = np.array([1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1])
# num_of_target_trials_path = "../src/output_files/" + "featuresAndModel/" + "features/"
# filename = 'num_tails_elecs_conditions.csv'
# df = pd.read_csv(num_of_target_trials_path+filename, header=None)
# endOfTarget = int(df.iloc[0, 0])
def main(y_pred,y_test, num_target):
    endOfCondition1 = num_target
    precentage_of_target_OF_LABEL = getPredictionPrecentage(0, endOfCondition1, y_test)
    precentage_of_distractor_OF_LABEL = getPredictionPrecentage(endOfCondition1, len(y_test), y_test)

    precentage_of_target_OF_TEST = getPredictionPrecentage(0, endOfCondition1, y_pred)
    precentage_of_distractor_OF_TEST = getPredictionPrecentage(endOfCondition1, len(y_pred), y_pred)
    winner = max(precentage_of_target_OF_TEST, 1- precentage_of_target_OF_TEST,precentage_of_distractor_OF_TEST, 1-precentage_of_distractor_OF_TEST)
    print(f"winner is " + str(winner))

    # if(precentage_of_target_OF_LABEL>precentage_of_distractor_OF_LABEL):
    #     print("TARGET IS THE LABEL")
    # else:
    #     print("DISTRACTOR IS THE LABEL")
    #
    # if(precentage_of_target_OF_TEST>precentage_of_distractor_OF_TEST):
    #     print("TARGET IS THE TEST")
    # else:
    #     print("DISTRACTOR IS THE TEST")

    if precentage_of_target_OF_LABEL>precentage_of_distractor_OF_LABEL and precentage_of_target_OF_TEST>precentage_of_distractor_OF_TEST:
        print("WEEEEE WIIIINNNNNN")
        return 1
    else:
        print("LOSE")
        return 0
    #
    # print("percentage: ")
    # print(max(precentage_of_target,precentage_of_distractor))
    # print("precentage of target: " + str(precentage_of_target))
    # print("precentage_of_distractor: " + str(precentage_of_distractor))

if __name__=='__main__':
    main()



