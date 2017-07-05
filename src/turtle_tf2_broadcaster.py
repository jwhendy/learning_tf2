#!/usr/bin/env python

import rospy
import tf
import tf2_ros
import geometry_msgs.msg
import turtlesim.msg
import std_msgs

def handle_turtle_pose(msg, turtlename):
    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()                                  

    t.header = std_msgs.msg.Header(stamp=rospy.Time.now(),
                                   frame_id='world')
    
    t.child_frame_id = turtlename

    t.transform.translation = geometry_msgs.msg.Vector3(x=msg.x,
                                                        y=msg.y,
                                                        z=0)
    
    qx, qy, qz, qw = tf.transformations.quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation = geometry_msgs.msg.Quaternion(x=qx,
                                                        y=qy,
                                                        z=qz,
                                                        w=qw)
    
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('tf2_turtle_broadcaster')
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()
                     
