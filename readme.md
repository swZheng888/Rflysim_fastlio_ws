1.编译源码
首先编译Livox-SDK2库（虽然平台的点云数据用的是PointCldou2格式，但是由于开源算法代码里用到livox点云格式，因此需要编译）
- cd Livox-SDK2-master && mkdir build && cd build
- cmake ..
- make
- sudo make install

2.编译ROS节点
- cd rflysim_fastlio_ws/src/livox_ros_driver2
- sudo chmod 777 -R *
- ./build.sh ROS1

3.运行代码
- cd rflysim_fastlio_ws/sh
- bash lidar.sh


