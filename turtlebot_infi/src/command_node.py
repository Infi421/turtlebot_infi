#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def send_command():
    rospy.init_node('command_node', anonymous=True)
    pub = rospy.Publisher('/my_commands', String, queue_size=10)

    while not rospy.is_shutdown():
        command = input("Enter command (e.g., 'Forward 5', 'Left 1'): ")
        pub.publish(command)
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        send_command()
    except rospy.ROSInterruptException:
        pass
