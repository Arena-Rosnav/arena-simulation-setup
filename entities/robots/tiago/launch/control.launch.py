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
        launch.actions.DeclareLaunchArgument(
            name='robot',
            default_value='titanium'
        ),
        launch.actions.DeclareLaunchArgument(
            name='arm',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='end_effector',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='ft_sensor',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='laser_model',
            default_value='sick-571'
        ),
        launch.actions.DeclareLaunchArgument(
            name='camera_model',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='multi',
            default_value=''
        ),
        launch.actions.DeclareLaunchArgument(
            name='gzpose',
            default_value='-x 0.0 -y 0.0 -z 0.0 -R 0.0 -P 0.0 -Y 0.0'
        ),
        launch.actions.DeclareLaunchArgument(
            name='gui',
            default_value='true'
        ),
        launch.actions.DeclareLaunchArgument(
            name='debug',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='public_sim',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='tuck_arm',
            default_value='true'
        ),
        launch.actions.DeclareLaunchArgument(
            name='recording',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='extra_gazebo_args',
            default_value=''
        ),
        launch.actions.DeclareLaunchArgument(
            name='use_moveit_camera',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='use_dynamic_footprint',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='base_type',
            default_value='pmb2'
        ),
        launch.actions.DeclareLaunchArgument(
            name='file_suffix',
            default_value="$(eval (('no-arm' if not arm else (end_effector if end_effector else 'no-ee') + ('_' +  ft_sensor if ft_sensor else ''))))"
        ),
        launch.actions.DeclareLaunchArgument(
            name='ee_suffix',
            default_value="$(eval (end_effector if end_effector else 'no-ee'))"
        ),
        launch_ros.actions.Node(
            package='gazebo_utils',
            executable='odom.py',
            name='odom_pub',
            parameters=[
                {
                    'gains/arm_7_joint/p': '10'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='topic_tools',
            executable='relay',
            name='cmd_vel_relay',
            parameters=[
                {
                    'gains/arm_7_joint/p': '10'
                }
            ]
        ),
        launch_ros.actions.Node(
            package='topic_tools',
            executable='relay',
            name='scan_relay',
            parameters=[
                {
                    'gains/arm_7_joint/p': '10'
                }
            ]
        ),
        launch.actions.IncludeLaunchDescription(
            launch.launch_description_sources.PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory(
                    'tiago_gazebo'), 'launch/simulation_tiago_bringup.launch.py')
            ),
            launch_arguments={
                'arm': launch.substitutions.LaunchConfiguration('arm'),
                'end_effector': launch.substitutions.LaunchConfiguration('end_effector'),
                'ft_sensor': launch.substitutions.LaunchConfiguration('ft_sensor'),
                'laser_model': launch.substitutions.LaunchConfiguration('laser_model'),
                'camera_model': launch.substitutions.LaunchConfiguration('camera_model'),
                'public_sim': launch.substitutions.LaunchConfiguration('public_sim'),
                'use_moveit_camera': launch.substitutions.LaunchConfiguration('use_moveit_camera'),
                'use_dynamic_footprint': launch.substitutions.LaunchConfiguration('use_dynamic_footprint'),
                'base_type': launch.substitutions.LaunchConfiguration('base_type')
            }.items()
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
