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
        launch_ros.actions.Node(
            package='controller_manager',
            executable='spawner',
            name='controller_spawner',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='gazebo_utils',
            executable='odom.py',
            name='odom_pub'
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
