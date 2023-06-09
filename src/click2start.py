import multiprocessing
# import os
# with contextlib.redirect_stdout(None):
    # import pygame
# from datetime import datetime
from lsl_Record_data import main as lsl_main
from GUI import showExperiment
from preProcessing import main as preProcessing_main
from psycho_data_Arrange import main as arrange_markers_main
from featureExtractionMNE import main as featureExtraction_main
from Model import main as model_main
from parameters import *

def createFile():
    # date & time
    date = datetime.now().strftime("%d_%m_%Y at %I_%M_%S_%p")

    # Create the "EXP_{date}" directory
    if modes[mode] == "TRAIN":
        exp_dir = f"output_files/EXP_{date}/"
    else:
        exp_dir = f"output_files/testSet/test_{date}/"
    os.makedirs(exp_dir, exist_ok=True)
    return exp_dir


def main():
    # modes of EXP : train or test
    # Create the "EXP_{date}" directory
    exp_path = createFile()

    with multiprocessing.Manager() as manager:
        keepRunning = manager.Value('b', True)
        # Create the processes
        p1 = multiprocessing.Process(target=lsl_main, args=[exp_path, keepRunning])
        p2 = multiprocessing.Process(target=showExperiment, args=[exp_path, keepRunning, modes[mode]])

        # Start the processes
        p1.start()
        p2.start()

        # Wait for the processes to finish
        p2.join()
        p1.join()
        print("finished recording")


    print("arranging and splitting data...")
    # Arrange the data by psychopy
    arrange_markers_main(exp_path)

    print("pre processing...")
    # pre processing
    epoch_target, epoch_distractor, epoch_baseLine, epoch_target_df, epoch_distractor_df, epoch_baseLine_df = preProcessing_main(exp_path)

    # overwrites every features and models folder
    # extract features
    featureExtraction_main(exp_path, modes[mode], epoch_target, epoch_distractor)

    # model TRAIN / TEST
    model_main(exp_path)
    


if __name__ == '__main__':
    main()
