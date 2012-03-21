class ExitTimer(object):
	def __init__(self, duration):
		# Number of milliseconds that must have elapsed
		# before the exit funciton will trigger.
		self.time_to_exit = duration
		
		# Time elapsed since the last update
		self.time = 0
		
		# An active timer can trigger when the full duration elapses.
		# Using kill() can 
		self.active = True
	
	def update(self, timestep):
		self.time += timestep
	
	def reset(self):
		# Reset the timer
		self.time = 0
	
	def can_exit(self):
		# Allow player to exit the current level
		return self.active and self.time > self.time_to_exit
		
	def kill(self):
		# Stop the timer prematurely without hitting the statement at the end
		self.active = False
