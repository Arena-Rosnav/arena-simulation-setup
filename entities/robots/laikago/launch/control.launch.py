import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


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
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'unitree_controller_go1'), 'launch/set_ctrl.launch.py')
            ),
            launch_arguments={
                'robot_namespace': launch.substitutions.LaunchConfiguration('robot_namespace'),
                'target_state': '5'
            }.items()
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
