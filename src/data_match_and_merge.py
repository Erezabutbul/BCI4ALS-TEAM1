import pandas as pd
import parameters as p


def cut(ms, markers_path, eeg_path, type):
    markers = pd.read_csv(markers_path)
    eeg = pd.read_csv(eeg_path)
    eeg_index = 0

    line = list()

    allTrials = list()
    # for index, e in eeg.iterrows():
    #     print(e[1])

    for index, marker in markers.iterrows():
        trial = list()
        curr_type = marker[2]
        if curr_type == type:
            start_time = marker[1]
            end_time = start_time + ms
            while eeg["timeStamp"][eeg_index] < start_time:
                eeg_index += 1
            # while eeg["timeStamp"][eeg_index]<end_time:
            #     trial.append(eeg[][eeg_index])
            print(eeg_index)
            for eeg_index, e in eeg.iterrows():
                if e[1] > end_time:
                    break
                else:
                    trial.append(e)
                # eeg_index += 1
        allTrials.append(trial)
        print(len(trial))
        # print(len(allTrials))

    return allTrials


def main():
    markers_path = "output_files/Marker_Recordings/x.csv"
    eeg_path = "output_files/EEG_Recordings/y"
    ms = 0.4
    type = "target"
    cut(ms, markers_path, eeg_path, type)


def getSegment(ms, startTime, eeg_path):
    eeg = pd.read_csv(eeg_path)


if __name__ == '__main__':
    main()
