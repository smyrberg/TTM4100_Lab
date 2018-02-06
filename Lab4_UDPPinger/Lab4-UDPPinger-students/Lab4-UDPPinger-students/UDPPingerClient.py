# This skeleton is valid for both Python 2.7 and Python 3.
# You should be aware of your additional code for compatibility of the Python version of your choice.

import time
from socket import *

# Get the server hostname and port as command line arguments
host = '127.0.0.1'#input('Fill in server host address\n')
port = 12000#int(input('Fill in server host port\n'))
timeout = 1 # in seconds

# Create UDP client socket
# FILL IN START
clientSocket =socket(AF_INET, SOCK_DGRAM)
# Set socket timeout as 1 second
clientSocket.settimeout(timeout)

# FILL IN END

# Sequence number of the ping message
ptime = 0

# Ping for 10 times
while ptime < 10:
    ptime += 1
    # Format the message to be sent as in the Lab description
    data = input('Enter message to server\n')

    try:
    	# FILL IN START
	    # Record the "sent time"
        sentTime = time.time()
        print(sentTime)
	    # Send the UDP packet with the ping message
        clientSocket.sendto(data,(host,port))
        print('test')
	    # Receive the server response
        response, serverAddress = clientSocket.recvfrom(1024)
	    # Record the "received time"
        recvTime = time.time()
	    # Display the server response as an output
        print('Message from server: ' + response + '\n')
	    # Round trip time is the difference between sent and received time
        RTT = recvTime - sentTime
        print(RTT)
        # FILL IN END
    except:
        # Server does not response
	     # Assume the packet is lost
        print("Request timed out.")
        continue

# Close the client socket
clientSocket.close()
