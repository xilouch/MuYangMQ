#coding=utf-8
__author__ = '药师Aric'
'''
'''
import socket
from request import Request
from producer import ProducerManager

request = Request()
request.maxConnections = 50
request.bufSize = 1024 * 100
request.host = 'localhost'
request.port = 8083

manager = ProducerManager()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((request.host, request.port))
server.listen(request.maxConnections) #并发数
print('server start')
while True:
    print('waiting accept')
    request.client, address = server.accept()
    manager.create(request).start()

