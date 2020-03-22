from manager.process import process
import threading
import time

def func(var=100):
	print(var)
	time.sleep(5)
	print('end')


process(func, 88).start()

prc = process(func, dstkwargs={'var':12334}, delay=2)
threading.Timer(1, prc.start).start()


while True:
	print(prc.status.name, prc.processlist)
	time.sleep(0.2)
