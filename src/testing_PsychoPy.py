from psychopy import visual, core
import numpy as np
import pylsl
import lsl_Record_data
from runExperiment import generated_experiment
import parameters as p
import time
import pandas as pd
import pylsl
import random
import keyboard

def showExperiment():
    interTime = p.interTime  # take from parameters
    StimOnset = p.StimOnset

    shapes = p.shapes
    shapeStrings = p.stimulusType

    win = visual.Window(fullscr=True)
    # win = visual.Window([400,400]) in case we want a window of given size
    message = visual.TextStim(win, text='Welcome')
    message.draw()
    win.flip()
    core.wait(2.0)

    # will save the time stamps and the shape according to the order of appearance
    timeStampAndShapes = list()

    for indexOfBlock in range(0, p.blocks_N):
        # get current block
        currentBlock = generated_experiment[indexOfBlock]

        # generating new order for target,non target,distractor
        baseline, target, distractor = random.sample(range(0, 3), 3)

        # plot to audience
        message.text = "Please focus on the {}".format(shapeStrings[target])  # Change properties of existing stim
        message.draw()
        win.flip()
        core.wait(2.0)
        # keyboard.wait(' ')
        print("___________ starting new block _________________")
        print("the length of this block is " + str(len(currentBlock)))
        curr_data = dict()
        curr_data["timeStamp"] = pylsl.local_clock()
        curr_data["description"] = "start_of_Block_number " + str(indexOfBlock)
        timeStampAndShapes.append(curr_data)

        # go through current block
        for i in currentBlock:
            curr_data = dict()
            if i == 0:
                shape_image = visual.ImageStim(win, image=shapes[baseline])
                shape_image.draw()
                win.flip()
                # write the timestamp of baseline
                print("writing baseline and the baseline is " + shapeStrings[baseline])
                curr_data["timeStamp"] = pylsl.local_clock()
                curr_data["description"] = "baseLine"
                core.wait(StimOnset)
                message.text = " "
                win.flip()
                core.wait(StimOnset)
            elif i == 1:
                shape_image = visual.ImageStim(win, image=shapes[target])
                shape_image.draw()
                win.flip()
                # write the timestamp of target
                print("writing target and the target is " + shapeStrings[target])
                curr_data["timeStamp"] = pylsl.local_clock()
                curr_data["description"] = "target"
                core.wait(StimOnset)
                message.text = " "
                win.flip()
                core.wait(StimOnset)
            elif i == 2:
                shape_image = visual.ImageStim(win, image=shapes[distractor])
                shape_image.draw()
                win.flip()
                # write the timestamp of distractor
                print("writing distractor and the distractor is " + shapeStrings[distractor])
                curr_data["timeStamp"] = pylsl.local_clock()
                curr_data["description"] = "distractor"
                core.wait(StimOnset)
                message.text = " "
                win.flip()
                core.wait(StimOnset)
            timeStampAndShapes.append(curr_data)

    file = pd.DataFrame(timeStampAndShapes)
    file.to_csv(p.markers_file_name)
    p.keepRunning = False


