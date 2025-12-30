#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Ryuta Kawamoto ryu073000@i.softbank.jp
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

class QueryService(Node):
    def __init__(self):
        super().__init__('server')
        #Queryのqueryを使うことまた、リクエストが来たらself.query_callback関数の実行
        self.srv = self.create_service(Query, 'query', self.query_callback)

        self.get_logger().info('Password Authentication Service Ready.')
        #正解のパスワード設定
        self.correct_password = "pass737300"

    #パスワードの判定
    def query_callback(self, request, response):
        #成功
        if request.password == self.correct_password:
            response.access_granted = True
            response.message = "Login Successful!"
            self.get_logger().info('Authentication: SUCCESS')
        #失敗
        else:
            response.access_granted = False
            response.message = "Access Denied: Incorrect password."
            self.get_logger().info('Authentication: FAILED')

        return response

def main():
    rclpy.init()
    node = QueryService()
    try:
        #ループ処理
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
#main関数の実行
if __name__ == '__main__':
    main()
