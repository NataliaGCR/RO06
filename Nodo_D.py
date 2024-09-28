#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class NodeD:
    def __init__(self):
        rospy.init_node('node_D', anonymous=True)
        self.pub = rospy.Publisher('outgoing_LETTER', String, queue_size=10)
        self.sub = rospy.Subscriber('outgoing_LETTER', String, self.callback)

    def callback(self, msg):
        if msg.data.startswith("C:"):
            modified_msg = "D:" + msg.data[2:] + " D"
            rospy.loginfo(f"Node D received: {msg.data}, sending: {modified_msg}")
            self.pub.publish(modified_msg)

if __name__ == '__main__':
    try:
        node_d = NodeD()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
