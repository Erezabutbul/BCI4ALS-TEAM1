<<<<<<< HEAD
import pandas as pd
from parameters import *
import os

<<<<<<< HEAD
# purse the psychopy output file into a readable csv file
def main(exp_path):
    completePath = exp_path + markers_psycho_folder_path + markers_psycho_file_name
    ex = pd.read_csv(completePath)
    col_names = ex.columns
    markers = pd.read_csv(completePath, usecols=[col_names[0]])
    markers_cols = markers.columns

    timeStamps = []
    descriptions = []

    for marker in markers[markers_cols[0]]:
        # print(marker)
        if isinstance(marker, str) and marker.__contains__("EXP"):
            EXP_marker = marker.split(" \tEXP \t")
            # print("marker - " +marker)
            # print(EXP_marker[0] + "-" + EXP_marker[1])
            timeStamps.append(EXP_marker[0])
            descriptions.append(EXP_marker[1])

    markers_Arranged = {
        'timeStamp': timeStamps,
        'description': descriptions
    }

    ###########################################################
    # save to "EXP_{date}" directory
    arrengedMarkers = exp_path + markers_arranged_folder_path
    os.makedirs(arrengedMarkers, exist_ok=True)
    #########################################################
    file = pd.DataFrame(markers_Arranged)
    file.to_csv(arrengedMarkers + markers_arranged_file_name, index=True, index_label="index", encoding="utf_8_sig")



if __name__ == '__main__':
    main()
=======

ex = pd.read_csv(markers_file_name_FORTEST)
col_names = ex.columns
markers = pd.read_csv(markers_file_name_FORTEST, usecols=[col_names[0]])
markers_cols = markers.columns

timeStamps = []
descriptions = []

for marker in markers[markers_cols[0]]:
    print(marker)
    if isinstance(marker, str) and marker.__contains__("EXP"):
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
file.to_csv(markers_psycho_folder_path + f"{date}_Fixed.csv", index=True, index_label="index", encoding="utf_8_sig")
>>>>>>> 5af68f5 (erez's version)
=======
>>>>>>> 372fbdb0d3b32824a93b186dd8e6e631e12dba4b
