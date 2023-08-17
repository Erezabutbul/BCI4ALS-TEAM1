# import time

# import parameters as p
from runExperiment import generateExperiment
from parameters import *
import random
import keyboard
from shutil import move


class Timer:
    def getTime(self):
        return pylsl.local_clock()

"""
shows experiment
args:
    keepRunning - boolian that changes to false after GUI finishes to indicate the lsl stream to stop
    gui_mode - TRAIN or TEST
    gui_trials - number of trials per block
    gui_blocks - number of blocks
"""
def showExperiment(exp_path, keepRunning, gui_mode, gui_trials, gui_blocks):

    from psychopy import logging, core, visual, sound
    win = visual.Window(fullscr=True, autoLog=False)

    markers_dir = exp_path + markers_psycho_folder_path
    os.makedirs(markers_dir, exist_ok=True)

    fileName = markers_dir + "/" + markers_psycho_file_name
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

    generated_experiment = generateExperiment(gui_trials , gui_blocks)

    for indexOfBlock in range(0, gui_blocks):
        # get current block
        currentBlock = generated_experiment[indexOfBlock]


        # generating new order for target,non target,distractor
        baseline = 0
        target, distractor = random.sample(range(1, 3), 2)


        # baseline_sound = sound.Sound(sounds[baseline])  -  activate if a sound for baseline is wanted
        target_sound = sound.Sound(sounds[target])
        distractor_sound = sound.Sound(sounds[distractor])

        # images
        baseline_image = visual.ImageStim(win, image=faces[baseline], autoLog=False)
        target_image = visual.ImageStim(win, image=faces[target], autoLog=False)
        distractor_image = visual.ImageStim(win, image=faces[distractor], autoLog=False)

        if gui_mode == "TRAIN":
        # plot to audience
            message.text = "Please focus on the {}".format(stimulusType[target])  # Change properties of existing stim
            message.draw()
            win.flip()
        else:
            message.text = "Please focus on \n {}".format(stimulusType[target] + " for YES\n OR \n" + stimulusType[
                distractor] + " for NO")  # Change properties of existing stim
            message.draw()
            win.flip()
            core.wait(4)
            message.text = "YES - {}".format(stimulusType[target]) + " with first sound \nNO - {} with second sound \n".format(stimulusType[distractor])
            message.draw()
            win.flip()
            core.wait(waitBetweenSounds)
            target_sound.play()
            core.wait(waitBetweenSounds)
            distractor_sound.play()
            # Open the file in write mode
            file = open(exp_path + "/pics_allocation.txt", "w")

            # Write content to the file
            file.write(f"condition1 is {target}: \n")
            file.write(stimulusType[target])
            file.write(f"\ncondition2 is {distractor}: \n")
            file.write(stimulusType[distractor])

            # Close the file
            file.close()

        # keyboard.wait(' ')
        core.wait(3)
        print("___________ starting new block _________________")
        print("the length of this block is " + str(len(currentBlock)))

        win.logOnFlip(level=logging.EXP, msg="startBlock")  # here we are logging the time
        win.flip()

        # go through current block
        for i in currentBlock:
            if i == 0:
                baseline_image.draw()
                # baseline_sound.play()
                win.logOnFlip(level=logging.EXP, msg="baseLine")  # here we are logging the time
                win.flip()
                # write the timestamp of baseline
                print("writing baseline and the baseline is " + stimulusType[baseline])
                core.wait(StimOnset)
                win.flip()
                core.wait(StimOnset)
            elif i == 1:
                target_image.draw()
                target_sound.play()
                win.logOnFlip(level=logging.EXP, msg="target")  # here we are logging the time
                win.flip()
                # write the timestamp of target
                print("writing target and the target is " + stimulusType[target])
                core.wait(StimOnset)
                win.flip()
                core.wait(StimOnset)
            elif i == 2:
                distractor_image.draw()
                distractor_sound.play()
                win.logOnFlip(level=logging.EXP, msg="distractor")  # here we are logging the time
                win.flip()
                # write the timestamp of distractor
                print("writing distractor and the distractor is " + stimulusType[distractor])
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
