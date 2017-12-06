import psutil
import sys
import os
from datetime import datetime, timedelta
import time

print 'Welcome to the infoGrabber!'
print 'This script uses "psutil" to grab pertinent system info. \n'

"""
Collect info about current users on the system.
"""
def get_users():
	print 'Collecting Information on Current System Users:\n'
	users = psutil.users()
	for user in users:
		print ('%-15s %-15s %s  (%s)' % (user.name,
						user.terminal or '-',
						datetime.fromtimestamp(user.started).strftime('%Y-%m-%d %H:%M'),
						user.host))

"""
Collect information about Disk Usage.
"""
def get_disk_usage():
	print 'Collecting Information on Disk Usage:\n'
	temp1 = '%-17s %8s %8s %8s %5s%% %9s  %s'
	print (temp1 % ('Device', 'Total', 'Used', 'Free', 'Use', 'Type', 'Mount'))
	for partition in psutil.disk_partitions(all=False):
		if os.name == 'nt':
			if 'cdrom' in partition.opts or partition.fstype == '':
				# Skip cd-rom
				continue
		usage = psutil.disk_usage(partition.mountpoint)
		# NEED TO CORRECT THE WAY THIS IS OUTPUT, KIND OF
		print (temp1 % (partition.device,
				du_bytes2human(usage.total),
				du_bytes2human(usage.used),
				du_bytes2human(usage.free),
				int(usage.percent),
				partition.fstype,
				partition.mountpoint))

def du_bytes2human(n):
	# http://code.activestate.com/recipes/578019
	symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
	prefix = {}
	for i, s in enumerate(symbols):
		prefix[s] = 1 << (i + 1) * 10
	for s in reversed(symbols):
		if n >= prefix[s]:
			value = float(n) / prefix[s]
			return '%.1f%s' % (value, s)
	return '$sB' % n


def main():
	#get_users()
	#print '\n\n'
	#get_disk_usage()



if __name__ == '__main__':
	main()


print '\n'
print 'DONE!'
