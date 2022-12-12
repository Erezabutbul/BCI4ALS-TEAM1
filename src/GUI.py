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
#
# from psychoPY

#0 - baseline
#1- target
#2 - distractor


def showExperiment():
    interTime = p.interTime # take from parameters
    StimOnset = p.StimOnset
    circle = mpimg.imread("circle.jpg")
    triangle = mpimg.imread("triangle.jpg")
    rectangle = mpimg.imread("rectangle.jpg")

    baseline = rectangle  # take from parameters
    target = circle
    distractor = triangle

    figure(figsize=(8, 6), dpi=80)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    plt.text(0.5, 0.5, "Welcome", fontsize=50, horizontalalignment='center')
    plt.axis('off')
    plt.pause(2)
    plt.clf()

    plt.ion()

    targets = ['Circle', 'Triangle', 'Circle', 'Triangle', 'Circle', 'Triangle', 'Circle', 'Triangle']
    n_blocks = np.size(generated_experiment)
    for n_block in list(range(0, n_blocks)):
        pos = generated_experiment[n_block]
        plt.text(0.5, 0.5, "Please focus on the {}".format(targets[n_block]), fontsize=50, horizontalalignment='center')
        plt.axis('off')
        plt.pause(2)
        plt.clf()

        timeStampAndShapes = list()
        for i in pos:
            if i == 0:
                plt.axis('off')
                plt.imshow(baseline)
                plt.show()
                # write the timestamp of baseline
                # timeStampAndShapes.append([time.time(), 0])
                timeStampAndShapes.append([pylsl.local_clock(), 0])
                # time.sleep(StimOnset)
                plt.pause(StimOnset)
                plt.clf()
                # time.sleep(interTime)
                plt.pause(interTime)
            elif i == 1:
                plt.axis('off')
                plt.imshow(target)
                plt.show()
                # write the timestamp of target
                # timeStampAndShapes.append([time.time(), 1])
                timeStampAndShapes.append([pylsl.local_clock(), 1])
                # time.sleep(StimOnset)
                plt.pause(StimOnset)
                plt.clf()
                # time.sleep(interTime)
                plt.pause(interTime)
            elif i == 2:
                plt.axis('off')
                plt.imshow(distractor)
                plt.show()
                # write the timestamp of distractor
                # timeStampAndShapes.append([time.time(), 2])
                timeStampAndShapes.append([pylsl.local_clock(), 2])
                # time.sleep(StimOnset)
                plt.pause(StimOnset)
                plt.clf()
                # time.sleep(interTime)
                plt.pause(interTime)
        file = pd.DataFrame(timeStampAndShapes)
        file.to_csv("listOfMarkers.csv")





