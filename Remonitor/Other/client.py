import zmq
import msgpack
import sys


def main(sys_name, port):
	context = zmq.Context()
	socket = context.socket(zmq.SUB)

	print "Connecting to server..."
	socket.connect("tcp://localhost:" + port)
	#subscribe to updates from specified system
	msgfilter = msgpack.packb(sys_name)
	socket.setsockopt(zmq.SUBSCRIBE, msgfilter)	

	#receive data and update display
	print "Retrieving data from server..."
	for update in range(1, 11):
		packet = socket.recv()
		pack = packet[len(msgfilter):]
		i = msgpack.unpackb(pack)
		print i
	
		
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Monitor must be initialized with a name and port number!"
	else:
		main(sys.argv[1], sys.argv[2])

