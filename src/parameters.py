from matplotlib import image as mpimg
from datetime import datetime

# Experiment parameters
StimOnset = 0.7  # (time to present the stimulus)
interTime = 0.2  # (time between stimulus)
targets_N = 2  # (number of target stimulus)

# Define stimulus types and load data
stimulusType = ["square", "triangle",
                "circle"]  # (type of stimulus to load and present- different pictures\ audio \ etc.)

path_to_image_circle = "../images/circle.jpg"
path_to_image_triangle = "../images/triangle.jpg"
path_to_image_rectangle = "../images/rectangle.jpg"
shapes = [path_to_image_circle, path_to_image_triangle, path_to_image_rectangle]


target_ratio = 7  # (percentage of the oddball onsets)
trials_N = 200  # (number of trials per block)
blocks_N = 1  # (number of blocks)
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
allTrialsBaseLine_file_name = "output_files/cut_data_by_class/baseLine/" + f"classBaseLine_testGPT.csv"
allTrialsTarget_file_name = "output_files/cut_data_by_class/target/" + f"classTarget_test1GPT.csv"
allTrialsDistractor_file_name = "output_files/cut_data_by_class/distractor/" + f"classDistractor_test1GPT.csv"

global keepRunning
keepRunning = True



