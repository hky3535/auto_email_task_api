"""
何恺悦 hekaiyue 2023-07-06
"""
import logging
import os

from utils.send import Send
from utils.config import Config


class Main:
    def __init__(self):
        logging.basicConfig(
            filename="run.log", 
            level=logging.INFO, 
            format='%(asctime)s %(levelname)s %(message)s'
        )
        logging.info("日志将记录在run.log中")
        self.root_dir = os.path.dirname(__file__)
        logging.info(f"当前程序所在路径为：{self.root_dir}")

        self.config = Config(self)
        self.send = Send(self)

    def main(self):
        self.config.http_config()

Main().main()