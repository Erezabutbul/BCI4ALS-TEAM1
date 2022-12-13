
import lsl_Record_data
import GUI

from threading import Thread


t1 = Thread(target=lsl_Record_data.main, args=[])
t1.start()
GUI.showExperiment()


