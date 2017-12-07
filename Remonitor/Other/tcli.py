import zmq
import msgpack
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main():
	context = zmq.Context()
	socket = context.socket(zmq.SUB)

	print "Connecting to server..."
	socket.connect("tcp://localhost:5555")
	#default filter of no messages (could be used to sub to specific machine	at execution
	socket.setsockopt(zmq.SUBSCRIBE, b'') 
	
	# Plotting resources
	x_array = []
	cpu_percent = []
	cpu_percent_next = []
	vmem_percent = []
	swap_percent = []
	disk_percent = []
	count = 0
	
	fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
	fig.suptitle('Remote System Monitor', fontsize=16, fontweight='bold')
	ax1.set_title("CPU Utilization vs. Time", fontsize=12)
	ax1.set_xlabel("Time", fontsize=12)
		
	def animate(j):
		print "INSIDE ANIMATE"
		i = socket.recv()
		unpacked = msgpack.unpackb(i)
		#print "Update " + str(update) + ":" + str(unpacked)
		cpu_percent.append(unpacked['CPU_usage'])
		cpu_percent_next.append(unpacked['CPU_usage'] + 5)
		vmem_percent.append(unpacked['vmem_percent'])
		swap_percent.append(unpacked['swap_percent'])
		disk_percent.append(unpacked['disk_percent'])
		x_array.append(j)
		ax1.clear()
		ax2.clear()
		ax3.clear()
		ax4.clear()
		ax1.plot(x_array, cpu_percent)
		ax1.plot(x_array, cpu_percent_next)
		ax2.plot(x_array, vmem_percent)
		ax3.plot(x_array, swap_percent)
		ax4.plot(x_array, disk_percent)
	ani = animation.FuncAnimation(fig, animate, interval=1000)
	plt.show()

	print 'CPU PERCENTS: ' + str(cpu_percent)
	print 'VMEM PERCENTS: ' + str(vmem_percent)
	print 'SWAP PERCENTS: ' + str(swap_percent)
	print 'DISK PERCENTS: ' + str(disk_percent)	

if __name__ == '__main__':
	main()

