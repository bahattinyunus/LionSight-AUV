from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Perception Nodes
        Node(
            package='lionsight_perception',
            executable='detection_node',
            name='detection_node',
            output='screen'
        ),
        Node(
            package='lionsight_perception',
            executable='stereo_vision_node',
            name='stereo_vision_node',
            output='screen'
        ),
        
        # Navigation Nodes
        Node(
            package='lionsight_navigation',
            executable='slam_node',
            name='slam_node',
            output='screen'
        ),
        Node(
            package='lionsight_navigation',
            executable='path_planner',
            name='path_planner',
            output='screen'
        ),
        
        # Control Nodes
        Node(
            package='lionsight_control',
            executable='pid_stabilizer',
            name='pid_stabilizer',
            output='screen'
        ),
        Node(
            package='lionsight_control',
            executable='thruster_manager',
            name='thruster_manager',
            output='screen'
        ),
        
        # Mission Node
        Node(
            package='lionsight_mission',
            executable='mission_node',
            name='mission_node',
            output='screen'
        ),
    ])
