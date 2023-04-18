import numpy as np

from featureExtraction import main as featureExtraction_main
from Model import main as model_main
from cross_validation import main as cross_validation_main
from parameters import *
import time
import itertools

def main():

    # extract features
    featureExtraction_main("test_29_03_2023 at 04_09_59_PM", modes[1])

    # model TRAIN / TEST
    model_main("test_29_03_2023 at 04_09_59_PM/")


    # rows = list(itertools.combinations(range(13), 5))
    # matrix = [list(row) for row in rows]

    # start_time = time.time()
    # successes = np.zeros(len(matrix))
    # for iter in range(0, len(matrix), 100):
    #     successes[iter] = cross_validation_main(matrix[iter])
    #     if successes[iter] == 10:
    #         break
    # successes = cross_validation_main(matrix[100])
    # print(successes)
    # print(matrix[100])
    # print(max(successes))
    # max_index = successes.argmax()
    # print(max_index)
    # end_time = time.time()
    #
    # runtime = end_time - start_time
    #
    # print(f"Runtime: {runtime:.6f} seconds")



if __name__ == '__main__':
    main()