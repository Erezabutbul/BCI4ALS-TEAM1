import multiprocessing
from datetime import datetime
from lsl_Record_data import main as lsl_main
from GUI import showExperiment
from preProcessing import main as preProcessing_main
from psycho_data_Arrange import main as arrange_markers_main
from featureExtractionMNE import main as featureExtraction_main
from Model import main as model_main
from parameters import *
from starting_gui import main as startingGui
import os


"""
create file folder according to the given mode
"""
def createFile(mode):

    # if output_files doesn't exist - create it
    os.makedirs(output_files, exist_ok=True)
    # date & time
    date = datetime.now().strftime("%d_%m_%Y at %I_%M_%S_%p")
    # Create the "EXP_{date}" directory
    if mode == "TRAIN":
        exp_dir = f"output_files/EXP_{date}/"
    elif mode == "TEST":
        exp_dir = f"output_files/testSet/test_{date}/"
    else:
        raise Exception("mode is not supported")
    os.makedirs(exp_dir, exist_ok=True)
    return exp_dir

"""
1. takes arguments from user (mode, num of trials, num of blocks)
2. starts lsl stream
3. starts gui 
4. arranging markers
5. pre processing
6. trains model / shows prediction (according to mode)
"""
def main():
    
    # show starting gui. choose the parameters.
    params = []
    startingGui(params)
    gui_mode = "TRAIN" if params[0] == "mode:" else params[0]
    gui_trials = trials_N if (params[1] == "" or not params[1].isdigit() ) else int(params[1])
    gui_blocks = blocks_N if (params[2] == "" or not params[2].isdigit() ) else int(params[2])
    print(f"exp mode: {gui_mode}, num of trials: {gui_trials}, num of blocks: {gui_blocks}")
    # modes of EXP : train or test
    # Create the "EXP_{date}" directory
    exp_path = createFile(gui_mode)

    with multiprocessing.Manager() as manager:
        keepRunning = manager.Value('b', True)
        # Create the processes
        p1 = multiprocessing.Process(target=lsl_main, args=[exp_path, keepRunning])
        p2 = multiprocessing.Process(target=showExperiment, args=[exp_path, keepRunning, gui_mode, gui_trials, gui_blocks])

        # Start the processes
        p1.start()
        p2.start()

        # Wait for the processes to finish
        p2.join()
        p1.join()
        print("finished recording")


    print("arranging and splitting data...")
    # Arrange the data by psychopy - makes the psychopy log readable
    arrange_markers_main(exp_path)

    print("pre processing...")
    # pre processing
    epoch_target, epoch_distractor, epoch_baseLine, epoch_target_df, epoch_distractor_df, epoch_baseLine_df = preProcessing_main(exp_path)

    # overwrites every features and models folder
    # extract features
    featureExtraction_main(exp_path, gui_mode, epoch_target, epoch_distractor)

    # model TRAIN / TEST
    model_main(gui_mode , exp_path)
    


if __name__ == '__main__':
    main()
