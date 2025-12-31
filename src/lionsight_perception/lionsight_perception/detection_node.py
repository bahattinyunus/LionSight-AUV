import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class DetectionNode(Node):
    def __init__(self):
        super().__init__('detection_node')
        self.subscription = self.create_subscription(
            Image,
            'camera/image_raw',
            self.listener_callback,
            10)
        self.get_logger().info('Lionsight Detection Node initialized with YOLOv8 placeholder.')

    def listener_callback(self, msg):
        # TODO: Implement YOLOv8 inference
        # self.get_logger().info('Receiving image frame...')
        pass

def main(args=None):
    rclpy.init(args=args)
    node = DetectionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
