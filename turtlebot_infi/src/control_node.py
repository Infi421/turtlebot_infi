#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def command_callback(data):
    rospy.loginfo("Received command: %s", data.data)
    process_command(data.data)

def process_command(command):
    # Extract direction and speed from the command
    parts = command.split()
    if len(parts) == 2:
        direction, speed = parts
        speed = float(speed)
        send_twist(direction, speed)

def send_twist(direction, speed):
    twist_msg = Twist()

    if direction.lower() == 'forward':
        twist_msg.linear.x = speed
    elif direction.lower() == 'backward':
        twist_msg.linear.x = -speed
    elif direction.lower() == 'left':
        twist_msg.angular.z = speed
    elif direction.lower() == 'right':
        twist_msg.angular.z = -speed

    # Publish Twist message to control TurtleBot
    twist_pub.publish(twist_msg)

if __name__ == '__main__':
    rospy.init_node('control_node', anonymous=True)
    twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('/my_commands', String, command_callback)
    rospy.spin()
