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
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
