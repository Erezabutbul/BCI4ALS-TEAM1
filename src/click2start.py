import multiprocessing
import time

import runExperiment
import lsl_Record_data
import GUI
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import pylsl




# t1 = Thread(target=lsl_Record_data.main, args=[])
# t1.start()
GUI.showExperiment()

# t2 = Thread(target=GUI.showExperiment, args=[])
# t2.start()
# t1.join()
# t2.join()



# executor = ThreadPoolExecutor(max_workers=3)
# executor.submit(lsl_Record_data.main())
# GUI.showExperiment()
# executor.submit(GUI.showExperiment())

# executor = ThreadPoolExecutor(max_workers=3)
# executor.submit(target=expTry)
# executor.submit(target=expTry2)


# t1 = Thread(target=expTry,args=[])
# t1.start()
#
# t2 = Thread(target=expTry2,args=[])
# t2.start()
#
# t1.join()
# t2.join()