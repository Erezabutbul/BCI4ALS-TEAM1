import pandas as pd
from parameters import *
import os

# currently cutting each type of trail - type = ["baseLine", "target", "distractor"]
# saving in different folder
# the format is : each raw represents a specific occurrence of "type"
# this raw has all the data according to this occurrence
# number of raws is the number of occurrences of "type"


def main():
    # markers_path = "output_files/Marker_Recordings/listOfMarkers 14_12_2022 at 12_30_26_PM"
    # eeg_path = "output_files/EEG_Recordings/EEG 14_12_2022 at 12_30_26_PM"

    markers_file_name = "./output_files/markersPsycho/" + f"listOfMarkers_26_12_2022 at 05_28_33_PM_ErezFirstRecord_D.csv"
    ex= pd.read_csv(markers_file_name)
    col_names = ex.columns
    markers= pd.read_csv(markers_file_name, usecols=[col_names[0]])
    markers_cols = markers.columns

    
    timeStamps=[]
    descriptions=[]

    for marker in markers[markers_cols[0]]:
            print(marker)
            if(isinstance(marker,str) and marker.__contains__("EXP")):
                EXP_marker = marker.split(" \tEXP \t")
                # print("marker - " +marker)
                # print(EXP_marker[0] + "-" + EXP_marker[1])
                timeStamps.append(EXP_marker[0])
                descriptions.append(EXP_marker[1])

    markers_Arranged = {
        'timeStamp': timeStamps,
        'description': descriptions
    }

    file = pd.DataFrame(markers_Arranged)
    file.to_csv(allArrangedMarkers_file_name, index=True, index_label="index", encoding="utf_8_sig")





    # print(ex[col_names[0]])

    # first_c = ex.columns[0]
    # first_c_vals = ex[first_c]

    # first_c_new = first_c_vals[0] 
    # print(first_c)
    # print(first_c_vals.to_string())
    # print(first_c_new)
    # for v in first_c_vals:
    #     print(v)

    # for (index, colname) in enumerate(ex):
    #     print("index - " + f"{index}")
    #     print("colname - " + f"{colname}")
    #     if(index == 0):
    #         markers= ex[colname][0]

    # print(markers)

    # for marker in markers:
    #     print(marker)
    #     if(marker.__contains__("EXP")):
    #         EXP_marker = marker.split(" \tEXP \t")
    #         # print("marker - " +marker)
    #         # print(EXP_marker[0] + "-" + EXP_marker[1])
    #         timeStamps.append(EXP_marker[0])
    #         descriptions.append(EXP_marker[1])

    # markers_Arranged = {
    #     'timeStamp': timeStamps,
    #     'description': descriptions
    # }

    # file = pd.DataFrame(markers_Arranged)
    # file.to_csv(allArrangedMarkers_file_name, index=True, index_label="index", encoding="utf_8_sig")

    ##########################################################################################

    # timeStamps=[]
    # descriptions=[]

    # for col in ex:
    #     # print(ex[col])
    #     # print("_")
    #     for marker in ex[col]:
    #         print(marker)
    #         if(marker.__contains__("EXP")):
    #             EXP_marker = marker.split(" \tEXP \t")
    #             # print("marker - " +marker)
    #             # print(EXP_marker[0] + "-" + EXP_marker[1])
    #             timeStamps.append(EXP_marker[0])
    #             descriptions.append(EXP_marker[1])

    # markers_Arranged = {
    #     'timeStamp': timeStamps,
    #     'description': descriptions
    # }

    # file = pd.DataFrame(markers_Arranged)
    # file.to_csv(allArrangedMarkers_file_name, index=True, index_label="index", encoding="utf_8_sig")

    #####################################################################################################################################

    # file = pd.DataFrame(markers_Arranged)
    # file.to_csv(allArrangedMarkers_file_name, index=True, index_label="index", encoding="utf_8_sig")


    # firstColumn=""
    # example = pd.read_csv(markers_file_name)
    # for e in example:
    #     firstColumn=e
    # markers = pd.read_csv(markers_file_name , index_col= firstColumn)

    # timeStamps=[]
    # descriptions=[]
    
    # for marker in markers.iterrows():
        
    #     if(marker[0].__contains__("EXP")):
    #         x = marker[0].split(" \tEXP \t")
    #         # print("marker - " +marker[0])
    #         # print(x[0] + "-" + x[1])
    #         timeStamps.append(x[0])
    #         descriptions.append(x[1])
    # print(timeStamps)
    # print(descriptions)

    # markers_Arranged = {
    #     'timeStamp': timeStamps,
    #     'description': descriptions
    # }

    # file = pd.DataFrame(markers_Arranged)
    # file.to_csv(allArrangedMarkers_file_name, index=True, index_label="index", encoding="utf_8_sig")




if __name__ == '__main__':
    main()
