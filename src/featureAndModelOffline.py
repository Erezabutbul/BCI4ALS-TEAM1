from featureExtraction import main as featureExtraction_main
from Model import main as model_main
from parameters import *

def main():

    # extract features
    featureExtraction_main("exp_path", modes[0])

    # model TRAIN / TEST
    model_main("exp_path")


if __name__ == '__main__':
    main()