import pandas as pd
import ast
from parameters import *
import os
<<<<<<< HEAD
from convertSample import main as convert_blocks_main
=======
>>>>>>> 5af68f5 (erez's version)

# ORIGINAL
# def meanCol(df, colNum, numOfRows):
#     numOfRows = len(df)
#     meanDict = {}
#     for i in range(numOfRows):
#         currDict = df.loc[i][colNum]
#         # this condition blocks the 'nan' value in the df,
#         # for some reason they show up as type 'float'
#         # and later give problems to "ast.literal_eval"
#         if type(currDict) != float and currDict not in (None, 'nan') and type(currDict) != float_:
#             currDict = ast.literal_eval(currDict)
#             for key, value in currDict.items():
#                 meanDict[key] = meanDict.get(key, 0) + value
#
#     for key in meanDict:
#         meanDict[key] = meanDict[key] / numOfRows
#     return meanDict
<<<<<<< HEAD
def meanAll(df, colNum, numOfRows):
    numOfRows = len(df)
    meanDict = {}
    for i in range(numOfRows):
        currDict = df.loc[i][colNum]

        for key, value in currDict.items():
            meanDict[key] = meanDict.get(key, 0) + value
    for key in meanDict:
        meanDict[key] = meanDict[key] / numOfRows
    return meanDict

=======
>>>>>>> 5af68f5 (erez's version)

def meanCol(df, colNum, startRow, endRow):
    numOfRows = len(df)
    meanDict = {}
    for i in range(startRow, endRow):
        currDict = df.loc[i][colNum]
        # this condition blocks the 'nan' value in the df,
        # for some reason they show up as type 'float'
        # and later give problems to "ast.literal_eval"
        if type(currDict) != float and currDict not in (None, 'nan'):
            currDict = ast.literal_eval(currDict)
            for key, value in currDict.items():
                meanDict[key] = meanDict.get(key, 0) + value

    for key in meanDict:
        meanDict[key] = meanDict[key] / numOfRows
    return meanDict


def meanByBlock(df):
    # Find the indices of the rows containing the startBlock markers
    start_block_indices = df.index[df['0'] == 'startBlock'].tolist()
    # List that will contain the mean values per block
    listOfBlock = list()
    # Iterate over the list of start block indices
    for i in range(len(start_block_indices)):
        listOfCols = list()
        # Slice the dataframe from the current start block index to the next start block index
        if i < len(start_block_indices) - 1:
            startRow = start_block_indices[i] + 1
            endRow = start_block_indices[i + 1]
        else:
            startRow = start_block_indices[len(start_block_indices) - 1] + 1
            endRow = df.shape[0]

        sliced_df = df.iloc[startRow:endRow, :]
        if not sliced_df.empty:
            for col in range(sliced_df.shape[1]):
                col_means = meanCol(sliced_df, col, startRow, endRow)
                listOfCols.append(col_means)
            listOfBlock.append(listOfCols)

    return listOfBlock


<<<<<<< HEAD
def main(exp_path):
    for marker_type in marker_types:
        if marker_type == "distractor":
            df = pd.read_csv(
                exp_path + allTrialsDistractor_folder_path + allTrialsDistractor_file_name)
        elif marker_type == "target":
            df = pd.read_csv(exp_path + allTrialsTarget_folder_path + allTrialsTarget_file_name)
        else:
            df = pd.read_csv(exp_path + allTrialsBaseLine_folder_path + allTrialsBaseLine_file_name)
        # removing indexes
        # cut the index column, and
        # according to the number of samples that supposed to see in the current sampling rate
        df = df.iloc[:, 1:(numOfSamplesToCut + 1)]

        outputDf = pd.DataFrame(meanByBlock(df))

        ###########################################################
        # save to "EXP_{date}" directory
        meanedData = exp_path + allClasses + marker_type + f"/Mean_EEG_Signal_{marker_type}/"
        os.makedirs(meanedData, exist_ok=True)
        #########################################################

        # save AVG by block
        outputDf.to_csv(
            meanedData + f"{marker_type}_AVG_by_blocks.csv",
            index=True, index_label="index", encoding="utf_8_sig")

        # AVG all the EXP
        avgAllDf = pd.DataFrame()
        for col in range(outputDf.shape[1]):
            avgAllDf[col] = meanAll(outputDf, col, outputDf.shape[0])
        # save AVG by all EXP
        avgAllDf.to_csv(
            meanedData + f"{marker_type}_AVG_all_the_EXP.csv",
            index=True, index_label="index", encoding="utf_8_sig")

    # make an avg for each block and save it
    convert_blocks_main(exp_path)






=======
def main():
    for marker_type in marker_types:
        if marker_type == "distractor":
            df = pd.read_csv(
                "output_files/cut_data_by_class/distractor/" + "class_distractor_28_12_2022 at 12_59_52_PM.csv")
        elif marker_type == "target":
            df = pd.read_csv("output_files/cut_data_by_class/target/" + "class_target_28_12_2022 at 12_59_52_PM.csv")
        else:
            df = pd.read_csv(
                "output_files/cut_data_by_class/baseLine/" + "class_baseLine_28_12_2022 at 12_59_52_PM.csv")
        # removing indexes
        # cut the index column, and
        # according to the number of samples that supposed to see in the current sampling rate
        df = df.iloc[:, 1:(numOfsamplesToCut + 1)]

        outputDf = pd.DataFrame(meanByBlock(df))

        outputDf.to_csv(
            f"output_files/cut_data_by_class/{marker_type}/Mean_EEG_Signal_{marker_type}/" + f"{marker_type}_AVG_by_blocks.csv",
            index=True, index_label="index", encoding="utf_8_sig")

>>>>>>> 5af68f5 (erez's version)

# print(meanCol(df, 1))
#         outDir = os.path.abspath(f"output_files/cut_data_by_class/{marker_type}/Mean_EEG_Signal_{marker_type}/")
#
#         # Save the DataFrame to a CSV file in the output directory
#         outputDf.to_csv(outDir + f"{marker_type}_AVG_by_blocks.csv", index=True,
#                         index_label="index", encoding="utf_8_sig")

if __name__ == '__main__':
    main()

# from parameters import *
# import numpy as np
# import pandas as pd
# import ast
#
#
# for col in range(numOfCol):
#     outputDf[col] = meanCol(df, col)
#
# # go through all the conditions
#
# # some kind of for that iterates and reads all the file type
# fname = "C:\\Users\\Erez\\Desktop\\BCI4ALS-TEAM1\\src\\output_files\\cut_data_by_class\\target\\class_target_19_12_2022 at 01_36_15_PM.csv"
#
# df = pd.read_csv(fname)
# l = list()
# df = df.iloc[:, 1:] # df.iloc[rows,columns]
# for line in df.loc[1]:
#     print(line)
#     l.append(line)
# print("__________________________")
# l[0]
# print("____________")
# l[1]
#
# lines = [ast.literal_eval(line) for line in df.loc[1]]
#
# type(lines) # list
#
# type(lines[0]) # dict
#
# lines[0]["channel_1"] # number
#
#
# def dict_mean(dict_list):
#     mean_dict = {}
#     for key in dict_list.keys():
#         mean_dict[key] = np.mean([d[key] for d in dict_list], axis=0)
#     return mean_dict
#
#
# # def avgCol(currentCol,df,lengthOfDF):
# #     arr = np.array(16)
# #     for i in range(0,lengthOfDF):
# #         currDict = df.iloc[i,currentCol]
# #         for key in currDict.keys():
