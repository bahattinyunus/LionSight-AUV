import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Wrench
from std_msgs.msg import Float64MultiArray
import numpy as np

class ThrusterManager(Node):
    def __init__(self):
        super().__init__('thruster_manager')
        self.subscription = self.create_subscription(Wrench, 'control/thrust_wrench', self.wrench_callback, 10)
        self.pwm_pub = self.create_publisher(Float64MultiArray, 'hardware/thruster_pwms', 10)
        
        # 6-DOF Mixer Matrix for 6 Vectored Thrusters (Simplified example)
        # Rows: Thrusters (1-6), Cols: DOF (X, Y, Z, Roll, Pitch, Yaw)
        self.mixer_matrix = np.array([
            [ 0.707,  0.707,  0.0,   0.0,   0.0,   1.0], # T1 (Front Left)
            [ 0.707, -0.707,  0.0,   0.0,   0.0,  -1.0], # T2 (Front Right)
            [-0.707,  0.707,  0.0,   0.0,   0.0,  -1.0], # T3 (Back Left)
            [-0.707, -0.707,  0.0,   0.0,   0.0,   1.0], # T4 (Back Right)
            [ 0.0,    0.0,    1.0,   1.0,   1.0,   0.0], # T5 (Vertical Left)
            [ 0.0,    0.0,    1.0,  -1.0,   1.0,   0.0]  # T6 (Vertical Right)
        ])
        
        self.get_logger().info('LionSight Thruster Manager active. 6-DOF Mixing Matrix loaded.')

    def wrench_callback(self, msg):
        wrench_vector = np.array([
            msg.force.x, msg.force.y, msg.force.z,
            msg.torque.x, msg.torque.y, msg.torque.z
        ])
        
        # Calculate thrust for each motor
        thruster_outputs = np.dot(self.mixer_matrix, wrench_vector)
        
        # Normalized and clip
        thruster_outputs = np.clip(thruster_outputs, -1.0, 1.0)
        
        pwm_msg = Float64MultiArray()
        pwm_msg.data = thruster_outputs.tolist()
        self.pwm_pub.publish(pwm_msg)

def main(args=None):
    rclpy.init(args=args)
    node = ThrusterManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
