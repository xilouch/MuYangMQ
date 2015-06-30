#coding=utf-8
__author__ = '药师Aric'
'''
'''
import threading
import json

class ProducerManager:
    def create(self, request):
        return Producer(request)

class Producer(threading.Thread):
    def __init__(self, request):
        threading.Thread.__init__(self)
        self.request = request
        self.client = request.client

    def run(self):
        try:
            self.request.data = self.client.recv(self.request.bufSize)
            self.client.send('receive'.encode());
            # data = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
            # self.client.send(data.encode)
            print('new thread : ' + self.name);
            print(self.request.data.decode())
        except Exception as e:
            print(e)
        finally:
            print(self.name + ' connect close')
            self.client.close()
