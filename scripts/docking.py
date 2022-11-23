#! /usr/bin/env python3
import rospy
import actionlib


class Docking():

    def __init__(self):
        


if __name__ == '__main__':
    # Initialize Node 
    rospy.init_node('robot_docking_node', anonymous=True)
    robotdocking = Docking()
    rospy.spin()