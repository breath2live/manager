from manager.process import process
import numpy as np
import threading
import time

def func(var):
	time.sleep(np.random.randint(1,10))

def showMe():
	print(process(lambda:None).processlist)
	threading.Timer(0.2, showMe).start()


threading.Timer(0.2, showMe).start()


# start
obj = []
for item in range(0,10):
	obj.append(process(func, item).start())
