import os
import sys

import launch
import launch_ros.actions


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
            name='namespace'
        ),
        launch.actions.DeclareLaunchArgument(
            name='train_mode',
            default_value='false'
        ),
        launch.actions.DeclareLaunchArgument(
            name='agent_name',
            default_value='rule_05'
        ),
        launch_ros.actions.Node(
            package='rosnav',
            executable='rosnav_node.py',
            name='rosnav_node',
            output='screen',
            parameters=[
                {
                    'agent_name': launch.substitutions.LaunchConfiguration('agent_name')
                }
            ],
            condition=launch.conditions.IfCondition(
                "$(eval arg('train_mode') == false)")
        ),
        launch_ros.actions.Node(
            package='testing',
            executable='drl_agent_node.py',
            name='rosnav_action_node',
            output='screen',
            parameters=[
                {
                    'agent_name': launch.substitutions.LaunchConfiguration('agent_name')
                }
            ],
            condition=launch.conditions.IfCondition(
                "$(eval arg('train_mode') == false)")
        ),
        launch_ros.actions.Node(
            package='spacial_horizon',
            executable='spacial_horizon_node',
            name='spacial_horizon_node',
            output='log',
            parameters=[
                {
                    'agent_name': launch.substitutions.LaunchConfiguration('agent_name')
                }
            ]
        )
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
