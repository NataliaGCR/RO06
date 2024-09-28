#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class NodeC:
    def __init__(self):
        rospy.init_node('node_C', anonymous=True)
        self.pub = rospy.Publisher('outgoing_LETTER', String, queue_size=10)
        self.sub = rospy.Subscriber('outgoing_LETTER', String, self.callback)

    def callback(self, msg):
        if msg.data.startswith("B:"):
            modified_msg = "C:" + msg.data[2:] + " C"
            rospy.loginfo(f"Node C received: {msg.data}, sending: {modified_msg}")
            self.pub.publish(modified_msg)

if __name__ == '__main__':
    try:
        node_c = NodeC()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
