from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
import pylsl
from matplotlib.pyplot import figure
# %matplotlib auto
import lsl_Record_data
from runExperiment import generated_experiment
import parameters as p
import time
import pandas as pd
import pylsl
import random
import keyboard


# from psychoPY


def showExperiment():
    interTime = p.interTime  # take from parameters
    StimOnset = p.StimOnset

    shapes = p.shapes
    shapeStrings = p.stimulusType

    figure(figsize=(8, 6), dpi=80)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.text(0.5, 0.5, "Welcome", fontsize=50, horizontalalignment='center')
    plt.axis('off')
    plt.pause(2)
    plt.clf()
    plt.ion()  # added for correctness

    # will save the time stamps and the shape according to the order of appearance
    timeStampAndShapes = list()

    for indexOfBlock in range(0, p.blocks_N):
        # get current block
        currentBlock = generated_experiment[indexOfBlock]

        # generating new order for target,non target,distractor
        baseline, target, distractor = random.sample(range(0, 3), 3)

        # plot to audience
        plt.text(0.5, 0.5, "Please focus on the {}".format(shapeStrings[target]), fontsize=50,
                 horizontalalignment='center')
        plt.axis('off')
        plt.pause(2)
        plt.clf()
        # keyboard.wait(' ')
        print("___________ starting new block _________________")
        print("the length of this block is " + str(len(currentBlock)))
        curr_data = dict()
        curr_data["time stamp"] = pylsl.local_clock()
        curr_data["description"] = "start of Block number " + str(indexOfBlock)
        timeStampAndShapes.append(curr_data)

        # go through current block
        for i in currentBlock:
            curr_data = dict()
            if i == 0:
                plt.axis('off')
                plt.imshow(shapes[baseline])
                plt.show()
                # write the timestamp of baseline
                print("writing baseline and the baseline is " + shapeStrings[baseline])
                curr_data["time stamp"] = pylsl.local_clock()
                curr_data["description"] = "base line"
                plt.pause(StimOnset)
                plt.clf()
                plt.pause(interTime)
            elif i == 1:
                plt.axis('off')
                plt.imshow(shapes[target])
                plt.show()
                print("writing target and the target is " + shapeStrings[target])
                curr_data["time stamp"] = pylsl.local_clock()
                curr_data["description"] = "target"
                plt.pause(StimOnset)
                plt.clf()
                plt.pause(interTime)
            elif i == 2:
                plt.axis('off')
                plt.imshow(shapes[distractor])
                plt.show()
                # write the timestamp of distractor
                print("writing distractor and the distractor is " + shapeStrings[distractor])
                curr_data["time stamp"] = pylsl.local_clock()
                curr_data["description"] = "distractor"
                plt.pause(StimOnset)
                plt.clf()
                plt.pause(interTime)
            timeStampAndShapes.append(curr_data)

    file = pd.DataFrame(timeStampAndShapes)
    file.to_csv(p.markers_file_name)
    plt.close()
    p.keepRunning = False
