#!/usr/bin/env python

import socket
import rospy
import time
from std_msgs.msg import String

rospy.init_node('TCPITL')

pub = rospy.Publisher('TCPITL', String)

TCP_IP = '128.153.144.103'
TCP_PORT = 5006
BUFFER_SIZE = 2048
MESSAGE = "Hello, World!"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
while not rospy.is_shutdown():
	data = s.recv(BUFFER_SIZE)
	pub.publish(data)
	time.sleep(.5)

s.close()

print "received data:", data
