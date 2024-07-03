import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


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
            name='namespace',
            default_value=''
        ),
        launch.actions.DeclareLaunchArgument(
            name='frame'
        ),
        launch.actions.DeclareLaunchArgument(
            name='move_forward_only',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='model_file',
            default_value=get_package_share_directory(
                'drl_vo_barn_nav') + '/src/model/drl_vo.zip'
        ),
        launch_ros.actions.Node(
            package='topic_tools',
            executable='relay',
            name='mbf_cmd_vel_relay'
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'drl_vo_barn_nav'), 'launch/barn_data.launch.py')
            )
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
