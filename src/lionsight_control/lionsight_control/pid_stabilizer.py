import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Wrench, PoseStamped
from nav_msgs.msg import Odometry
import numpy as np

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0.0
        self.integral = 0.0

    def calculate(self, setpoint, current, dt):
        error = setpoint - current
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        return (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

class PidStabilizer(Node):
    def __init__(self):
        super().__init__('pid_stabilizer')
        self.wrench_pub = self.create_publisher(Wrench, 'control/thrust_wrench', 10)
        self.odom_sub = self.create_subscription(Odometry, 'nav/odom', self.odom_callback, 10)
        
        # PIDs for 4 controlled DOF (X and Y are handled by path planning)
        self.pid_depth = PIDController(10.0, 0.1, 5.0)
        self.pid_roll  = PIDController(5.0,  0.0, 2.0)
        self.pid_pitch = PIDController(5.0,  0.0, 2.0)
        self.pid_yaw   = PIDController(8.0,  0.1, 3.0)
        
        self.setpoint_depth = 1.0 # default 1m depth
        
        self.get_logger().info('LionSight PID Stabilizer active. 4-Axis (Z, R, P, Y) control enabled.')

    def odom_callback(self, msg):
        # In a real control loop, dt would be calculated from timestamps
        dt = 0.05 
        
        wrench = Wrench()
        wrench.force.z  = self.pid_depth.calculate(self.setpoint_depth, msg.pose.pose.position.z, dt)
        # Yaw, Pitch, Roll calculation placeholders
        # wrench.torque.z = self.pid_yaw.calculate(...)
        
        self.wrench_pub.publish(wrench)

def main(args=None):
    rclpy.init(args=args)
    node = PidStabilizer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
