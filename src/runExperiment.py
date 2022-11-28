import random

import numpy

import parameters as p

#FUNCTIONS

# Generate Block
def generateBlock(trials_N, trial_len):
    block = list()
    block.append(generated_trial(trial_len))
    return block

# Generate Trial
def generated_trial(trial_len):
    trial = numpy.zeros(trial_len)
    rIndex = random.randrange(1, trial_len)
    trial[rIndex] = 1
    return trial

for b in range(p.blocks_N):
    generated_block = generateBlock(p.trials_N,p.trial_len)
    print(generated_block)
    print("________________________________________")
    print("________________________________________")
    print("________________________________________")