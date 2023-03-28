from preProcessing import main as preProcessing_main
from featureExtractionMNE import main as featureExtraction_main
from parameters import *

"""
    MAKE SURE YOU CHANGE THE PARAMETERS BEFORE RUNNING
"""


def getEXPFoldersList(main_folder):
    # get all the experiment folders
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('EXP')]

    #

    return exp_folders


def getTESTFoldersList(main_folder):
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('test')]
    return exp_folders

def main():
    # for each folder of exp of data
    data_folder_list = getEXPFoldersList(output_files)
    # data_folder_list = getEXPFoldersList(output_files + "/" + "testSet/")
    print("number of data folders found: " + str(len(data_folder_list)))

    for curr_folder_path in data_folder_list:

        indexOfFile = data_folder_list.index(curr_folder_path) + 1

        curr_folder_path = output_files + "/" + curr_folder_path + "/"
        # curr_folder_path = output_files + "/" + "testSet/" + curr_folder_path + "/"

        print(f"arranging and splitting data file number: {indexOfFile}")
        # Arrange the data by psychopy
        # arrange_markers_main(curr_folder_path)


        print(f"pre processing file number: {indexOfFile}")
        # pre processing
        epoch_target, epoch_distractor, epoch_baseLine, epoch_target_df, epoch_distractor_df, epoch_baseLine_df = preProcessing_main(curr_folder_path)

        print(f"extracting features: {indexOfFile}")
        # # extract features
        featureExtraction_main(curr_folder_path, modes[mode], epoch_target, epoch_distractor)

        # model_main(curr_folder_path)


if __name__ == '__main__':
    main()
