"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream
from datetime import datetime
import time
import pandas as pd

def main():
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])
    # create a dict inorder to save the data
    list_res = list()


    # change totalTimeOfTrail to get different time duration of the trail
    # can always interrupt using ctrl+c
    start_time = time.time()
    totalTimeOfTrail = 1 #3.5*60

    file_name = "EEG"
    index = 0
    try:
        while True:
            if time.time() - start_time > totalTimeOfTrail:
                break
            # get a new sample (you can also omit the timestamp part if you're not
            # interested in it)
            data = dict()
            sample, timestamp = inlet.pull_sample()
            data["timeStamp"] = timestamp
            data["channel 1"] = sample[0]
            data["channel 2"] = sample[1]
            data["channel 3"] = sample[2]
            data["channel 4"] = sample[3]
            data["channel 5"] = sample[4]
            data["channel 6"] = sample[5]
            data["channel 7"] = sample[6]
            data["channel 8"] = sample[7]
            data["channel 9"] = sample[8]
            data["channel 10"] = sample[9]
            data["channel 11"] = sample[10]
            data["channel 12"] = sample[11]
            data["channel 13"] = sample[12]
            data["channel 14"] = sample[13]
            data["channel 15"] = sample[14]
            data["channel 16"] = sample[15]
            index += 1
            list_res.append(data)
            print(timestamp, sample)
    except KeyboardInterrupt:
        pass
    file = pd.DataFrame(list_res)
    file.to_csv(file_name)

if __name__ == '__main__':
    main()