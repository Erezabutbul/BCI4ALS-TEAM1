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
    totalTrials = (lastTrial - firstTrial)/len(selected_channels)
    return (totalOnes / totalTrials) * 100

# Example input array
# arr = np.array([1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1])
# num_of_target_trials_path = "../src/output_files/" + "featuresAndModel/" + "features/"
# filename = 'num_tails_elecs_conditions.csv'
# df = pd.read_csv(num_of_target_trials_path+filename, header=None)
# endOfTarget = int(df.iloc[0, 0])
def main(arr, exp_path):
    test_feature_folder_path = os.path.join(output_files, exp_path, test_features_folder_name)
    df = pd.read_csv(test_feature_folder_path + num_trails_elecs_conditions_file_name, header=None)
    endOfCondition1 = int(df.iloc[0, 0])
    precentage_of_target = getPredictionPrecentage(0, endOfCondition1, arr)
    precentage_of_distractor = getPredictionPrecentage(endOfCondition1, len(arr), arr)

    if(precentage_of_target>precentage_of_distractor):
        print("TARGET is the selected condition")
    else:
        print("DISTRACTOR is the selected condition")

    print("percentage: ")
    print(max(precentage_of_target, precentage_of_distractor)) # Output: [1, 0, 1, 0]

if __name__=='__main__':
    main()



