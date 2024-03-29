from parameters import *
"""
args:
    keepRunning - boolian that indicate the lsl stream to stop
"""
def main(exp_path, keepRunning):

    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = pylsl.resolve_stream('type', 'EEG')
    # create a new inlet to read from the stream
    inlet = pylsl.StreamInlet(streams[0])

    # create a dict inorder to save the data
    list_res = list()

    index = 0

    while keepRunning.value:

        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        data = dict()
        sample, timestamp = inlet.pull_sample()
        data["timeStamp"] = pylsl.local_clock()
        data["channel_1"] = sample[0]
        data["channel_2"] = sample[1]
        data["channel_3"] = sample[2]
        data["channel_4"] = sample[3]
        data["channel_5"] = sample[4]
        data["channel_6"] = sample[5]
        data["channel_7"] = sample[6]
        data["channel_8"] = sample[7]
        data["channel_9"] = sample[8]
        data["channel_10"] = sample[9]
        data["channel_11"] = sample[10]
        data["channel_12"] = sample[11]
        data["channel_13"] = sample[12]
        data["channel_14"] = sample[13]
        data["channel_15"] = sample[14]
        data["channel_16"] = sample[15]
        index += 1
        list_res.append(data)


    # save to "EXP_{date}" directory
    EEG_dir = exp_path + "EEG_Recordings"
    os.makedirs(EEG_dir, exist_ok=True)
    
    file = pd.DataFrame(list_res)
    file.to_csv(EEG_dir + "/" + EEG_file_name, index=True, index_label="index", encoding="utf_8_sig")


if __name__ == '__main__':
    main()


