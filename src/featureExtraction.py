from dict2Mat import main as dict2Mat_main
import os
from parameters import *
import pandas as pd
import numpy as np


def main(state):
    # get all the experiment folders
    main_folder = "output_files"
    # TODO - add path for test condition
    # save test condition in the exp_path folder : 'currTest/features/'
    exp_folders = [f for f in os.listdir(main_folder) if
                   os.path.isdir(os.path.join(main_folder, f)) and f.startswith('EXP')]

    # extract trial by class for each experiment
    for exp_num in range(len(exp_folders)):
        exp_path = "output_files/" + exp_folders[exp_num]
        dict2Mat_main(exp_path)

    outputDf_target = pd.DataFrame()
    outputDf_distractor = pd.DataFrame()
    # for each experiment, per class, concatenate all trials
    for exp_num in range(len(exp_folders)):
        exp_path = "output_files/" + exp_folders[exp_num]

        for marker_type in marker_types:
            folder_path = exp_path + f"/cut_data_by_class/{marker_type}/Trial_EEG_Signal_{marker_type}/"
            trial_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

            outputDf_exp = pd.DataFrame()
            for trial in range(len(trial_files)):
                trial_path = folder_path + trial_files[trial]
                currDf = pd.read_csv(trial_path)
                # TODO - trial and electrode rejection
                outputDf_exp = pd.concat([outputDf_exp, currDf])

            outputDf_exp.to_csv(folder_path + f"All_Trials_{marker_type}.csv")

            if state == 'train':
                # for each class concatenate trials for all EXP
                if marker_type == 'target':
                    outputDf_target = pd.concat([outputDf_target, outputDf_exp])
                if marker_type == 'distractor':
                    outputDf_distractor = pd.concat([outputDf_distractor, outputDf_exp])

    if state == 'train':
        # save features matrix for all EXP available
        features_path = "output_files/featuresAndModel/features/"
        outputDf_target.to_csv(features_path + f"Features_target.csv")
        outputDf_distractor.to_csv(features_path + f"Features_distractor.csv")

        # create labels vector
        num_target = outputDf_target.shape[0]
        num_distractor = outputDf_distractor.shape[0]
        labels_vec = np.concatenate((np.ones(num_target), np.zeros(num_distractor)))
        np.savetxt(features_path + f"labels_vector.csv", labels_vec, delimiter=",")
        outputDf = pd.concat([outputDf_target, outputDf_distractor])
        outputDf.to_csv(features_path + f"features_matrix.csv")



if __name__ == '__main__':
    main()
