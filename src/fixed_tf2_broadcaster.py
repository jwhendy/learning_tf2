#!/usr/bin/env python

import rospy
import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg
import std_msgs

class FixedTFBroadcaster:

    def __init__(self):
        self.pub_tf = rospy.Publisher('/tf', tf2_msgs.msg.TFMessage, queue_size=1)

        while not rospy.is_shutdown():
            rospy.sleep(0.1)

            t = geometry_msgs.msg.TransformStamped()                                  

            t.header = std_msgs.msg.Header(stamp=rospy.Time.now(),
                                           frame_id='turtle1')
    
            t.child_frame_id = 'carrot1'

            t.transform.translation = geometry_msgs.msg.Vector3(x=0,
                                                                y=2,
                                                                z=0)
    
            qx, qy, qz, qw = (0, 0, 0, 1)
            t.transform.rotation = geometry_msgs.msg.Quaternion(x=qx,
                                                                y=qy,
                                                                z=qz,
                                                                w=qw)
            tfm = tf2_msgs.msg.TFMessage([t])
            self.pub_tf.publish(tfm)

if __name__ == '__main__':
    rospy.init_node('my_tf2_broadcaster')
    tfb = FixedTFBroadcaster()
    rospy.spin()
    
