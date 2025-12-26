# SPDX-FileCopyrightText: 2025 Your Name <your.email@example.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

class QueryService(Node):
    def __init__(self):
        super().__init__('server')
        self.srv = self.create_service(Query, 'query', self.query_callback)
        self.get_logger().info('Password Authentication Service Ready.')
        
        # ここが正解のパスワードです
        self.correct_password = "successful_pass737300"

    def query_callback(self, request, response):
        # 受け取ったパスワードを確認
        if request.password == self.correct_password:
            response.access_granted = True
            response.message = "Login Successful! Welcome to the system."
            self.get_logger().info('Authentication: SUCCESS')
        else:
            response.access_granted = False
            response.message = "Access Denied: Incorrect password."
            self.get_logger().info('Authentication: FAILED')

        return response

def main():
    rclpy.init()
    node = QueryService()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()

if __name__ == '__main__':
    main()
