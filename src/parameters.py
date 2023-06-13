from matplotlib import image as mpimg
from datetime import datetime
import os
import pandas as pd
import pylsl
import numpy as np

#train or test MODE
modes = ["TRAIN", "TEST"]
mode = 0

# Experiment parameters
StimOnset = 0.7  # (time to present the stimulus)
interTime = 0.4  # (time between stimulus)
targets_N = 2  # (number of target stimulus)
waitBetweenSounds = 2 # (introducing the sounds in test condition)

# Define stimulus types and load data
# stimulusType = ["neutral face", "sad face",
#                 "happy face"]  # (type of stimulus to load and present- different pictures\ audio \ etc.)
# nadav's update to gui
stimulusType = ["neutral", "Chochava",
                "Chook Cha"] # (type of stimulus to load and present- different pictures\ audio \ etc.)

# psychopy parameters

# image
path_to_image_neutral = "../images/unknown.png" #"../images/neutral_face.jpg"
path_to_image_happy = "../images/chookcha1.png"# "../images/happy_face.jpg"
path_to_image_sad = "../images/chohava3.png" #"../images/sad_face.jpg"

faces = [path_to_image_neutral, path_to_image_sad, path_to_image_happy]

# sound
# normal_path = "../sounds/ding1.mp3"
# major_path = "../sounds/ding1.mp3"
# minor_path = "../sounds/ding2.mp3"
# sounds = [normal_path, minor_path, major_path]

neutral_path = ""
cat_sound_path = "../sounds/cat.wav"
dog_sound__path = "../sounds/dog.wav"

sounds = [neutral_path, cat_sound_path, dog_sound__path]

target_ratio = 7  # (percentage of the oddball onsets)
trials_N = 50  # (number of trials per block) -  at least 200
blocks_N = 1  # (number of blocks)
targetAppearances = trials_N / target_ratio  # (number of times target appear per block)
marker_types = ["baseLine", "target", "distractor"]
durationAfterStimuli = 0.6  # look 6 mil sec after the stimuli was shown
durationBeforeStimuli = -0.2  # look 4 mil sec before the stimuli was shown
samplingRate = 125
numOfSamplesToCut = int(samplingRate * (durationBeforeStimuli + durationAfterStimuli))

# selected electrodes for features extractions
# selected_channels = ['C3', 'C4', 'Cz', 'FC1', 'FC2', 'FC5', 'FC6'] BEST SCORE 5/7 - 21.5.23
selected_channels = ['Cz', 'FC1', 'FC2', 'CP1', 'CP2']

# date & time
# date = datetime.now().strftime("%d_%m_%Y at %I_%M_%S_%p")

# file parameters
output_files = "output_files/"

EEG_file_name = "EEG_Recording_unprocessed.csv"
EEG_folder_path = "EEG_Recordings/"
markers_psycho_file_name = f"listOfMarkers_before_parse.csv"
markers_psycho_folder_path = "markerPsychoBeforeParse/"
markers_arranged_file_name = f"listOfMarkers_after_parse.csv"
markers_arranged_folder_path = "markerPsychoAfterParse/"
Filtered_EEG_file_name = f"EEG_Recording_processed.csv"
filtered_EEG_folder_path = "filtered_EEG_Recordings/"

allClasses = "cut_data_by_class/"
allTrialsBaseLine_file_name = "classbaseLine.csv"
allTrialsBaseLine_folder_path = "cut_data_by_class/baseLine/"
allTrialsTarget_file_name = "classtarget.csv"
allTrialsTarget_folder_path = "cut_data_by_class/target/"
allTrialsDistractor_file_name = "classdistractor.csv"
allTrialsDistractor_folder_path = "cut_data_by_class/distractor/"

mean_EEG_baseLine_folder_path = "Mean_EEG_Signal_baseLine/"
mean_EEG_target_folder_path = "Mean_EEG_Signal_target/"
mean_EEG_distractor_folder_path = "Mean_EEG_Signal_distractor/"

train_features_folder_name = "features/"
featuresAndModel_folder_name = "featuresAndModel/"
target_train_features_file_name = "target_train_features_Matrix.csv"
distractor_train_features_file_name = "distractor_train_features_Matrix.csv"
target_test_features_file_name = "target_test_features_Matrix.csv"
distractor_test_features_file_name = "distractor_test_train_features_Matrix.csv"
train_model_folder_name = "models/"


test_features_folder_name = "features/"
test_features_file_name = "test_features_Matrix.csv"
label_file_name = "labels.csv"
target_label_file_name = "target_labels.csv"
distractor_label_file_name = "distractor_labels.csv"
num_trails_elecs_conditions_file_name = "num_trails_elecs_conditions.csv"

# Pre Processing Parameters
baseline_min = -0.2
baseline_max = 0
reject_criteria = dict(eeg=200e-6)
bad_channels = ['O1', 'O2']
channel_reject_criteria = 0.3

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


