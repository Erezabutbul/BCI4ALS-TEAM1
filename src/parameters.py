import matplotlib.pyplot as plt
import numpy as np
# Experiment parameters
StimOnset = 1  # (time to present the stimulus)
interTime = 1  # (time between stimulus)
targets_N = 3  # (number of target stimulus)
stimulusType = ["square", "triangle",
                "circle"]  # (type of stimulus to load and present- different pictures\ audio \ etc.)
blocks_N = 80  # (number of blocks)
trials_N = 8  # (number of trials per block)
target_ratio = 1 / 7  # (percentage of the oddball onsets)
trial_len = int(1 / target_ratio)
target_image_path = "..\images\logo.png"
nontarget_image_path = "..\images\\arrows.png"

# Images

target_i = plt.imread(target_image_path) # Load images (or any other stimulus type per target)
nontarget = plt.imread(nontarget_image_path)


