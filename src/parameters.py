from matplotlib import image as mpimg
from datetime import datetime

# Experiment parameters
StimOnset = 0.7  # (time to present the stimulus)
interTime = 0.2  # (time between stimulus)
targets_N = 2  # (number of target stimulus)

# Define stimulus types and load data
stimulusType = ["square", "triangle",
                "circle"]  # (type of stimulus to load and present- different pictures\ audio \ etc.)
circle = mpimg.imread("../images/circle.jpg")
triangle = mpimg.imread("../images/triangle.jpg")
square = mpimg.imread("../images/rectangle.jpg")
shapes = [square, triangle, circle]

targetAppearances = 1 # (how many time each target will show)
target_ratio = 7  # (percentage of the oddball onsets)
trials_N = targetAppearances * target_ratio  # (number of trials per block)

blocks_N = 4  # (number of blocks)

date = datetime.now().strftime("%d_%m_%Y at %I_%M_%S_%p")
# EEG_file_name = "output_files/EEG_Recordings/" + f"EEG {date}.csv"
EEG_file_name = "output_files/EEG_Recordings/" + f"EEG_test.csv"
markers_file_name = "output_files/Marker_Recordings/" + f"listOfMarkers_test.csv"
# markers_file_name = "output_files/Marker_Recordings/" + f"listOfMarkers {date}.csv"

allTrialsBaseLine_file_name = "output_files/cut_data_by_class/baseLine/" + f"classBaseLine {date}.csv"
allTrialsTarget_file_name = "output_files/cut_data_by_class/target/" + f"classTarget {date}.csv"
allTrialsDistractor_file_name = "output_files/cut_data_by_class/distractor/" + f"classDistractor {date}.csv"

global keepRunning
keepRunning = True



