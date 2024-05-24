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
            name='speed',
            default_value='0.22'
        ),
        launch.actions.DeclareLaunchArgument(
            name='namespace'
        ),
        launch.actions.DeclareLaunchArgument(
            name='frame'
        ),
        launch_ros.actions.Node(
            package='topic_tools',
            executable='relay',
            name='mbf_cmd_vel_relay'
        ),
        launch_ros.actions.Node(
            package='cohan_layers',
            executable='agents_bridge.py',
            name='agents',
            output='screen'
        ),
        launch_ros.actions.Node(
            package='agent_path_prediction',
            executable='agent_path_prediction',
            name='agent_path_predict',
            output='screen',
            parameters=[
                {
                    'velobs_mul': '1.0'
                },
                {
                    'velscale_mul': '2.0'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='agent_path_prediction',
            executable='predict_goal.py',
            name='agent_goal_predict',
            output='screen'
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'cohan_layers'), 'launch/agent_filter.launch.py')
            )
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
