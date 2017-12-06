import os
import sys
import psutil

print 'Welcome to the psutil tester!'

"""
# SPIN
for i in range(1, 10000000):
	i = i + 1
"""

# Use this process as test process
process = psutil.Process(os.getpid())
print '\n'

# See the time on the CPU
print 'CPU Time: ' + str(process.get_cpu_times())
print '\n'

# See the number of threads in this program
print 'Num Processes: ' + str(process.get_num_threads())
print '\n'

# See the priority of priority of this thread
print 'Process priority: ' + str(process.get_nice())
print '\n'

# See the number of context switches undergone by this process
print 'Number of context switches: ' + str(process.get_num_ctx_switches())
print '\n'

# See the process CPU utilization percentage
print 'CPU Utilization: ' + str(process.get_cpu_percent())
print '\n'

# See the process memory information
print 'Memory information: ' + str(process.get_memory_info())
print '\n'

# See memory percentage
print 'Memory percentage: ' + str(process.get_memory_percent())
print '\n'

# See child processes of a process
print 'Child processes: ' + str(process.get_children())
print '\n'

print 'DONE GATHERING PROCESS INFORMATION.  NOW ACQUIRING AGGREGATE INFO.'
print '\n'

# See all currently running PIDs
print 'List of currently running PIDs: ' + str(psutil.get_pid_list())
print '\n'

# See all currently running processes
print 'List of running processes: ' + str(psutil.get_process_list())
print '\n'

# See system wide CPU usage percentage
print 'System wide CPU usage percentage: ' + str(psutil.cpu_percent(interval = 1, percpu = False))
print '\n'

# See system wide info on virtual memory
print 'System wide virtual memory info: ' + str(psutil.virtual_memory())
print '\n'

# See system wide info on swap memory
print 'System wide swap memory info: ' + str(psutil.swap_memory())
print '\n'

# See system wide info on disk usage
print 'System wide disk usage info: ' + str(psutil.disk_usage('/'))
print '\n'

print 'DONE!'









