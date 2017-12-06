import zmq
import msgpack
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Necessary imports above

def main(ports):
	#print ports

	# ZMQ setup PUSH/PULL model
	context = zmq.Context()
	socket = context.socket(zmq.PULL)
	list_dict = dict()

	# Connect to same host on multiple ports
	print "Connecting to servers"
	for port in ports:
		print str(port)
		socket.connect("tcp://127.0.0.1:" + port)
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
	
	# Create plotting context w/ info
	fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
	fig.suptitle('Remote System Monitor', fontsize=16, fontweight='bold')
		
	# Animate function run to dynamically update plots
	def animate(j):
		# Receive packets from remote host
		packet = socket.recv()
		
		# Unpack the byte stream
		i = msgpack.unpackb(packet)
		print i

		# Isolate the port field to identify which list to update dynamically
		in_port = i['port']

		# Update lists for plotting
		list_dict[str(in_port) + '_cpu_percent'].append(i['CPU_usage'])
		list_dict[str(in_port) + '_vmem_percent'].append(i['vmem_percent'])
		list_dict[str(in_port) + '_swap_percent'].append(i['swap_percent'])
		list_dict[str(in_port) + '_disk_percent'].append(i['disk_percent'])
		list_dict[str(in_port) + '_number'].append(j)


		# Print lengths to assure correct plotting dimensions (debugging)
		#print 'LENGTH x_array: ' + str(len(x_array))
		#print 'LENGTH cpu_percent: ' + str(len(cpu_percent))
		#print 'LENGTH vmem_percent: ' + str(len(vmem_percent))
		#print 'LENGTH swap_percent: ' + str(len(swap_percent))
		#print 'LENGTH disk_percent: ' + str(len(disk_percent))

		# Clear plots for redraw
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

	# Call for animate function using matplotlib animation API
	ani = animation.FuncAnimation(fig, animate, interval=1000)

	# Display the charts
	plt.show()

	# Print the final arrays to view (debugging)
	#print 'CPU PERCENTS: ' + str(cpu_percent)
	#print 'VMEM PERCENTS: ' + str(vmem_percent)
	#print 'SWAP PERCENTS: ' + str(swap_percent)
	#print 'DISK PERCENTS: ' + str(disk_percent)

# Main function
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print 'Must pass the ports of running servers!'
	else:
		main(sys.argv[1:])

