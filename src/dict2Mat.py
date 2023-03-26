# import pandas as pd
import ast
from numpy import float_
from parameters import *
# import os


def getCol(curDf, colNum, row):
    currDict = curDf.loc[row][colNum]
    # this condition blocks the 'nan' value in the df,
    # for some reason they show up as type 'float'
    # and later give problems to "ast.literal_eval"
    if type(currDict) != float and currDict not in (None, 'nan') and type(currDict) != float_:
        currDict = ast.literal_eval(currDict)
    return currDict

# input: load cut by class recording file
# output: create file for each class in the experiment,
#         in the format that can be sampled to feature extraction ect
def main(exp_path):
    for marker_type in marker_types:

        if marker_type == "baseLine":  # no need to extract baseline trials
            continue

        # read file
        df = pd.read_csv(
            exp_path + f"/cut_data_by_class/{marker_type}/class{marker_type}.csv")
        # removing indexes
        # cut the index column, and
        # according to the number of samples that supposed to see in the current sampling rate
        df = df.iloc[:, 1:(numOfSamplesToCut + 1)]

        # Find the indices of the rows containing the startBlock markers
        start_block_indices = df.index[df['0'] == 'startBlock'].tolist()

        # Iterate over the list of start block indices
        for i in range(len(start_block_indices)):
            # Slice the dataframe from the current start block index to the next start block index
            if i < len(start_block_indices) - 1:
                startRow = start_block_indices[i] + 1
                endRow = start_block_indices[i + 1]
            else:
                startRow = start_block_indices[len(start_block_indices) - 1] + 1
                endRow = df.shape[0]

            sliced_df = df.iloc[startRow:endRow, :]
            numOfCol = sliced_df.shape[1]
            if not sliced_df.empty:
                # Select the trial you want to see
                # the trial is represented as a row in the block
                for trial in range(startRow, endRow):
                    # Create a output dataframe
                    outputDf = pd.DataFrame()

                    for col in range(numOfCol):
                        outputDf[col] = getCol(sliced_df, col, trial)

                    # remove the index and the timestamps
                    outputDf = outputDf.iloc[2:, :]

                    # check if directory exists, if not make one
                    directory = exp_path + f"/cut_data_by_class/{marker_type}/Trial_EEG_Signal_{marker_type}/"
                    if not os.path.exists(directory):
                        os.makedirs(directory)

                    # save the file / show it
                    outputDf.to_csv(exp_path + f"/cut_data_by_class/{marker_type}/Trial_EEG_Signal_{marker_type}/"
                                    + f"Trial_num_{trial}.csv")


if __name__ == '__main__':
    main()
