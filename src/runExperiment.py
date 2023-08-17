import random

import numpy as np
#
# from parameters import *

"""
Generate Experiment - returns the trials / test order
"""
def generateExperiment(Trials_num, blocks_Num):

    experiment = list()
    for i in range(0, blocks_Num):
        experiment.append(generateBlock(Trials_num))
    return experiment

"""
provide baseline after target or distractor
"""
def generateBlock(Trials_num):
    
    ones = Trials_num // 7
    twos = Trials_num // 7
    zeros = (5 * Trials_num) // 7

    # extream cases
    if ones + twos > zeros:
        zeros = ones + twos

    # Generate an array of zeros and insert ones and twos randomly
    block = [0] * Trials_num
    while ones != 0:
        index = random.randint(1, Trials_num - 2)
        if block[index] == 0 and block[index - 1] == 0 and block[index + 1] == 0:
            block[index] = 1
            ones -= 1
    while twos != 0:
        index = random.randint(1, Trials_num - 2)
        if block[index] == 0 and block[index - 1] == 0 and block[index + 1] == 0:
            block[index] = 2
            twos -= 1

    return block

