import numpy as np
import threading
import ctypes
import enum

class status(enum.Enum):
	idle = 0
	running = 1
	done = 2
	delaying = 3


class process(threading.Thread):
	processlist = []
	__maxIdNumber = 10**10

	def __init__(self, target, *args, **kwargs):
		dstkwargs = kwargs.get('dstkwargs')
		threading.Thread.__init__(self, target=target, args=args, kwargs=dstkwargs)
		self._stop_event = threading.Event()
		kw = {
			'name' : self.getname(),
			'target' : target,
			'args' : [],
			'dstkwargs' : {},
			'priority' : 1000,
			'delay' : 0,
			'status' : status.idle,
			'thread' : None
		}
		for key, value in kw.items():
			if key in kwargs: setattr(self, key, kwargs[key])
			else: setattr(self, key, value)

	def __del__(self):
		return self.rmname()

	def __str__(self):
		return '<process object>, name={}, callback={}, fargs={}, fkwargs={}'.format(self.id, self.callback, self.args, self.kwargs)

	def getname(self):
		while True:
			new = np.random.randint(np.random.randint(self.__maxIdNumber, self.__maxIdNumber*10-1))
			if new not in self.processlist: break
		self.processlist.append(new)
		return new

	def rmname(self):
		return self.processlist.remove(int(self.name))

	def schedule(self, delay):
		self.status = status.delaying
		shed = threading.Timer(delay, self.run)
		shed.start()
		return shed

	def run(self):
		if (self.delay > 0) & (self.status != status.delaying):
			return self.schedule(self.delay)
		else:
			self.status = status.running
			super().run()
			self.status = status.done
