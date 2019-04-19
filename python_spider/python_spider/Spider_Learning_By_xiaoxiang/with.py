#!/usr/bin/python3
#-*-coding =utf-8 -*-
class CDNTextIOWrapper():
    def __init__(self):
        print('__init__')
        pass
    def __enter__(self):
        print('__enter__')
        return self
    def __exit__(self,type,value,trace):
        print('type:',type)
        print('value:',value)
        print('trace:',trace)
    def do_something(self):
        print('do_something')
def demo():
    return CDNTextIOWrapper()
with demo() as d:
    d.do_something()