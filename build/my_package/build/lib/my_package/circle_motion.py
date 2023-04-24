import rclpy
from geometry_msgs.msg import Twist

def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('move_robot_node')

    publisher = node.create_publisher(Twist, '/cmd_vel', 10)

    twist_msg = Twist()
    twist_msg.linear.x = 0.2
    twist_msg.angular.z = 0.5

    while rclpy.ok():
        publisher.publish(twist_msg)
        node.get_logger().info('Publishing cmd_vel message')
        rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
