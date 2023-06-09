import pandas as pd
import numpy as np


# a file that was made in order to enable a quick concat and creation of new and relevant features_matrix
def main():
    feature_folder_path = "../src/output_files/featuresAndModel/features/"
    outputDf_target = pd.read_csv(feature_folder_path + f"Features_target.csv", index_col=[0, 1])
    # outputDf_target = outputDf_target.drop(outputDf_target.columns[0], axis=1)
    # outputDf_target = outputDf_target[1:]
    outputDf_target.to_csv(feature_folder_path + f"Features_target_test.csv", header=False, index=False)
    outputDf_distractor = pd.read_csv(feature_folder_path + f"Features_distractor.csv", index_col=[0, 1])
    # outputDf_distractor = outputDf_distractor.drop(outputDf_target.columns[0], axis=1)
    # outputDf_distractor = outputDf_distractor[1:]
    outputDf_distractor.to_csv(feature_folder_path + f"Features_distractor_test.csv", header=False, index=False)

    # create labels vector
    num_target = outputDf_target.shape[0]
    num_distractor = outputDf_distractor.shape[0]
    labels_vec = np.concatenate((np.ones(num_target), np.zeros(num_distractor)))
    np.savetxt(feature_folder_path + f"labels_vector_test.csv", labels_vec, delimiter=",")
    finalFeatureMatrix = pd.concat([outputDf_target, outputDf_distractor])
    finalFeatureMatrix.to_csv(feature_folder_path + f"features_matrix.csv", header=False, index=False)

    # Load CSV file using genfromtxt
    # data = np.genfromtxt(feature_folder_path + f"features_matrix.csv", delimiter=',')
    # Save the NumPy array to a file in the libsvm format
    # dump_svmlight_file(data[:, 1:], data[:, 0], 'features_matrix_for_model.libsvm')

    # Load the saved file into a new NumPy array
    # new_data = np.genfromtxt('features_matrix_for_model.libsvm', comments='#')




if __name__ == '__main__':
    main()