import multiprocessing
import os
from datetime import datetime
from lsl_Record_data import main as lsl_main
from GUIForTest import showExperiment as showExperimentForTest
from preProcessing import main as preProcessing_main
from data_extraction_by_class import main as data_spliting_main
from psycho_data_Arrange import main as arrange_markers_main
from avgData import main as avgData_main
from featureExtractionForTest import main as featureExtractionForTest_main
from LiveModel import main as liveModelPrediction


def createFile():
    # date & time
    date = datetime.now().strftime("%d_%m_%Y at %I_%M_%S_%p")

    # Create the "EXP_{date}" directory
    exp_dir = f"output_files/testSet/test_{date}/"
    os.makedirs(exp_dir, exist_ok=True)
    return exp_dir


def main():
    # Create the "test_{date}" directory
    exp_path = createFile()

    with multiprocessing.Manager() as manager:
        keepRunning = manager.Value('b', True)
        # Create the processes
        p1 = multiprocessing.Process(target=lsl_main, args=[exp_path, keepRunning])
        p2 = multiprocessing.Process(target=showExperimentForTest, args=[exp_path, keepRunning])

        # Start the processes
        p1.start()
        p2.start()

        # Wait for the processes to finish
        p2.join()
        p1.join()
        print("finished recording\n\n")

    print("pre processing...")
    # pre processing
    preProcessing_main(exp_path)

    print("arranging and splitting data...")
    # Arrange the data by psychopy
    arrange_markers_main(exp_path)

    # extract data by class
    data_spliting_main(exp_path)

    print("AVG...")
    # avg data
    avgData_main(exp_path)

    # test feature extraction
    print("extracting features from test set...")
    featureExtractionForTest_main(exp_path)

    # predict
    liveModelPrediction(exp_path)




if __name__ == '__main__':
    main()
