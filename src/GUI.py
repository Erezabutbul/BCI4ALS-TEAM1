from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
import pylsl
from matplotlib.pyplot import figure
# %matplotlib auto
import lsl_Record_data
from runExperiment import generated_experiment
import parameters as p
import pylsl
import random
import keyboard
from shutil import move


class Timer:
    def getTime(self):
        return pylsl.local_clock()


def showExperiment():
    interTime = p.interTime  # take from parameters
    StimOnset = p.StimOnset
    faces = p.faces
    stimulusType = p.stimulusType
    win = visual.Window(fullscr=True, autoLog=False)

    ###########################################################
    # save to "EXP_{date}" directory
    markers_dir = exp_path + p.markers_psycho_folder_path
    os.makedirs(markers_dir, exist_ok=True)
    ###########################################################

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
        baseline = 0
        target, distractor = random.sample(range(1, 3), 2)

        # sounds
        # baseline_sound = sound.Sound('A', octave=5, sampleRate=44100, secs=0.1, bits=8)
        # target_sound = sound.Sound('B', octave=6, sampleRate=44100, secs=0.1, bits=8)
        # distractor_sound = sound.Sound('C', octave=7, sampleRate=44100, secs=0.1, bits=8)

        baseline_sound = sound.Sound(p.sounds[baseline])
        target_sound = sound.Sound(p.sounds[target])
        distractor_sound = sound.Sound(p.sounds[distractor])

        # images
        baseline_image = visual.ImageStim(win, image=faces[baseline], autoLog=False)
        target_image = visual.ImageStim(win, image=faces[target], autoLog=False)
        distractor_image = visual.ImageStim(win, image=faces[distractor], autoLog=False)

        if state == "train":
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
        curr_data["timeStamp"] = pylsl.local_clock()
        curr_data["description"] = "start_of_Block_number " + str(indexOfBlock)
        timeStampAndShapes.append(curr_data)

        win.logOnFlip(level=logging.EXP, msg="startBlock")  # here we are logging the time
        win.flip()
        # go through current block
        for i in currentBlock:
            if i == 0:
                plt.axis('off')
                plt.imshow(shapes[baseline])
                plt.show()
                # write the timestamp of baseline
                print("writing baseline and the baseline is " + shapeStrings[baseline])
                curr_data["timeStamp"] = pylsl.local_clock()
                curr_data["description"] = "baseLine"
                plt.pause(StimOnset)
                plt.clf()
                plt.pause(interTime)
            elif i == 1:
                plt.axis('off')
                plt.imshow(shapes[target])
                plt.show()
                print("writing target and the target is " + shapeStrings[target])
                curr_data["timeStamp"] = pylsl.local_clock()
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
                curr_data["timeStamp"] = pylsl.local_clock()
                curr_data["description"] = "distractor"
                plt.pause(StimOnset)
                plt.clf()
                plt.pause(interTime)
            timeStampAndShapes.append(curr_data)

    file = pd.DataFrame(timeStampAndShapes)
    file.to_csv(p.markers_file_name, index=True, index_label="index", encoding="utf_8_sig")
    plt.close()
    p.keepRunning = False
