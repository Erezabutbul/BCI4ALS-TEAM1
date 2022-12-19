import pandas as pd
from parameters import *

# currently cutting each type of trail - type = ["baseLine", "target", "distractor"]
# saving in different folder
# the format is : each raw represents a specific occurrence of "type"
# this raw has all the data according to this occurrence
# number of raws is the number of occurrences of "type"

def cut(durationBeforeStimuli,durationAfterStimuli, markers_path, eeg_path, type):
    markers = pd.read_csv(markers_path)
    eeg = pd.read_csv(eeg_path)
    allTrials = list()

    for index, marker in markers.iterrows():
        trial = dict()
        midTrial = list()
        # marker[1] - the start time
        # marker[2] - the type of the marker
        curr_type = marker[2]
        if curr_type == type:
            if marker[1] - durationBeforeStimuli >= 0:
                start_time = marker[1] - durationBeforeStimuli
            else:
                start_time = 0
            end_time = marker[1] + durationAfterStimuli
            for j, e in eeg.iterrows():
                if e[1] > end_time:
                    break
                elif start_time <= e[1] <= end_time:
                    trial["timeStamp"] = e[1]
                    trial["channel_1"] = e[2]
                    trial["channel_2"] = e[3]
                    trial["channel_3"] = e[4]
                    trial["channel_4"] = e[5]
                    trial["channel_5"] = e[6]
                    trial["channel_6"] = e[7]
                    trial["channel_7"] = e[8]
                    trial["channel_8"] = e[9]
                    trial["channel_9"] = e[10]
                    trial["channel_10"] = e[11]
                    trial["channel_11"] = e[12]
                    trial["channel_12"] = e[13]
                    trial["channel_13"] = e[14]
                    trial["channel_14"] = e[15]
                    trial["channel_15"] = e[16]
                    trial["channel_16"] = e[17]
                    midTrial.append(trial)
            allTrials.append(midTrial)
            # print(len(trial))
    return allTrials


def main():
    # markers_path = "output_files/Marker_Recordings/listOfMarkers 14_12_2022 at 12_30_26_PM"
    # eeg_path = "output_files/EEG_Recordings/EEG 14_12_2022 at 12_30_26_PM"
    markers_path = markers_file_name
    eeg_path = Filtered_EEG_file_name
    durationAfterStimuli = 0.4
    durationBeforeStimuli = 0.2
    type = ["baseLine", "target", "distractor"]
    allTrialsBaseLine = cut(durationBeforeStimuli,durationAfterStimuli, markers_path, eeg_path, type[0])
    allTrialsTarget = cut(durationBeforeStimuli,durationAfterStimuli, markers_path, eeg_path, type[1])
    allTrialsDistractor = cut(durationBeforeStimuli,durationAfterStimuli, markers_path, eeg_path, type[2])

    file = pd.DataFrame(allTrialsBaseLine)
    file.to_csv(allTrialsBaseLine_file_name, index=True, index_label="index", encoding="utf_8_sig")

    file = pd.DataFrame(allTrialsTarget)
    file.to_csv(allTrialsTarget_file_name, index=True, index_label="index", encoding="utf_8_sig")

    file = pd.DataFrame(allTrialsDistractor)
    file.to_csv(allTrialsDistractor_file_name, index=True, index_label="index", encoding="utf_8_sig")



if __name__ == '__main__':
    main()
