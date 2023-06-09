import numpy as np
import pandas as pd

def getPredictionPrecentage(startIndex,EndIndex):
    voting_results = []  # Initialize an empty list to store voting results

    for i in range(startIndex, EndIndex, 5):
        subarray = arr[i:i + 5]  # Get a subarray of 5 elements
        total = np.sum(subarray)
        if total > 2:
            voting_results.append(1)
        else:
            voting_results.append(0)
    totalOnes = np.sum(voting_results)
    return (totalOnes / (EndIndex - startIndex)) * 100

# Example input array
arr = np.array([1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1])
num_of_target_trials_path = "../src/output_files/" + "featuresAndModel/" + "features/"
filename = 'num_tails_elecs_conditions.csv'
df = pd.read_csv(num_of_target_trials_path+filename, header=None)
endOfTarget = int(df.iloc[0, 0])
precentage_of_target = getPredictionPrecentage(0, endOfTarget)
precentage_of_distractor = getPredictionPrecentage(0, endOfTarget)


print(max(precentage_of_target,precentage_of_distractor)) # Output: [1, 0, 1, 0]



