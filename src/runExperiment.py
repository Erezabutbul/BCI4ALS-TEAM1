import random

from parameters import *


# Generate Experiment - returns the trials / test order

def generateExperiment():
    experiment = list()
    for i in range(0, blocks_N):
        experiment.append(generateBlock())
    return experiment


####### ****NEW**** Generate Block
# does not provide baseline after target or distractor
def generateBlock():
    block = list()

    for i in range(trials_N):
        r = random.randint(1, trials_N)
        if 1 <= r <= targetAppearances:
            block.append(1)
<<<<<<< HEAD
=======
            t = t + 1
>>>>>>> 5af68f5 (erez's version)
        elif targetAppearances < r <= 2 * targetAppearances:
            block.append(2)
        else:
            block.append(0)
    return block


# Generate Trial
#   get the trial shape based on the probability and target ratio
def generated_trial():
    rNum = random.randint(1, target_ratio - targets_N)  # corrects the target ratio
    if 1 <= rNum <= targets_N:
        return rNum
    return 0


# for b in range(p.blocks_N):
#     generated_block = generateBlock(p.trials_N,p.target_ratio,p.targets_N)
#     print(generated_block)
#     print("________________________________________")
#     print("________________________________________")
#     print("________________________________________")
generated_experiment = generateExperiment()

# for i in range(0,len(generated_experiment)):
#     print(generated_experiment[i])
#     print("_________ next block _____________")
