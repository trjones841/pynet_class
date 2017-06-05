"""

"""

import time

def example():
	'''
	
	'''
	import os
	
	return os.environ

def main():
	
	startTime = time.clock()
	print "\n The start time is %s sec" % startTime
	
	while time.clock() < 63:
		print " \n Capturing screen at time %.4f sec" % time.clock()
		name = str("%.2f"%time.clock())+ "sec"
		time.sleep(2)
		print example()

if __name__ == "__main__":
		main()

