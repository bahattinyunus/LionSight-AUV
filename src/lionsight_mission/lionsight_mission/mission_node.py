import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from vision_msgs.msg import Detection2DArray
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import time

class MissionNode(Node):
    def __init__(self):
        super().__init__('mission_node')
        self.state_pub = self.create_publisher(String, 'mission/state', 10)
        self.detection_sub = self.create_subscription(Detection2DArray, 'perception/lionfish_detections', self.detection_callback, 10)
        
        # Mission States
        self.states = ['SEARCHING', 'TRACKING', 'ENGAGING', 'RECOVERY']
        self.current_state = 'SEARCHING'
        
        self.get_logger().info('LionSight Mission Manager active. State machine initialized: SEARCHING.')
        
        # Main State Machine Timer (2Hz)
        self.timer = self.create_timer(0.5, self.state_machine_loop)

    def detection_callback(self, msg):
        if len(msg.detections) > 0 and self.current_state == 'SEARCHING':
            self.get_logger().info('🎯 Visual contact! Transitioning to TRACKING.')
            self.current_state = 'TRACKING'

    def state_machine_loop(self):
        """
        Simulated Behavior Tree logic.
        """
        state_msg = String()
        state_msg.data = self.current_state
        self.state_pub.publish(state_msg)
        
        if self.current_state == 'SEARCHING':
            # Logic to request random path from path_planner
            pass
        elif self.current_state == 'TRACKING':
            # Logic to maintain distance from detected object
            pass
        elif self.current_state == 'RECOVERY':
            # Return to boat or surface
            pass

def main(args=None):
    rclpy.init(args=args)
    node = MissionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
