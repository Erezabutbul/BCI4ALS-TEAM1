import pandas as pd
from parameters import *


def cut(durationBeforeStimuli, durationAfterStimuli, markers_path, eeg_path, marker_type):
    markers = pd.read_csv(markers_path)
    eeg = pd.read_csv(eeg_path)
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
            allTrial.append(trial_data)
    return allTrial


def main():
    markers_path = markers_file_name
    # TODO - make sure you change to filtered after all the BALAGAN
    eeg_path = EEG_file_name
    durationAfterStimuli = 0.4
    durationBeforeStimuli = 0.2
    marker_types = ["baseLine", "target", "distractor"]

    for marker_type in marker_types:
        allTrialOfType = cut(durationBeforeStimuli, durationAfterStimuli, markers_path, eeg_path, marker_type)
        df = pd.DataFrame(allTrialOfType)
        df.to_csv(f"output_files/cut_data_by_class/{marker_type}/" + f"class_{marker_type}_after_tests.csv", index=True,
                  index_label="index", encoding="utf_8_sig")


if __name__ == '__main__':
    main()
