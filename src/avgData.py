import pandas as pd
import numpy as np
import ast

from numpy import float_

from parameters import *


# my function
# def meanCol(df, colNum):
#     listOfsamples = list()
#     numOfRows = len(df)
#     meanDict = ast.literal_eval(df.iloc[0, colNum])
#     for i in range(1, numOfRows):
#         currDict = ast.literal_eval(df.iloc[i, colNum])
#         for key in meanDict:
#             meanDict[key] = meanDict[key] + currDict[key]
#     for key in meanDict:
#         meanDict[key] = meanDict[key] / numOfRows
#     return meanDict

# chat gtp function
def meanCol(df, colNum):
    numOfRows = len(df)
    meanDict = {}
    for i in range(numOfRows):
        currDict = df.loc[i][colNum]
        # this condition blocks the 'nan' value in the df,
        # for some reason they show up as type 'float'
        # and later give problems to "ast.literal_eval"
        if type(currDict) != float and currDict not in (None, 'nan') and type(currDict) != float_:
            currDict = ast.literal_eval(currDict)
            for key, value in currDict.items():
                meanDict[key] = meanDict.get(key, 0) + value

    for key in meanDict:
        meanDict[key] = meanDict[key] / numOfRows
    return meanDict







def main():
    for marker_type in marker_types:
        # df = pd.read_csv(getTheMostUpdatedFile(f"output_files/cut_data_by_class/{marker_type}/"))
        # if marker_type == "distractor":
        #     df = pd.read_csv("output_files/cut_data_by_class/distractor/" +"class_distractor_21_12_2022 at 06_50_22_PM______DATAFROMNADAV.csv")
        # elif marker_type == "target":
        #     df = pd.read_csv("output_files/cut_data_by_class/target/" +"class_target_21_12_2022 at 06_50_22_PM______DATAFROMNADAV.csv")
        # else:
        #     df = pd.read_csv("output_files/cut_data_by_class/baseLine/" +"class_baseLine_21_12_2022 at 06_50_22_PM______DATAFROMNADAV.csv")
            # removing indexes
        df = pd.read_csv(
        "output_files/cut_data_by_class/target/" + "class_target_27_12_2022 at 01_03_32_PM_ErezFirstRecord.csv")
        # cut the index column, and
        # according to the number of samples that supposed to see in the current sampling rate
        df = df.iloc[:, 1:(numOfsamplesToCut + 1)]
        numOfCol = df.shape[1]
        outputDf = pd.DataFrame()
        # print(numOfCol)
        for col in range(numOfCol):
            # Convert the dictionary to a Pandas series
            # print(meanCol(df, col))
            # print(meanCol(df, col)['channel_5'] - meanCol(df, col+1)['channel_5'])
            # print("_____________________________ new mean col ______________________________________________")
            # series = pd.Series(meanCol(df, col))
            # outputDf[col] = series
            outputDf[col] = meanCol(df, col)
            # pd.concat(outputDf[col], meanCol(df, col))

        # remove the index and timeStamp on the current dataframe
        outputDf.to_csv(f"output_files/cut_data_by_class/target/Mean_EEG_Signal_" + f"class_target_27_12_2022 at 01_03_32_PM_ErezFirstRecordMEANED.csv.csv",index=True,index_label="index", encoding="utf_8_sig")
        # outputDf.to_csv(f"output_files/cut_data_by_class/{marker_type}/Mean_EEG_Signal_{marker_type}{mean_EEG_file_name}" + f"{marker_type}.csv",index=True,index_label="index", encoding="utf_8_sig")

    # print(meanCol(df, 1))


if __name__ == '__main__':
    main()

# from parameters import *
# import numpy as np
# import pandas as pd
# import ast
#
#
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
