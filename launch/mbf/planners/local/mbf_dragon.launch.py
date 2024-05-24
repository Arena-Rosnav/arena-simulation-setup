import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='model'
        ),
        launch.actions.DeclareLaunchArgument(
            name='speed'
        ),
        launch.actions.DeclareLaunchArgument(
            name='move_forward_only',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='namespace'
        ),
        launch.actions.DeclareLaunchArgument(
            name='frame'
        ),
        launch.actions.DeclareLaunchArgument(
            name='odom_topic',
            default_value='odom'
        ),
        launch_ros.actions.Node(
            package='barn_challenge',
            executable='gap_navigation',
            name='gap_navigation',
            output='log',
            parameters=[
                {
                    'goal_x': '10'
                },
                {
                    'goal_y': '10'
                },
                {
                    'left': '-100'
                },
                {
                    'top': '-100'
                },
                {
                    'bwidth': '200'
                },
                {
                    'bheight': '200'
                },
                {
                    'gapThresh': '.65'
                },
                {
                    'dist': '10'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='barn_challenge',
            executable='reduce_lidar',
            name='reduce_lidar',
            output='screen',
            parameters=[
                {
                    'cap': '10'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='barn_challenge',
            executable='cone_bench.py',
            name='cone_bench',
            output='log',
            parameters=[
                {
                    'max_vel_x': launch.substitutions.LaunchConfiguration('speed')
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
