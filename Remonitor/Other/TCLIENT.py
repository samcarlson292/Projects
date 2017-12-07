import zmq
import msgpack
import sys
import threading
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def main(ports):
	print ports
	context = zmq.Context()
	socket = context.socket(zmq.PULL)
	list_dict = dict()

	print "Connecting to servers"
	for port in ports:
		print str(port)
		socket.connect("tcp://localhost:" + port)
		port_string_cpu = str(port) + "_cpu_percent"
		port_string_vmem = str(port) + "_vmem_percent"
		port_string_swap = str(port) + "_swap_percent"
		port_string_disk = str(port) + "_disk_percent"
		port_string_number = str(port) + "_number"
		list_dict[port_string_cpu] = []
		list_dict[port_string_vmem] = []
		list_dict[port_string_swap] = []
		list_dict[port_string_disk] = []
		list_dict[port_string_number] = []
	
	#msgfilter = msgpack.packb(sys_name)
	#socket.setsockopt(zmq.SUBSCRIBE, msgfilter)
	
	# Plotting resources
	#cpu_percent = []
	#cpu_percent_next = []
	#vmem_percent = []
	#swap_percent = []
	#disk_percent = []
	
	fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
	fig.suptitle('Remote System Monitor', fontsize=16, fontweight='bold')

	def update(socket, list_dict, lock, j):
		packet = socket.recv()
		#pack = packet[len(msgfilter):]
		i = msgpack.unpackb(packet)
		print i

		in_port = i['port']
		lock.acquire()
		# Update lists for plotting
		list_dict[str(in_port) + '_cpu_percent'].append(i['CPU_usage'])
		list_dict[str(in_port) + '_vmem_percent'].append(i['vmem_percent'])
		list_dict[str(in_port) + '_swap_percent'].append(i['swap_percent'])
		list_dict[str(in_port) + '_disk_percent'].append(i['disk_percent'])
		list_dict[str(in_port) + '_number'].append(j)
		lock.release()
		return
		
	def animate(j):
		lock = threading.Lock()
		print "INSIDE ANIMATE"
		threads = []
		for port in ports:
			threads.append(threading.Thread(target=update, args=(socket, list_dict, lock, j)))
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()
		#cpu_percent.append(i['CPU_usage'])
		#vmem_percent.append(i['vmem_percent'])
		#swap_percent.append(i['swap_percent'])
		#disk_percent.append(i['disk_percent'])
		#x_array.append(j)

		#print 'LENGTH x_array: ' + str(len(x_array))
		#print 'LENGTH cpu_percent: ' + str(len(cpu_percent))
		#print 'LENGTH vmem_percent: ' + str(len(vmem_percent))
		#print 'LENGTH swap_percent: ' + str(len(swap_percent))
		#print 'LENGTH disk_percent: ' + str(len(disk_percent))

		# Clear for redraw
		ax1.clear()
		ax2.clear()
		ax3.clear()
		ax4.clear()

		# Plot to redraw
		for port in ports:
			ax1.plot(list_dict[str(port) + '_number'], list_dict[str(port) + '_cpu_percent'])
			ax2.plot(list_dict[str(port) + '_number'], list_dict[str(port) + '_vmem_percent'])
			ax3.plot(list_dict[str(port) + '_number'], list_dict[str(port) + '_swap_percent'])
			ax4.plot(list_dict[str(port) + '_number'], list_dict[str(port) + '_disk_percent'])

	# Call for animation
	ani = animation.FuncAnimation(fig, animate, interval=1000)

	# Display the charts
	plt.show()

	# Print the final arrays
	#print 'CPU PERCENTS: ' + str(cpu_percent)
	#print 'VMEM PERCENTS: ' + str(vmem_percent)
	#print 'SWAP PERCENTS: ' + str(swap_percent)
	#print 'DISK PERCENTS: ' + str(disk_percent)


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Must pass the ports of running servers!'
	else:
		main(sys.argv[1:])

