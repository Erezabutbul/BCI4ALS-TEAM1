<<<<<<< HEAD
import multiprocessing
<<<<<<< HEAD
import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from datetime import datetime
from lsl_Record_data import main as lsl_main
from GUI import showExperiment
from preProcessing import main as preProcessing_main
from data_extraction_by_class import main as data_spliting_main
from psycho_data_Arrange import main as arrange_markers_main
from avgData import main as avgData_main
from featureExtraction import main as featureExtraction_main
from featureExtractionForTest import main as featureExtractionForTest_main
from Model import main as modelToTrain
from LiveModel import main as liveModelPrediction

=======
import lsl_Record_data
import time
if __name__ == '__main__':
    multiprocessing.freeze_support()




import data_extraction_by_class
from threading import Thread
>>>>>>> 5af68f5 (erez's version)
=======
import time

import lsl_Record_data
import GUI
import data_match_and_merge
from threading import Thread
>>>>>>> 372fbdb0d3b32824a93b186dd8e6e631e12dba4b


<<<<<<< HEAD
<<<<<<< HEAD
    # Create the "EXP_{date}" directory
    if state == "train":
        exp_dir = f"output_files/EXP_{date}/"
    else:
        exp_dir = f"output_files/testSet/test_{date}/"
    os.makedirs(exp_dir, exist_ok=True)
    return exp_dir


def main():
    # state of EXP : train or test
    state = "train"
    # Create the "EXP_{date}" directory
    exp_path = createFile(state)

    with multiprocessing.Manager() as manager:
        keepRunning = manager.Value('b', True)
        # Create the processes
        p1 = multiprocessing.Process(target=lsl_main, args=[exp_path, keepRunning])
        p2 = multiprocessing.Process(target=showExperiment, args=[exp_path, keepRunning, state])

        # Start the processes
        p1.start()
        p2.start()

        # Wait for the processes to finish
        p2.join()
        p1.join()
        print("finished recording")

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

    # extract features
    featureExtraction_main(exp_path, state)

    # TODO - convert Model & LiveModel files into handleModel as discussed
    # handleModel(exp_path, state)


if __name__ == '__main__':
    main()
=======




# multiprocessing.freeze_support()
# multiprocessing.set_start_method('fork')


# Create the processes
p1 = multiprocessing.Process(target=lsl_Record_data.main)
p1.start()
time.sleep(10)
import GUI
p2 = multiprocessing.Process(target=GUI.showExperiment)
#
# Start the processes

p2.start()
# GUI.showExperiment()
# Wait for the processes to finish
p2.join()
p1.join()
print("All processes finished")

# t1 = Thread(target=lsl_Record_data.main, args=[])
# t1.start()
# lsl_Record_data.main()
# GUI.showExperiment()
# t1.join()

# data_extraction_by_class.main()

#
# import concurrent.futures
# import time
#
#
#
# # Create a ThreadPoolExecutor with 2 threads
# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     # Submit 2 tasks to the executor
#     task1 = executor.submit(lsl_Record_data.main, [])
#     task2 = executor.submit(GUI.showExperiment, [])
#
#     # Wait for the tasks to complete
#     result1 = task1.result()
#     result2 = task2.result()


# lsl_Record_data.main()


############### using subprocess

# import subprocess
# from functools import partial
#
# record = partial(lsl_Record_data.main())
#
# # Start a process that applies the record function to its input
# p1 = subprocess.Popen(["python", "-c", "print(record())"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#
# show = partial(GUI.showExperiment())
# # Start a process that prints "Goodbye, World!" every 2 seconds
# p2 = subprocess.Popen(["python", "-c", "print(show())"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Wait for both processes to complete
# p1.wait()
# p2.wait()
>>>>>>> 5af68f5 (erez's version)
=======
t1 = Thread(target=lsl_Record_data.main, args=[])
t1.start()
GUI.showExperiment()
t1.join()

data_match_and_merge.main()
>>>>>>> 372fbdb0d3b32824a93b186dd8e6e631e12dba4b
