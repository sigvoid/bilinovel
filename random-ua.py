import http.server
import socketserver
import random

PORT = 12378

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 读取ua.txt文件中的所有行
        with open('ua.txt', 'r') as file:
            ua_list = file.readlines()

        # 随机选择一行文本
        random_ua = random.choice(ua_list).strip()

        # 设置响应头
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # 响应随机选择的文本
        self.wfile.write(random_ua.encode())

# 创建HTTP服务器并监听指定端口
with socketserver.TCPServer(("localhost", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    # 保持服务器运行
    httpd.serve_forever()
