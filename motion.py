#!/usr/bin/env python
import rospy
import json, pprint
from std_msgs.msg import String
from geometry_msgs.msg import Twist

alexaPacket = None

def callback(msg):
	global alexaPacket
	#print type(msg), ':', msg, '\n', dir(msg)
	#print type(msg.data), ':', msg.data
	alexaPacket = json.loads(msg.data)
	pprint.pprint(alexaPacket)
	
rospy.init_node('move')
rospy.Subscriber("TCPITL", String, callback)
motion_node = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
rate = rospy.Rate(10)

motion = Twist()

while not rospy.is_shutdown():
	#rospy.Subscriber("TCP-ITL", String, callback)
	if alexaPacket == None:
		continue
	intent_slots = alexaPacket['request']['intent']['slots']
	dir = intent_slots['Direction'].get('value', 'stop')
	if dir == "left":
		motion.linear.x = 0.0	
		motion.angular.z = 1.0
	elif dir == "right" or dir == "71":
		motion.linear.x = 0.0	
		motion.angular.z = -1.0
	elif dir == "forward":
		motion.linear.x = 0.1
		motion.angular.z = 0.0
	elif dir == "backward":
		motion.linear.x = -0.1
		motion.angular.z = 0.0
	elif dir == "stop": 
		motion.linear.x = 0.0
		motion.angular.z = 0.0

	motion_node.publish(motion)
	rate.sleep()

	
#alexaPacket = json.loads()
