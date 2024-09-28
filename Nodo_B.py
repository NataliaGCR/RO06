#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class NodeB:
    def __init__(self):
        rospy.init_node('node_B', anonymous=True)
        self.pub = rospy.Publisher('outgoing_LETTER', String, queue_size=10)
        self.sub = rospy.Subscriber('outgoing_LETTER', String, self.callback)

    def callback(self, msg):
        if msg.data.startswith("A:"):
            modified_msg = "B:" + msg.data[2:] + " B"
            rospy.loginfo(f"Node B received: {msg.data}, sending: {modified_msg}")
            self.pub.publish(modified_msg)

if __name__ == '__main__':
    try:
        node_b = NodeB()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
