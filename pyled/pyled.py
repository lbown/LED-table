#!/usr/bin/env python2
import sys
import settings
import collections

# TODO: import correct movie driver based on config setting

def main(*args):
	
	# Specifies behavior to follow once pictureStack is exhausted
	actionTimer = None # TODO: read queue done action from config
	
	# Strings specifying what actions are next. Loops by default
	actionQueue = collections.deque([]) # TODO: this needs to be _bound_ to a user-maintained queue (both read and write required from client and table)
	actionQueueUpdate = False

	actionObject = getActionObject(actionQueue[0])
	actionQueue.rotate(-1)

	# Action
		# parent of Movie
		# parent of Game -- don't terminate Game objects on timer, Game objects send a finished signal back to the loop
		# parent of StateMachine
		# parent of ResponsiveVisualization
		###
		# Has tick method - returns a picture
		# __delete__ function needs to correctly relinquish all input. An option is to 

	# Main loop: execute every 1/60 second

								### Maintain action object ###

		# Loop through Action queue based on timer maintained here, or signal recieved from Game object
			# Request update from Action object, send response picture to output driver

								### Maintain binding on actionQueue ###
		# If actionQueueUpdate and len(actionQueue) > 0 
			# actionObject.__delete__()
			# actionObject = getActionObject(actionQueue[0])
			# actionQueue.rotate(-1)


if __name__ == '__main__':
	main(*sys.argv[1:])