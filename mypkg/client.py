#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Ryuta Kawamoto ryu073000@i.softbank.jp
# SPDX-License-Identifier: BSD-3-Clause

#コマンドライン引数
import sys

import rclpy
from rclpy.node import Node

#定義した型（Quer.srv）の読み込み
from person_msgs.srv import Query

class QueryClient(Node):

    #クラスの定義と初期化メソッド
    def __init__(self):
        #ノードの名前をclientとする
        super().__init__('client')
        #Query型を使って、queryというサービスに通信する
        self.cli = self.create_client(Query, 'query')
        #ループ：1.0秒ごとにserver.pyの立ち上がりを確認し、待機
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('通信中:serverを待っています...')
        #リクエストオブジェクト
        self.req = Query.Request()

    #リクエスト通信メソッド
    def send_request(self, password):
        #受け取ったパスワードをリクエストで定義する
        self.req.password = password
        #非同期でサーバに上で定義したリクエストを送る
        self.future = self.cli.call_async(self.req)
        #サーバから返事が返ってくるまでこのノードの処理をループする
        rclpy.spin_until_future_complete(self, self.future)
        #サーバから返事が帰ってきた結果を返す
        return self.future.result()

def main():
    rclpy.init()
    node = QueryClient()
    #パスワードの確認
    if len(sys.argv) > 1:
        input_password = sys.argv[1]
    else:

        input_password = "wrong_password"
    #リクエスト送信メソッドを呼び出し、結果を受け取る
    response = node.send_request(input_password)
    #結果の表示（ros2のログ出力機能)
    if response.access_granted:
        node.get_logger().info(f'[SUCCESS] {response.message}')
    else:
        node.get_logger().info(f'[FAILED] {response.message}')
    #終了処理（メモリなどのソースの解法）
    node.destroy_node()
    #終了処理（ros2の通信システム全体の終了）
    rclpy.shutdown()
#main関数の実行
if __name__ == '__main__':
    main()
