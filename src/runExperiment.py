import random

import numpy

import parameters as p

#FUNCTIONS



# Generate Experiment
def generateExperiment(blocks_N,trials_N,target_ratio,targets_N):
    experiment = list()
    for i in range(0,blocks_N):
        experiment.append(generateBlock(trials_N,target_ratio,targets_N))
    return experiment


# Generate Block
def generateBlock(trials_N,target_ratio,targets_N):
    block = list()
    block.append(0)  #block starts with 0
    for i in range(0,trials_N):
        t=generated_trial(target_ratio,targets_N)
        if(t!=0): #if target was selected
            block.append(t)
        block.append(0)
    return block



# Generate Trial
#   get the trial shape based on the probability and target ratio
def generated_trial(target_ratio,targets_N):
    rNum = random.randint(1, target_ratio-targets_N)  #corrects the target ratio
    if(1 <= rNum and rNum <= targets_N):
        return rNum
    return 0

# for b in range(p.blocks_N):
#     generated_block = generateBlock(p.trials_N,p.target_ratio,p.targets_N)
#     print(generated_block)
#     print("________________________________________")
#     print("________________________________________")
#     print("________________________________________")
generated_experiment = generateExperiment(p.blocks_N,p.trials_N,p.target_ratio,p.targets_N)
for i in range(0,len(generated_experiment)):
    print(generated_experiment[i])
    print("_________ next block _____________")