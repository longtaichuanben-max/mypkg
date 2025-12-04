#!/bin/bash -xv
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
source /opt/ros/humble/setup.bash
export PYTHONUNBUFFERED=1

timeout 30 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log || true
cat /tmp/mypkg.log | grep 'Listen: 10'
