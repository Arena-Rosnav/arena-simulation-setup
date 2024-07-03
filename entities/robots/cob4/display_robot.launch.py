import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='robot',
            default_value='$(optenv ROBOT !!NO_ROBOT_SET!!)'
        ),
        launch.actions.DeclareLaunchArgument(
            name='gui',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='rvizconfig',
            default_value=get_package_share_directory(
                'arena_simulation_setup') + '/entities/robots/cob4/robots/common/display_robot.rviz'
        ),
        launch_ros.actions.Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='rviz',
            executable='rviz',
            name='rviz',
            on_exit=launch.actions.Shutdown()
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'arena_simulation_setup'), 'entities/robots/cob4/upload_robot.launch.py')
            ),
            launch_arguments={
                'robot': launch.substitutions.LaunchConfiguration('robot')
            }.items()
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
