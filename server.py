#coding=utf-8
__author__  = "xilouch <ch_56@163.com>"
__status__  = "production"
__version__ = "0.1"
__date__    = ""

import socket
import logging
from request import Request
from producer import ProducerManager

logger = logging.getLogger('default')

request = Request()
request.maxConnections = 50
request.bufSize = 1024 * 100
request.host = 'localhost'
request.port = 8083

manager = ProducerManager()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((request.host, request.port))
server.listen(request.maxConnections) #并发数
logger.info('server start')
while True:
    logger.info('waiting accept')
    request.client, address = server.accept()






