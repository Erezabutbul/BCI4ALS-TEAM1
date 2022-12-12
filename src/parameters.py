import matplotlib.pyplot as plt
import numpy as np
# Experiment parameters
StimOnset = 0.7  # (time to present the stimulus)
interTime = 0.2  # (time between stimulus)
targets_N = 2  # (number of target stimulus)
stimulusType = ["square", "triangle",
                "circle"]  # (type of stimulus to load and present- different pictures\ audio \ etc.)
baseline = stimulusType[0]
targetAppearances = 1 # (how many time each target will show)
target_ratio = 7  # (percentage of the oddball onsets)
trials_N = targetAppearances * target_ratio  # (number of trials per block)

blocks_N = 1  # (number of blocks)

# trial_len = int(1 / target_ratio)
target_image_path = "..\images\logo.png"
nontarget_image_path = "..\images\\arrows.png"

# Images

target_i = plt.imread(target_image_path) # Load images (or any other stimulus type per target)
nontarget = plt.imread(nontarget_image_path)


