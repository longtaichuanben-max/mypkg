#!/bin/bash -xv
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
source /opt/ros/humble/setup.bash

export PYTHONUNBUFFERED=1

#修正部分: > /tmp/mypkg.log 2>&1 || true に変更
#これでエラー出力も含めて全てファイルに書き込まれます
timeout 30 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1 || true

#デバッグ用: ログの中身を一度画面に表示させる（何が起きているか確認するため）
cat /tmp/mypkg.log

#テスト判定: パイプを使わずファイルパスを直接指定
grep 'Listen: 10' /tmp/mypkg.log
