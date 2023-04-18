from featureExtraction import main as featureExtraction_main
from Model import main as model_main
from parameters import *

def main():

    # extract features
    # featureExtraction_main("exp_path", modes[0])

    # model TRAIN / TEST
    model_main("test_29_03_2023 at 04_09_59_PM/")


if __name__ == '__main__':
    main()