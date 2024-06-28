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
            name='pkg_hardware_config',
            default_value=get_package_share_directory(
                'arena_simulation_setup') + '/entities/robots/cob4'
        ),
        launch.actions.DeclareLaunchArgument(
            name='name',
            default_value='$(anon scan_unifier)'
        ),
        launch.actions.DeclareLaunchArgument(
            name='input_scans'
        ),
        launch.actions.DeclareLaunchArgument(
            name='output_scan',
            default_value='/scan'
        ),
        launch_ros.actions.Node(
            package='cob_scan_unifier',
            executable='scan_unifier_node',
            name=launch.substitutions.LaunchConfiguration('name'),
            output='log'
        ),
        launch_ros.actions.Node(
            package='laser_filters',
            executable='scan_to_scan_filter_chain',
            name='scan_unifier_filter',
            parameters=[
                get_package_share_directory(
                    'arena_simulation_setup') + '/entities/robots/cob4/robots/cob4/config/scan_unifier_filter.yaml'
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
