import time

import lsl_Record_data
import GUI
import data_match_and_merge
from threading import Thread


t1 = Thread(target=lsl_Record_data.main, args=[])
t1.start()
GUI.showExperiment()
t1.join()

data_match_and_merge.main()
