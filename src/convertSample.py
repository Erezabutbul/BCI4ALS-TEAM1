import pandas as pd
import ast
from numpy import float_
from parameters import *


def getCol(curDf, colNum, row):
<<<<<<< HEAD
=======

>>>>>>> 5af68f5 (erez's version)
    currDict = curDf.loc[row][colNum]
    # this condition blocks the 'nan' value in the df,
    # for some reason they show up as type 'float'
    # and later give problems to "ast.literal_eval"
    if type(currDict) != float and currDict not in (None, 'nan') and type(currDict) != float_:
        currDict = ast.literal_eval(currDict)
    return currDict

<<<<<<< HEAD
# input: load recording file of the experiment
# output: create file for each block in the experiment,
#         in the format that can be sampled to feature extraction ect
def main(exp_path):
    for marker_type in marker_types:
        # read file
        df = pd.read_csv(
            exp_path + f"cut_data_by_class/{marker_type}/Mean_EEG_Signal_{marker_type}/" + f"{marker_type}_AVG_by_blocks.csv")
        df = df.iloc[:, 1:]
        numOfCol = df.shape[1]
        numOfRows = df.shape[0]
        # Select the block you want to see
        # the block is represented as a row in the mean signal file file
        for block in range(numOfRows):

            # Create a output dataframe
            outputDf = pd.DataFrame()

            for col in range(numOfCol):
                outputDf[col] = getCol(df, col, block)

            # remove the index and the timestamps
            # because we mean it would be the same value for all
            outputDf = outputDf.iloc[2:, :]

            # save the file / show it
            outputDf.to_csv(exp_path + f"cut_data_by_class/{marker_type}/Mean_EEG_Signal_{marker_type}/" + f"AVG_block_num_{block}.csv")


if __name__ == '__main__':
    main()
=======
# read file
df = pd.read_csv(
    "output_files/cut_data_by_class/baseLine/" + "Mean_EEG_Signal_baseLinebaseLine_AVG_by_blocks.csv")
df = df.iloc[:, 1:]
numOfCol = df.shape[1]
numOfRows = df.shape[0]
# Select the block you want to see
# the block is represented as a row in the mean signal file file
block = 1

# Create a output dataframe
outputDf = pd.DataFrame()


for col in range(numOfCol):
    outputDf[col] = getCol(df, col, block)

# remove the index and the timestamps
# because we mean it would be the same value for all
outputDf = outputDf.iloc[2:, :]

# save the file / show it
outputDf.to_csv("output_files/cut_data_by_class/baseLine/" + f"AVG_block_num_{block}.csv")
>>>>>>> 5af68f5 (erez's version)
