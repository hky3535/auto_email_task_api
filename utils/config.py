"""
何恺悦 hekaiyue 2023-07-06
"""
import logging
import traceback
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Config:
    def __init__(self, parent):
        self.parent = parent
        self.config = dict()

    def http_config(self):
        def request_handler(self):
            parent = self
            class RequestHandler(BaseHTTPRequestHandler):
                def _set_headers(self, code=200):
                    self.send_response(code)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()

                def custom_response(self, code, custom_code, custom_message):
                    self._set_headers(code)
                    self.wfile.write(json.dumps({"code": custom_code, "message": custom_message}, ensure_ascii=False).encode())

                def do_GET(self):
                    self.custom_response(404, 404, "不支持GET请求")

                def do_POST(self):
                    if self.path == "/send_emails":
                        try:
                            # 接收参数
                            content_length = int(self.headers["Content-Length"])
                            parameters = str(self.rfile.read(content_length),"utf-8")
                            parameters = json.loads(parameters, strict=False)
                            logging.info(f"传入源参数为：{str(parameters)}")
                            
                            # 解析参数并运行一次
                            parent.config = parameters
                            parent.parent.send.send_task()

                            self.custom_response(200, 200, "参数解析成功，邮件已发送成功")
                        except Exception as e:
                            self.custom_response(500, 500, f"参数解析失败，错误原因：POST请求格式错误，{e}")
                            logging.error(traceback.format_exc())  
                    else:
                        self.custom_response(404, 404, "POST请求路径错误")
            
            return RequestHandler
        
        request_handler = HTTPServer(("0.0.0.0", 8888), request_handler(self))
        print("http://0.0.0.0:8888/send_emails")
        request_handler.serve_forever()
