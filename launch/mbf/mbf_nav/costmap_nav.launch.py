import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            name='model',
            default_value=''
        ),
        launch.actions.DeclareLaunchArgument(
            name='train_mode',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='namespace'
        ),
        launch.actions.DeclareLaunchArgument(
            name='frame'
        ),
        launch.actions.DeclareLaunchArgument(
            name='speed',
            default_value='2'
        ),
        launch.actions.DeclareLaunchArgument(
            name='inter_planner'
        ),
        launch.actions.DeclareLaunchArgument(
            name='local_planner'
        ),
        launch.actions.DeclareLaunchArgument(
            name='agent_name',
            default_value=launch.substitutions.LaunchConfiguration('model')
        ),
        launch_ros.actions.Node(
            package='mbf_costmap_nav',
            executable='move_base_legacy_relay.py',
            name='move_base_legacy_relay',
            parameters=[
                get_package_share_directory(
                    'arena_simulation_setup') + '/configs/mbf/move_base_params.yaml',
                launch.substitutions.LaunchConfiguration('model')
            ]
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'arena_simulation_setup'), 'launch/mbf/planners/local/mbf_$(arg local_planner).launch.py')
            ),
            launch_arguments={
                'model': launch.substitutions.LaunchConfiguration('model'),
                'speed': launch.substitutions.LaunchConfiguration('speed'),
                'train_mode': launch.substitutions.LaunchConfiguration('train_mode'),
                'agent_name': launch.substitutions.LaunchConfiguration('agent_name'),
                'namespace': launch.substitutions.LaunchConfiguration('namespace'),
                'frame': launch.substitutions.LaunchConfiguration('frame')
            }.items()
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'arena_simulation_setup'), 'launch/mbf/planners/inter/mbf_$(arg inter_planner).launch.py')
            ),
            launch_arguments={
                'model': launch.substitutions.LaunchConfiguration('model'),
                'speed': launch.substitutions.LaunchConfiguration('speed'),
                'namespace': launch.substitutions.LaunchConfiguration('namespace'),
                'frame': launch.substitutions.LaunchConfiguration('frame')
            }.items()
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
