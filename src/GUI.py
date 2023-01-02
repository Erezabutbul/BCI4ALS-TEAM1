import os
from psychopy import logging, core, visual
from runExperiment import generated_experiment
import parameters as p
import pylsl
import random
import keyboard
from shutil import move


class Timer:
    def getTime(self):
        return pylsl.local_clock()


def showExperiment(exp_path, keepRunning):
    # fileName = p.markers_file_name_psychopy

    interTime = p.interTime  # take from parameters
    StimOnset = p.StimOnset

    shapes = p.shapes
    shapeStrings = p.stimulusType

    win = visual.Window(fullscr=True, autoLog=False)

    # Set up the logger
    ###########################################################
    # save to "EXP_{date}" directory
    markers_dir = exp_path + p.markers_psycho_folder_path
    os.makedirs(markers_dir, exist_ok=True)
    ###########################################################

    fileName = markers_dir + "/" + p.markers_psycho_file_name
    # fileName = p.markers_psycho_file_name
    logfile = open(fileName, 'w')
    log = logging.LogFile(fileName, level=logging.EXP, filemode='w')
    studyClock = Timer()
    logging.setDefaultClock(studyClock)  # this is the logger

    win.logOnFlip(level=logging.EXP, msg="START")
    win.flip()
    # win = visual.Window([400, 400], autoLog=False)  # in case we want a window of given size
    message = visual.TextStim(win, text='Welcome', autoLog=False)
    message.draw()
    win.flip()
    core.wait(interTime)

    for indexOfBlock in range(0, p.blocks_N):
        # get current block
        currentBlock = generated_experiment[indexOfBlock]

        # generating new order for target,non target,distractor
        baseline, target, distractor = random.sample(range(0, 3), 3)

        # plot to audience
        message.text = "Please focus on the {}".format(shapeStrings[target])  # Change properties of existing stim
        message.draw()
        win.flip()
        core.wait(interTime)
        keyboard.wait(' ')
        print("___________ starting new block _________________")
        print("the length of this block is " + str(len(currentBlock)))

        win.logOnFlip(level=logging.EXP, msg="startBlock")  # here we are logging the time
        win.flip()
        # go through current block
        for i in currentBlock:
            if i == 0:
                shape_image = visual.ImageStim(win, image=shapes[baseline], autoLog=False)
                shape_image.draw()
                win.logOnFlip(level=logging.EXP, msg="baseLine")  # here we are logging the time
                win.flip()
                # write the timestamp of baseline
                print("writing baseline and the baseline is " + shapeStrings[baseline])
                core.wait(StimOnset)
                win.flip()
                core.wait(StimOnset)
            elif i == 1:
                shape_image = visual.ImageStim(win, image=shapes[target], autoLog=False)
                shape_image.draw()
                win.logOnFlip(level=logging.EXP, msg="target")  # here we are logging the time
                win.flip()
                # write the timestamp of target
                print("writing target and the target is " + shapeStrings[target])
                core.wait(StimOnset)
                win.flip()
                core.wait(StimOnset)
            elif i == 2:
                shape_image = visual.ImageStim(win, image=shapes[distractor], autoLog=False)
                shape_image.draw()
                win.logOnFlip(level=logging.EXP, msg="distractor")  # here we are logging the time
                win.flip()
                # write the timestamp of distractor
                print("writing distractor and the distractor is " + shapeStrings[distractor])
                core.wait(StimOnset)
                win.flip()
                core.wait(StimOnset)

    logging.flush()
    logfile.close()
    # end the recording
    keepRunning.value = False
    # win.close()
    # core.quit()

if __name__ == '__main__':
    showExperiment()
