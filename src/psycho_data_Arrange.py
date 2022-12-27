import pandas as pd
from parameters import *
import os


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
file.to_csv(markers_folder_path + "listOfMarkers_26_12_2022 at 05_28_33_PM_ErezFirstRecord_FIXED.csv", index=True, index_label="index", encoding="utf_8_sig")
