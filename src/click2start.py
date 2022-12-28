import multiprocessing
import lsl_Record_data
import time
if __name__ == '__main__':
    multiprocessing.freeze_support()




import data_extraction_by_class
from threading import Thread






# multiprocessing.freeze_support()
# multiprocessing.set_start_method('fork')


# Create the processes
p1 = multiprocessing.Process(target=lsl_Record_data.main)
p1.start()
time.sleep(10)
import GUI
p2 = multiprocessing.Process(target=GUI.showExperiment)
#
# Start the processes

p2.start()
# GUI.showExperiment()
# Wait for the processes to finish
p2.join()
p1.join()
print("All processes finished")

# t1 = Thread(target=lsl_Record_data.main, args=[])
# t1.start()
# lsl_Record_data.main()
# GUI.showExperiment()
# t1.join()

# data_extraction_by_class.main()

#
# import concurrent.futures
# import time
#
#
#
# # Create a ThreadPoolExecutor with 2 threads
# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     # Submit 2 tasks to the executor
#     task1 = executor.submit(lsl_Record_data.main, [])
#     task2 = executor.submit(GUI.showExperiment, [])
#
#     # Wait for the tasks to complete
#     result1 = task1.result()
#     result2 = task2.result()


# lsl_Record_data.main()


############### using subprocess

# import subprocess
# from functools import partial
#
# record = partial(lsl_Record_data.main())
#
# # Start a process that applies the record function to its input
# p1 = subprocess.Popen(["python", "-c", "print(record())"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#
# show = partial(GUI.showExperiment())
# # Start a process that prints "Goodbye, World!" every 2 seconds
# p2 = subprocess.Popen(["python", "-c", "print(show())"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

# Wait for both processes to complete
# p1.wait()
# p2.wait()
