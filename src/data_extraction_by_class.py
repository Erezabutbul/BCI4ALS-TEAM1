import pandas as pd
from parameters import *
import os
from datetime import datetime


def cut(durationBeforeStimuli, durationAfterStimuli, currentMarkerFile, currentEEGFile, marker_type):
    markers = pd.read_csv(currentMarkerFile)
    eeg = pd.read_csv(currentEEGFile)
    allTrial = list()
    for index, marker in markers.iterrows():
        curr_type = marker[2]

        if curr_type in marker_type:
            # setting time for beginning of sample
            if marker[1] - durationBeforeStimuli >= 0:
                start_time = marker[1] - durationBeforeStimuli
            else:
                start_time = 0
            # setting time for end of sample
            end_time = marker[1] + durationAfterStimuli

            trial_data = eeg.loc[
                (start_time <= eeg["timeStamp"]) & (eeg["timeStamp"] <= end_time),
                ["index", "timeStamp", *[f"channel_{i}" for i in range(1, 17)]]
            ].to_dict("records")

            # TODO - check
            # # Get the index of the start_time row
            # start_index = eeg[eeg["timeStamp"] >= start_time].index[0]
            #
            # # Select the rows from start_index -start_index to start_index + numOfsamplesToCut
            # trial_data = eeg.iloc[start_index:start_index + numOfsamplesToCut, :]
            #
            # # Select the relevant columns
            # trial_data = trial_data[["index", "timeStamp", *[f"channel_{i}" for i in range(1, 17)]]]
            #
            # # Convert to a list of dictionaries
            # trial_data = trial_data.to_dict("records")

            allTrial.append(trial_data)

        elif curr_type == 'startBlock':
            allTrial.append(["startBlock"])
    return allTrial


def main():
    # currentMarkerFile = markers_folder_path + getTheMostUpdatedFile(markers_folder_path)
    # TODO - make sure you change to filtered after all the BALAGAN
    # currentEEGFile = EEG_folder_path + getTheMostUpdatedFile(EEG_folder_path)
    currentEEGFile = EEG_file_name_FORTEST

    currentMarkerFile = markers_psycho_file_name_FORTEST
    # currentEEGFile = EEG_file_name_FORTEST

    for marker_type in marker_types:
        allTrialOfType = cut(durationBeforeStimuli, durationAfterStimuli, currentMarkerFile, currentEEGFile,
                             marker_type)
        df = pd.DataFrame(allTrialOfType)
        df.to_csv(f"output_files/cut_data_by_class/{marker_type}/" + f"class_{marker_type}_{date}.csv", index=True,
                  index_label="index", encoding="utf_8_sig")


if __name__ == '__main__':
    main()
