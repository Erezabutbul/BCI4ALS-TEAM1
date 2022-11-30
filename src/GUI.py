from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import numpy as np
#import time
from matplotlib.pyplot import figure
%matplotlib auto

from runExperiment import generated_experiment 

#0 - baseline
#1- target
#2 - distractor

interTime = 0.2
StimOnset = 0.7
 
circle = mpimg.imread("circle.jpg")
triangle = mpimg.imread("triangle.jpg")
rectangle = mpimg.imread("rectangle.jpg")

baseline = rectangle
target = circle
distractor = triangle

figure(figsize=(8, 6), dpi=80)
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.text(0.5,0.5,"Welcome",fontsize=50,horizontalalignment='center')
plt.axis('off')
plt.pause(2)
plt.clf()

targets = ['Circle','Triangle','Circle','Triangle','Circle','Triangle','Circle','Triangle']
n_blocks = np.size(generated_experiment)
for n_block in list(range(0, n_blocks)):
    pos = generated_experiment[n_block]
    plt.text(0.5,0.5,"Please focus on the {}".format(targets[n_block]),fontsize=50,horizontalalignment='center')
    plt.axis('off')
    plt.pause(2)
    plt.clf()
    for i in pos:
        if i == 0:
            plt.axis('off')
            plt.imshow(baseline)
            plt.show()
            plt.pause(StimOnset)
            plt.clf()
            plt.pause(interTime)
        elif i == 1:
            plt.axis('off')
            plt.imshow(target)
            plt.show()
            plt.pause(StimOnset)
            plt.clf()
            plt.pause(interTime)
        elif i == 2:
            plt.axis('off')
            plt.imshow(distractor)
            plt.show()
            plt.pause(StimOnset)
            plt.clf()
            plt.pause(interTime)
