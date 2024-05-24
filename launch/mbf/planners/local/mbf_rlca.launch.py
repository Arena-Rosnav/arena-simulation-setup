import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='model',
            default_value='burger'
        ),
        launch.actions.DeclareLaunchArgument(
            name='speed'
        ),
        launch.actions.DeclareLaunchArgument(
            name='namespace'
        ),
        launch.actions.DeclareLaunchArgument(
            name='frame'
        ),
        launch.actions.DeclareLaunchArgument(
            name='move_forward_only',
            default_value='false'
        ),
        launch_ros.actions.Node(
            package='rlca-ros',
            executable='rlca_node_tb3.py',
            name='rl_collision_avoidance',
            output='log',
            parameters=[
                {
                    'max_vel_x': launch.substitutions.LaunchConfiguration('speed')
                }
            ]
        ),
        launch_ros.actions.Node(
            package='spacial_horizon',
            executable='spacial_horizon_node',
            name='spacial_horizon_node',
            output='screen',
            parameters=[
                launch.substitutions.LaunchConfiguration('model')
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
