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
            name='namespace'
        ),
        launch.actions.DeclareLaunchArgument(
            name='frame'
        ),
        launch.actions.DeclareLaunchArgument(
            name='move_forward_only',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='move_base_node',
            default_value='move_base_flex'
        ),
        launch_ros.actions.Node(
            package='LfH',
            executable='run_policy.py',
            name='hallucination',
            output='log',
            on_exit=launch.actions.Shutdown(),
            parameters=[
                {
                    'move_base_node': launch.substitutions.LaunchConfiguration('move_base_node')
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
