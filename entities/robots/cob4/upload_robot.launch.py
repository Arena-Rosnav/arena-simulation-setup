import os
import sys

import launch
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='robot',
            default_value='cob4-11'
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
