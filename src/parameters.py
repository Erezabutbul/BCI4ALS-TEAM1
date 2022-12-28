from matplotlib import image as mpimg
from datetime import datetime
import os
import time
# Experiment parameters
StimOnset = 0.7  # (time to present the stimulus)
interTime = 0.35  # (time between stimulus)
targets_N = 2  # (number of target stimulus)

# Define stimulus types and load data
stimulusType = ["square", "triangle",
                "circle"]  # (type of stimulus to load and present- different pictures\ audio \ etc.)
circle = mpimg.imread("../images/circle.jpg")
triangle = mpimg.imread("../images/triangle.jpg")
square = mpimg.imread("../images/rectangle.jpg")
shapes = [square, triangle, circle]

target_ratio = 7  # (percentage of the oddball onsets)
trials_N = 70  # (number of trials per block)
blocks_N = 3  # (number of blocks)
targetAppearances = trials_N/target_ratio # (number of times target appear per block)


date = datetime.now().strftime("%d_%m_%Y at %I_%M_%S_%p")
# EEG_file_name = "output_files/EEG_Recordings/" + f"EEG_{date}.csv"
# markers_file_name = "output_files/Marker_Recordings/" + f"listOfMarkers_{date}.csv"
EEG_file_name = "output_files/EEG_Recordings/" + f"EEG_test.csv"
markers_file_name = "output_files/Marker_Recordings/" + f"listOfMarkers_test.csv"
Filtered_EEG_file_name = "output_files/filtered_EEG_Recordings/" + f"Filtered_EEG_test.csv"



# allTrialsBaseLine_file_name = "output_files/cut_data_by_class/baseLine/" + f"classBaseLine_{date}.csv"
# allTrialsTarget_file_name = "output_files/cut_data_by_class/target/" + f"classTarget_{date}.csv"
# allTrialsDistractor_file_name = "output_files/cut_data_by_class/distractor/" + f"classDistractor_{date}.csv"
allTrialsBaseLine_file_name = "output_files/cut_data_by_class/baseLine/" + f"classBaseLine_test.csv"
allTrialsTarget_file_name = "output_files/cut_data_by_class/target/" + f"classTarget_test.csv"
allTrialsDistractor_file_name = "output_files/cut_data_by_class/distractor/" + f"classDistractor_test.csv"
allArrangedMarkers_file_name = "output_files/ArrangedMarkersPsycho/" + f"Markers_Arranged_test.csv"

global keepRunning
keepRunning = True



