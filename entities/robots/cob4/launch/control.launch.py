import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='robot_namespace'
        ),
        launch.actions.DeclareLaunchArgument(
            name='frame'
        ),
        launch.actions.DeclareLaunchArgument(
            name='robot',
            default_value='cob4-11'
        ),
        launch.actions.DeclareLaunchArgument(
            name='input_scans',
            default_value=launch.substitutions.LaunchConfiguration(
                'robot_namespace')
        ),
        launch_ros.actions.Node(
            package='gazebo_utils',
            executable='odom.py',
            name='odom_pub'
        ),
        launch_ros.actions.Node(
            package='topic_tools',
            executable='relay',
            name='cmd_vel_relay'
        ),
        launch_ros.actions.Node(
            package='cob_sick_s300',
            executable='cob_scan_filter',
            name='scan_filter',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='cob_sick_s300',
            executable='cob_scan_filter',
            name='scan_filter',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='cob_sick_s300',
            executable='cob_scan_filter',
            name='scan_filter',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='cob_scan_unifier',
            executable='scan_unifier_node',
            name='cob_scan_unifier',
            output='log',
            parameters=[
                {
                    'frame': launch.substitutions.LaunchConfiguration('frame')
                }
            ]
        ),
        launch_ros.actions.Node(
            package='topic_tools',
            executable='relay',
            name='laser_relay'
        ),
        launch_ros.actions.Node(
            package='controller_manager',
            executable='controller_manager',
            name='base_controller_spawner',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[
                launch.substitutions.LaunchConfiguration('robot')
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
