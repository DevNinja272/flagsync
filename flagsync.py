#!/usr/bin/env python

##
# File: flagsync.py
# Description: Sync the flag to a remote system.
# WARNING DO NOT HARDCODE THE FLAG
##

##
# External modules
##
import os                       # Environment variable reading
import socket                   # Network interaction, duh


##
# Read connection details for host and port
# Connect to remote service
# Send flag and close the connection
##
def sync_flag():
        # Read connection details for host and port
	# DO NOT hardcode the flag here
        host = str(os.environ['FLAG_HOST'])
        port = int(os.environ['FLAG_PORT'])
        flag = str(os.environ['FLAG_FLAG'])

        # Connect to remote service
        s = socket.socket()
        s.connect((host, port))

        # Send flag and close the connection
        s.send(flag)
        s.close()


##
# Make it do the thing
##
if __name__ == '__main__':
        sync_flag()
