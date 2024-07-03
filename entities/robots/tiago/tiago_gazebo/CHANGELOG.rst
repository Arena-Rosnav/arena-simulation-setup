^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.1.5 (2024-05-10)
------------------
* Merge branch 'omm/fix/launch_standarization' into 'humble-devel'
  Launch files moved to TIAGo family standard
  See merge request robots/tiago_simulation!145
* Suggested changeSuggested changes
* Restored has_screen arg
* Passing base_type argument
* Passing the needed args
* Suggested changes
* Launch files moved to TIAGo family standard
* Contributors: Oscar, davidterkuile

4.1.4 (2024-04-25)
------------------
* Merge branch 'abr/fix/old-params' into 'humble-devel'
  remove old params
  See merge request robots/tiago_simulation!147
* remove old params
* Contributors: antoniobrandi

4.1.3 (2024-04-22)
------------------
* Merge branch 'sgg/feat/base_type_omni_base' into 'humble-devel'
  Migrate to new parameter style
  See merge request robots/tiago_simulation!144
* Migrate to new parameter style
* Contributors: Sergi Garcia, davidterkuile

4.1.2 (2024-04-16)
------------------
* Merge branch 'feat/ros2-pipelines' into 'humble-devel'
  navigation pipeline integration for private sim
  See merge request robots/tiago_simulation!142
* cosmetic and update readme
* removed slam arg
* linters
* navigation pipeline integration for private sim
* Contributors: andreacapodacqua, antoniobrandi

4.1.1 (2024-04-04)
------------------
* Reset self._is_successful when sending a goal
* Enable tuck_arm test
* Contributors: Noel Jimenez

4.1.0 (2024-02-28)
------------------
* Launch MoveIt 2 by default
* Contributors: Noel Jimenez

4.0.9 (2024-02-02)
------------------
* Merge branch 'feat/register-components' into 'humble-devel'
  use single entry point for navigation
  See merge request robots/tiago_simulation!133
* use single entry point for navigation
* Contributors: antoniobrandi

4.0.8 (2024-01-19)
------------------
* Adding pal_robotiq_description in the package list
* Contributors: Aina Irisarri

4.0.7 (2023-12-22)
------------------
* changing package name of hey5 into the new one: pal_hey5
* Contributors: Aina Irisarri

4.0.6 (2023-12-20)
------------------
* move world_name to pal_gazebo_worlds
* Disable tuck_arm_test
* Contributors: Noel Jimenez, antoniobrandi

4.0.5 (2023-11-14)
------------------
* Add website tag
* Contributors: Noel Jimenez

4.0.4 (2023-11-13)
------------------
* Set use_sim_time true
* Remove pal flags dependency
* Contributors: Noel Jimenez

4.0.3 (2023-06-16)
------------------
* Merge branch 'fix/set-is-robot' into 'humble-devel'
  Use a different navigation launcher for simulation
  See merge request robots/tiago_simulation!116
* use tiago_sim_navigation
* using is_robot argument in simulation
* Merge branch 'ros1_cleanup' into 'humble-devel'
  ROS 1 cleanup for humble-devel
  See merge request robots/tiago_simulation!117
* remove not ported grasping demo
* Remove Media, models and worlds folders
* Contributors: Noel Jimenez, Sai Kishor Kothakota, antoniobrandi, thomaspeyrucain

4.0.2 (2023-02-24)
------------------
* Merge branch 'tuck_arm' into 'humble-devel'
  tuck_arm for play_motion2
  See merge request robots/tiago_simulation!103
* comment subprocess to kill gazebo at the end of the test
* remove unused deps and reorder
* reduce sleep time
* log waiting for state
* remove unnecessary const
* tuck arm test
* launch tuck arm
* tuck_arm for play_motion2
* Contributors: Jordan Palacios, Noel Jimenez

4.0.1 (2023-02-08)
------------------
* Merge branch 'robot_state_publisher' into 'humble-devel'
  Remove robot_state_publisher from tiago_spawn
  See merge request robots/tiago_simulation!105
* remove robot_state_publisher from tiago_spawn
* Contributors: Jordan Palacios, Noel Jimenez

4.0.0 (2022-11-30)
------------------
* Merge branch 'fix_dependency' into 'humble-devel'
  Fix buildtool dependency
  See merge request robots/tiago_simulation!102
* fix buildtool dependency
* Merge branch 'refactor_simulation_launchers' into 'humble-devel'
  Refactor simulation launchers
  See merge request robots/tiago_simulation!98
* move navigation to simulation launcher
* add moveit to simulation launcher
* Merge branch 'cleanup' into 'humble-devel'
  Cleanup
  See merge request robots/tiago_simulation!95
* update package deps
* Merge branch 'fix_world_name_arg' into 'humble-devel'
  fix world_name arg
  See merge request robots/tiago_simulation!94
* add world_name arg to simulation
* Merge branch 'linters' into 'humble-devel'
  Linters
  See merge request robots/tiago_simulation!93
* linters
* add linters
* Merge branch 'cleanup' into 'humble-devel'
  Cleanup
  See merge request robots/tiago_simulation!91
* rm ros1 launchers
* Merge branch 'refactor_ld' into 'humble-devel'
  Refactor LaunchDescription population
  See merge request robots/tiago_simulation!90
* refactor LaunchDescription population
* Merge branch 'update_copyright' into 'humble-devel'
  Update copyright
  See merge request robots/tiago_simulation!89
* update license
* update copyright
* Merge branch 'update_maintainers' into 'humble-devel'
  Update maintainers
  See merge request robots/tiago_simulation!88
* update maintainers
* Merge branch 'del_arg' into 'humble-devel'
  Remove robot_name arg
  See merge request robots/tiago_simulation!87
* del unnecesary arg robot_name
* Merge branch 'humble_fixes' into 'humble-devel'
  Add robot name arg to rewrite default
  See merge request robots/tiago_simulation!86
* robot name arg
* Since play motion is not started by default can't tuck arm
* Cleanup
* Added tuck_arm script to tiago_gazebo.launch.py
* Added retries
* Don't use spin() and check for goal result
* Wait for play_motion is_ready to be successfull
* Migrated tuck_arm.py to ros2
* Added some ToDo's
* tiago_gazebo now also launches the tiago_bringup
* Moved the tiago spawn to its own launch.py
* Added pal_gripper_description package
* Added tiago_gazebo.launch.py
* package.xml and CMakeLists.txt to ros2 format
* Contributors: Jordan Palacios, Noel Jimenez, Victor Lopez

2.0.23 (2020-07-30)
-------------------
* Merge branch 'rename_tf_prefix' into 'erbium-devel'
  Rename tf_prefix to robot_namespace
  See merge request robots/tiago_simulation!70
* Rename tf_prefix to robot_namespace
* Contributors: davidfernandez, victor

2.0.22 (2020-04-21)
-------------------

2.0.21 (2020-02-26)
-------------------

2.0.20 (2019-11-04)
-------------------

2.0.19 (2019-10-23)
-------------------

2.0.18 (2019-10-15)
-------------------

2.0.17 (2019-10-15)
-------------------
* Merge branch 'refactor' into 'erbium-devel'
  Refactor
  See merge request robots/tiago_simulation!64
* removed joystick from sim
* Contributors: Procópio Stein, Victor Lopez

2.0.16 (2019-10-10)
-------------------
* Merge branch 'remove-sonar-cloud' into 'erbium-devel'
  Remove sonar cloud
  See merge request robots/tiago_simulation!63
* removed dep
* removed sonar cloud
* Contributors: Procópio Stein, Victor Lopez

2.0.15 (2019-09-25)
-------------------
* Merge branch 'remove-speed-limit' into 'erbium-devel'
  Remove speed limit
  See merge request robots/tiago_simulation!61
* removed remap of twist mux topic
* removed speed limit
* Contributors: Procópio Stein, Victor Lopez

2.0.14 (2019-09-23)
-------------------

2.0.13 (2019-09-23)
-------------------

2.0.12 (2019-08-07)
-------------------

2.0.11 (2019-08-01)
-------------------

2.0.10 (2019-07-17)
-------------------
* Merge branch 'multi_pmb2' into 'erbium-devel'
  Fix multi tiago private simulation
  See merge request robots/tiago_simulation!53
* Fix multi tiago private simulation
* Contributors: Adria Roig, Victor Lopez

2.0.9 (2019-07-09)
------------------

2.0.8 (2019-07-03)
------------------

2.0.7 (2019-06-17)
------------------
* Merge branch 'cylinder_on_table' into 'erbium-devel'
  Added the world cylinder on the table for the pick and place demo
  See merge request robots/tiago_simulation!47
* Merge branch 'teb_planner' into 'erbium-devel'
  Add TEB planner
  See merge request robots/tiago_simulation!49
* Add TEB planner
* Added the world cylinder on the table for the pick and place demo
* Contributors: Jordi Pages, Victor Lopez, alessandrodifava, davidfernandez

2.0.6 (2019-03-26)
------------------
* Forward missing parameter
* Remove duplicated package
* Contributors: Victor Lopez

2.0.5 (2019-03-14)
------------------

2.0.4 (2019-02-26)
------------------
* Merge branch 'multi_simulation' into 'erbium-devel'
  Fix multitiago simulation
  See merge request robots/tiago_simulation!48
* Fix multitiago simulation
* Forward use_moveit_camera arg
* Add use_moveit_camera
* Contributors: Victor Lopez, davidfernandez

2.0.3 (2019-01-23)
------------------
* Change default deprecated param to titanium
  For backwards compatibility
* Contributors: Victor Lopez

2.0.2 (2019-01-23)
------------------
* Add mapping from deprecated robot to new variables
* Remove usages of pass_all_args, not supported in kinetic yet
* Contributors: Victor Lopez

2.0.1 (2018-12-20)
------------------

2.0.0 (2018-12-19)
------------------
* Merge branch 'specifics-refactor' into 'erbium-devel'
  Add advanced navigation option to tiago_navigation.launch
  See merge request robots/tiago_simulation!45
* Add missing multi arg
* Remvoe pass_all_args
* Refactor controller configuration
* Contributors: Victor Lopez

1.0.11 (2018-11-26)
-------------------
* Merge branch 'add-extra-gz-args-flag' into 'erbium-devel'
  Add extra_gazebo_args flag
  See merge request robots/tiago_simulation!44
* Add extra_gazebo_args flag
* Contributors: Victor Lopez

1.0.10 (2018-11-26)
-------------------
* Merge branch 'fix_opencv_public' into 'erbium-devel'
  Fix wrong model
  See merge request robots/tiago_simulation!42
* Fix wrong model
* Contributors: Victor Lopez, davidfernandez

1.0.9 (2018-10-26)
------------------
* Merge branch 'add-image-proc' into 'erbium-devel'
  Add image proc
  See merge request robots/tiago_simulation!39
* Add image proc to emulate better robot topics
* Contributors: Victor Lopez

1.0.8 (2018-09-28)
------------------

1.0.7 (2018-07-30)
------------------
* Merge branch 'fix-simulation-warnings' into 'erbium-devel'
  call upload.launch rather than tiago_upload.launch
  See merge request robots/tiago_simulation!38
* call upload.launch rather than tiago_upload.launch
* Contributors: Jordi Pages, Victor Lopez

1.0.6 (2018-07-06)
------------------
* Merge branch 'add-log-recording' into 'erbium-devel'
  Add log recording
  See merge request robots/tiago_simulation!36
* Add log recording param
* Contributors: Victor Lopez

1.0.5 (2018-06-05)
------------------
* Merge branch 'use-gazebo-worlds' into 'erbium-devel'
  Use pal_gazebo_worlds
  See merge request robots/tiago_simulation!34
* Use pal_gazebo_worlds
* Contributors: Daniele De Cillis, Hilario Tome

1.0.4 (2018-05-16)
------------------

1.0.3 (2018-04-10)
------------------

1.0.2 (2018-03-29)
------------------
* Add param to skip tuck_arm
* Contributors: Victor Lopez

1.0.1 (2018-03-26)
------------------

1.0.0 (2018-03-26)
------------------

0.0.18 (2018-03-21)
-------------------
* Fix typo
* Merge branch 'add-simple-ramp-world' into 'dubnium-devel'
  add simple_ramp world
  See merge request robots/tiago_simulation!27
* add simple_ramp world
* Contributors: Jordi Pages, Victor Lopez

0.0.17 (2018-02-20)
-------------------
* added missing depend
* Contributors: Hilario Tome

0.0.16 (2018-02-16)
-------------------
* Added missing scripts directory from installation
* Contributors: Jordan Palacios

0.0.15 (2018-01-24)
-------------------
* use robot sufix in all launch files
* enable planning to fix strange movement in Gazebo
* tmp hack for pal_nav_sm in simulation
* Contributors: Jeremie Deray, Jordi Pages

0.0.14 (2017-11-07)
-------------------
* add point cloud throttle and filter
  launch this node unless we are in public simulation
* Contributors: Jordi Pages

0.0.13 (2017-11-02)
-------------------
* reduce tables height to 0.8 m
* fixed pal_office world for tiago navigation, added script to create the tiago pose files, modified the launch files to have tiago_multi with and without navigation
* add pal office world
* Add pal office world
* Contributors: AleDF, Jordi Pages

0.0.12 (2017-05-30)
-------------------
* Add sun and ground_plane models
* Contributors: Victor Lopez

0.0.11 (2017-05-16)
-------------------
* Add camera parameter for Octomap with MoveIt!
* Allow multiple Tiagos to use the navigation stack
* Allow multiple Tiagos on Gazebo
  Fixes #15402
* Fix z height from Gazebo world objects_on_table
* Add lights in front of the people to fix color
  Given that Gazebo renders the models of the people very dark as can be seen in the TIAGo tutorial:
  ![TIAGo tutorial people rendered dark screenshot](http://wiki.ros.org/Robots/TIAGo/Tutorials/PersonDetection?action=AttachFile&do=get&target=gazebo_person_detection.jpg)
  I added some lights in front of the models so they become more visible.
* add Willow Garage world
* Contributors: Adria Roig, AleDF, David Fernandez, Jordi Pages, Sam Pfeiffer, davidfernandez

0.0.10 (2016-10-21)
-------------------

0.0.9 (2016-10-14)
------------------
* add aruco board
* move a bit farther the pringles can
* add a poster in the tutorial office for opencv_tut
* refs #14222. Do not call simple_action_grasping
  In public simulation this package is unreleased
* Add simulation world and model for refs #14521
* add look_to_point example world and models
* use proper pal_hardware_gazebo yaml file
* add sonars and depth image
* fix tiago_controller_configuration_gazebo dep
* set myself as maintainer
* launch files to support public map/loc
* add export to remove some error prints
* convert to rectangular box and fix inertia
* fix sdf version
* change slightly the pose of the table and cube
* add 5 cm single marker side cube
* disable dynamic_footprint when public_sim=true
* add missing running dependencies
* set up simulation for Steel and Titanium versions
* set steel robot for grasping demo
* New worlds for Apps/tiago_tutorials
* add simulation world and models
* New launch file for the pick and place demo, also provided the world
* improve inertia, friction and collision model
* remove home motion to speed up demo
* grasping demo using green cube
* add separate motions file and fix can intertia
* Add a image_rect_color topic republishing image_raw rgb image to have the same interface in simulation
* Added aruco cube and world
* Contributors: Jordi Pages, Sam Pfeiffer, job-1994

0.0.7 (2016-06-15)
------------------

0.0.6 (2016-06-15)
------------------
* add missing launch sonar_to_cloud
* Contributors: Jeremie Deray

0.0.5 (2016-06-15)
------------------
* Change default robot to custom for some launch files
* Contributors: Victor Lopez

0.0.4 (2016-06-15)
------------------

0.0.3 (2016-06-14)
------------------
* Updated simulation for imu and force torque
* Add simulation controller configuration package
  Also make the simulation launch that related controllers instead of the tiago_bringup ones
* Update package.xml to pull pal_hardware_gazebo dependence
* Cleanup
* Make steel default
* Added navigation visualisation to rviz
* Contributors: Bence Magyar, Jordi Adell, Sam Pfeiffer

0.0.2 (2015-04-15)
------------------

0.0.1 (2015-04-15)
------------------
* Install tuck script and configuration files
* Add tuck_arm to gazebo launch sequence
* Robot spawns on the ground instead of tiny elevation
* Pass robot param to bringup
* Changed default value of robot to titanium
* add camera view in rviz and modify objects places
* Fix conflict...
* Add objects on table world and belongings
  Conflicts:
  tiago_gazebo/worlds/objects_on_table.world
* add tiago standalone rviz configuration file
* add simulated worlds
* add rviz for whole body control testing
* refs #10237 : adds small_office world
* Lower spawn height
* Initial commit of tiago_simulation
* Contributors: Bence Magyar, Jordi Pages, enriquefernandez
