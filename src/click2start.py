import multiprocessing
import time

import runExperiment
import lsl_Record_data
import GUI
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import pylsl

def expTry():
    timeStampAndShapes = list()
    shapes = [0, 1, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 1, 2, 1, 1, 1, 0, 0]
    for i in shapes:
        print(i)
        timeStampAndShapes.append([pylsl.local_clock(), i])
        time.sleep(0.5)


def expTry2():
    timeStampAndShapes = list()
    shapes = [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
    for i in shapes:
        print(i)
        timeStampAndShapes.append([pylsl.local_clock(), i])
        time.sleep(0.5)



t1 = Thread(target=lsl_Record_data.main, args=[])
t1.start()
GUI.showExperiment()

# t2 = Thread(target=GUI.showExperiment, args=[])
# t2.start()
t1.join()
# t2.join()


# t2 = Thread(expTry())
# t2.start()
# lsl_Record_data.main()

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