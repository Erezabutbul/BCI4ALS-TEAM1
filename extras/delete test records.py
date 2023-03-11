import os
from src.parameters import *

os.remove("../src/" + EEG_file_name)
os.remove("../src/" + markers_file_name)
os.remove("../src/" + Filtered_EEG_file_name)
os.remove("../src/" + allTrialsBaseLine_file_name)
os.remove("../src/" + allTrialsTarget_file_name)
os.remove("../src/" + allTrialsDistractor_file_name)