#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Ryuta Kawamoto ryu073000@i.softbank.jp
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# Launchを実行してログをファイルに保存
timeout 10 ros2 launch mypkg server_client.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Login Successful'
