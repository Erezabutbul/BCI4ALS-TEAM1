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
rectangle = mpimg.imread("../images/rectangle.jpg")
shapes = [rectangle, triangle, circle]

targetAppearances = 1 # (how many time each target will show)
target_ratio = 7  # (percentage of the oddball onsets)
trials_N = targetAppearances * target_ratio  # (number of trials per block)

blocks_N = 4  # (number of blocks)

date = datetime.now().strftime("%d_%m_%Y at %I_%M_%S_%p")

EEG_file_name = "output_files/Marker_Recordings/" + f"EEG {date}"
markers_file_name = "output_files/Marker_Recordings/" + f"listOfMarkers {date}.csv"


# # trial_len = int(1 / target_ratio)
# target_image_path = "..\images\logo.png"
# nontarget_image_path = "..\images\\arrows.png"
#
# # Images
#
# target_i = plt.imread(target_image_path) # Load images (or any other stimulus type per target)
# nontarget = plt.imread(nontarget_image_path)


