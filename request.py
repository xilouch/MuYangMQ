#coding=utf-8
__author__ = '药师Aric'
'''
'''
class Request:
    def __init__(self):
        self.client = None
        self.maxConnections = 0
        self.bufSize = 0
        self.host = None
        self.port = None
        self.data = None
