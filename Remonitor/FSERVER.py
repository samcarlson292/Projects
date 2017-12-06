import psutil
import threading
import os
import sys
import zmq
import msgpack
from operator import itemgetter

# Necessary imports above

# Object to store system info
class infoStore:

	# Object constructor
	def __init__(self, port):
		self.info_dict = dict()

		# Internal lock to protect the info_dict data structure during concurrent calls
		self.lock = threading.Lock()

		self.set_name(port)
		self.get_proc_info()
		self.get_CPU_usage()
		self.get_mem_info()
		self.get_swap_info()
		self.get_disk_info()
		self.get_info_dict()
	
	# Sets the port that this server sends on
	def set_name(self, port):
		self.lock.acquire()
		self.info_dict['port'] = port
		self.lock.release()

	# Gets the individual process info
	# Multithreaded function to grab all process info simultaneously
	def get_proc_info(self):
		proc_list = psutil.get_pid_list() 
		num_proc = len(proc_list)
		time_list_lock = threading.Lock()
		time_list = dict()
		thread_list = []
		for proc in proc_list:
			try:
				process = psutil.Process(proc)
				thread_list.append(threading.Thread(target=self.by_process, args=(time_list, process, time_list_lock, proc)))
			except psutil.NoSuchProcess:
				pass
		for thread in thread_list:
			thread.start()
		for thread in thread_list:
			thread.join()
		sorted_time_list = sorted(time_list.items(), key=itemgetter(1), reverse=True)
		self.lock.acquire()
		self.info_dict['num_proc'] = num_proc
		counter = 1
		for key, info in sorted_time_list[:5]:
			self.info_dict['proc' + str(counter)] = info
			counter += 1
		self.lock.release()

	# Get specific info about each process
	def by_process(self, time_list, process, lock, PID):
		try:
			cpu_percent = process.get_cpu_percent(interval=.5)
			num_threads = process.get_num_threads()
			mem_percent = process.get_memory_percent()
		except psutil.NoSuchProcess:
			return
		lock.acquire()
		time_list[PID] = (cpu_percent, mem_percent, num_threads)
		lock.release()
		return

	# Get aggregate CPU utilization of the system
	def get_CPU_usage(self):
		usage = psutil.cpu_percent(interval=1, percpu = False)
		self.lock.acquire()
		self.info_dict['CPU_usage'] = usage
		self.lock.release()

	# Get aggregate virtual memory utilization of the system
	def get_mem_info(self):
		mem_info = psutil.virtual_memory()
		self.lock.acquire()
		self.info_dict['vmem_total'] = mem_info.total
		self.info_dict['vmem_used'] = mem_info.used
		self.info_dict['vmem_percent'] = mem_info.percent
		self.lock.release()

	# Get aggregate swap memory utilization of the system
	def get_swap_info(self):
		swap_info = psutil.swap_memory()
		self.lock.acquire()
		self.info_dict['swap_total'] = swap_info.total
		self.info_dict['swap_used'] = swap_info.used
		self.info_dict['swap_percent'] = swap_info.percent
		self.lock.release()

	# Get aggregate disk utilization info about the system
	def get_disk_info(self):
		disk_info = psutil.disk_usage('/')
		self.lock.acquire()
		self.info_dict['disk_total'] = disk_info.total
		self.info_dict['disk_used'] = disk_info.used
		self.info_dict['disk_percent'] = disk_info.percent
		self.lock.release()

	# Print the data struct info dictionary
	def print_info_dict(self):
		print 'Info dictionary: ' + str(self.info_dict)

	# Return the info dictionary data structure
	def get_info_dict(self):
		return self.info_dict

# Define main function
def main(port):

	# ZMQ setup PUSH/PULL
	context = zmq.Context()
	socket = context.socket(zmq.PUSH)
	socket.bind("tcp://*:" + port)
	#set high watermark to avoid queueing lots of old messages
	socket.setsockopt(zmq.SNDHWM, 3)

	# Continuously get the info_dict from class above, encode, and send it
	while True:
		i = infoStore(port)
		packed = msgpack.packb(i.get_info_dict())
		socket.send(packed)
		
# Main function
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Monitor must be initialized with a port number!"
	else:
		main(sys.argv[1])


