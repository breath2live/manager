import threading
import time
import numpy as np



class manager():
	def __init__(self):
		self.tasklist = []

	def start(self):
		pass

	def stop(self):
		pass

	def append(self, task :process):
		return self.tasklist.append(task)
