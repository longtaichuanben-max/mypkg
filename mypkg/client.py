#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Ryuta Kawamoto ryu073000@i.softbank.jp
# SPDX-License-Identifier: BSD-3-Clause

import sys
import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

class QueryClient(Node):
    def __init__(self):
        super().__init__('client')
        self.cli = self.create_client(Query, 'query')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for authentication service...')
        self.req = Query.Request()

    def send_request(self, password):
        self.req.password = password
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main():
    rclpy.init()
    node = QueryClient()

    if len(sys.argv) > 1:
        input_password = sys.argv[1]
    else:

        input_password = "wrong_password"

    response = node.send_request(input_password)

    if response.access_granted:
        node.get_logger().info(f'[SUCCESS] {response.message}')
    else:
        node.get_logger().info(f'[FAILED] {response.message}')

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
