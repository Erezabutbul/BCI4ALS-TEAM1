from matplotlib import image as mpimg
from datetime import datetime
import os

# Experiment parameters
StimOnset = 0.7  # (time to present the stimulus)
interTime = 0.2  # (time between stimulus)
targets_N = 2  # (number of target stimulus)

# Define stimulus types and load data
stimulusType = ["square", "triangle",
                "circle"]  # (type of stimulus to load and present- different pictures\ audio \ etc.)

# psychopy parameters
path_to_image_circle = "../images/circle.jpg"
path_to_image_triangle = "../images/triangle.jpg"
path_to_image_rectangle = "../images/rectangle.jpg"
shapes = [path_to_image_rectangle, path_to_image_triangle, path_to_image_circle]

# matplotlib parameters
# circle = mpimg.imread("../images/colorful_shapes/circle.jpg")
# triangle = mpimg.imread("../images/colorful_shapes/triangle.jpg")
# square = mpimg.imread("../images/colorful_shapes/rectangle.jpg")
# shapes = [square, triangle, circle]

target_ratio = 7  # (percentage of the oddball onsets)
trials_N = 1  # (number of trials per block) -  at least 200
blocks_N = 2  # (number of blocks)
targetAppearances = trials_N / target_ratio  # (number of times target appear per block)
marker_types = ["baseLine", "target", "distractor"]
durationAfterStimuli = 0.4  # look 4 mil sec after the stimuli was shown
durationBeforeStimuli = 0.2  # look 2 mil sec before the stimuli was shown
samplingRate = 125
numOfsamplesToCut = int(samplingRate * (durationBeforeStimuli+durationAfterStimuli))

# date & time
date = datetime.now().strftime("%d_%m_%Y at %I_%M_%S_%p")

# file parameters
EEG_folder_path = "output_files/EEG_Recordings/"
EEG_file_name = "output_files/EEG_Recordings/" + f"EEG_{date}.csv"
markers_folder_path = "output_files/Marker_Recordings/"
markers_psycho_folder_path = "output_files/markerPsycho/"
markers_psycho_file_name = "output_files/markerPsycho/" + f"listOfMarkers_{date}.csv"
markers_file_name = "output_files/Marker_Recordings/" + f"listOfMarkers_{date}.csv"
# markers_file_name_psychopy = "output_files/Marker_Recordings/" + f"listOfMarkers_{date}.psycholog"
allTrialsBaseLine_file_name = "output_files/cut_data_by_class/baseLine/" + f"classBaseLine_{date}.csv"
allTrialsTarget_file_name = "output_files/cut_data_by_class/target/" + f"classTarget_{date}.csv"
allTrialsDistractor_file_name = "output_files/cut_data_by_class/distractor/" + f"classDistractor_{date}.csv"
mean_EEG_BaseLine_folder_path = "output_files/cut_data_by_class/baseLine/Mean_EEG_Signal_BaseLine"
mean_EEG_Target_folder_path = "output_files/cut_data_by_class/target/Mean_EEG_Signal_Target"
mean_EEG_distractor_folder_path = "output_files/cut_data_by_class/distractor/Mean_EEG_Signal_Distractor"
mean_EEG_file_name = f"Mean_EEG_Signal_For_{date}_"


# test name parameters
# EEG_file_name_FORTEST = "output_files/EEG_Recordings/" + f"EEG_test.csv"
# markers_file_name_FORTEST = "output_files/Marker_Recordings/" + f"listOfMarkers_test.csv"

EEG_file_name_FORTEST = "output_files/EEG_Recordings/" + f"EEG_26_12_2022 at 05_34_52_PM_ErezFirstRecord.csv"
markers_file_name_FORTEST = "output_files/Marker_Recordings/" + f"listOfMarkers_26_12_2022 at 05_28_33_PM_ErezFirstRecord_FIXED.csv"

# Filtered_EEG_file_name = "output_files/filtered_EEG_Recordings/" + f"Filtered_EEG_test.csv"
allTrialsBaseLine_file_name_FORTEST = "output_files/cut_data_by_class/baseLine/" + f"classBaseLine_test1.csv"
allTrialsTarget_file_name_FORTEST = "output_files/cut_data_by_class/target/" + f"classTarget_test1.csv"
allTrialsDistractor_file_name_FORTEST = "output_files/cut_data_by_class/distractor/" + f"classDistractor_test1.csv"


# useful functions
def getTheMostUpdatedFile(pathOfFiles):
    # because of the way of saving
    # no need to sort the files
    files = os.listdir(pathOfFiles)
    # check if the last letter is "M" like the "datetime" format
    # example: listOfMarkers_19_12_2022 at 12_12_11_PM.csv file name ends with M
    # if folder doesn't contain file with the specified format return the latest file
    index = len(files) - 1
    removeTypeOfFile = 5
    while index >= 0 and files[index][len(files[index]) - removeTypeOfFile] != "M":
        index -= 1
    if index == -1:
        return files[len(files) - 1]
    return files[index]


def extract_date(file_name):
    # Extract the date from the file name and convert it to a datetime object
    return datetime.strptime(file_name.split('_')[1], "%d_%m_%Y")


global keepRunning
keepRunning = True
