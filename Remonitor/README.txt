Project Team: Samuel B. Carlson (carlsosb) & Mitchell J. Masia (masiamj)

Correct Files to View, Test, & Grade:
	1.  Server (Run on remote machines): FSERVER.py
	2.  Client (Run on one machine): FCLIENT.py
	3.  Project Description: project_proposal.txt
	4.  ALL OTHER FILES WERE FOR TESTING PURPOSES, NOT NECESSARY, BUT INTERESTING TO SEE.


To run and test:

Necessary Installs:
	ZeroMQ (via pip [pyzmq])
	Message Pack (via pip [msgpack-python])
	Matplotlib
	Numpy
	Psutil

Program Components:
	Server: Collects information on remote systems and sends a byte-stream of info to the client via ZeroMQ.
	Client: Receives, processes, and plots the data from servers.

To run:
	1.  Start server --> "python FSERVER.py <port>" where <port> is an unused port number (e.g. 5555)
		a.  One can start an arbitrary number of servers
	2.  Start client --> "python FCLIENT.py <port>" where <port> represents all ports used by current servers.
		a.  For example, if 3 servers have been started using ports 5555, 5556, & 5557,
			the command to correctly run the client is: "python FCLIENT.py 5555 5556 5557"

For further information about the project implementation and motivation see: "project_proposal.txt"

Thanks,
The Remonitor Team
