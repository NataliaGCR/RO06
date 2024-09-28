#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class NodeA:
    def __init__(self):
        rospy.init_node('node_A', anonymous=True)
        self.pub = rospy.Publisher('outgoing_LETTER', String, queue_size=10)
        self.sub = rospy.Subscriber('outgoing_LETTER', String, self.callback)
        self.message = "Hello, this is a secret message."
        self.counter = 1
        rospy.Timer(rospy.Duration(2), self.publish_message)

    def publish_message(self, event):
        msg_to_send = f"A:{self.message} - Count: {self.counter}"
        rospy.loginfo(f"Node A publishing: {msg_to_send}")
        self.pub.publish(msg_to_send)
        self.counter += 1

    def callback(self, msg):
        if msg.data.startswith("D:"):
            rospy.loginfo(f"Node A received: {msg.data[2:]}")

if __name__ == '__main__':
    try:
        node_a = NodeA()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
