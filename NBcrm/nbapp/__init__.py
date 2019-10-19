# import random
#
# with open('a', encoding='utf-8', mode='w')as f:
#     for i in range(0,100):
#
#         b=random.randint(0,256)
#         c='172.25.254.%s'%b
#         f.write(c+'\n')
#
#         # if b>99:
#         #     print(('172.25.254.%s')%b)
#
#
# with open('a',encoding='utf-8')as f2:
#     # data=f2.read()
#     for line in f2:
#
#         if len(line.split('.')[3].strip())==3:
#             print(line)
from abc import ABCMeta
import time

class Node():
    def __init__(self,item):
        self.item=item
        self.next=None

class Link():
    def __init__(self):
        self.head=None
    def add(self,item):
        node=Node(item)
        node.next=self.head
        self.head=node
    def travel(self):
        cur=self.head
        if self.head==None:
            print('null!')
        while cur:
            print(cur.item)
            cur=cur.next
    def isEmpty(self):
        return not bool(self.head)

    def length(self):
        cur=self.head
        length=0
        while cur:
            length+=1
            cur=cur.next
        return length
    def search(self,item):
        cur=self.head
        find=False
        while cur:
            if cur.item==item:
                find=True
                break
            cur=cur.next
        return find

    def append(self,item):
        node=Node(item)

        if self.head==None:
            self.head=node
            return
        cur=self.head
        pre=None
        while cur:
            pre=cur
            cur=cur.next
        pre.next=node

    def insert(self,pos,item):
        node=Node(item)
        if pos<=0 or pos>self.length():
            print('out range')
            return
        cur=self.head
        pre=None
        for i in range(pos):
            pre=cur
            cur=cur.next
        pre.next=node
        node.next=cur

    def remove(self,item):
        cur=self.head
        pre=None
        if self.head==None:
            return 'null'
        if self.head.item==item:
            self.head=cur.next

        while cur:
            pre=cur
            cur=cur.next
            if cur.item==item:
                pre.next=cur.next
                return

    def reverse(self):
        cur=self.head
        pre=None
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        self.head=pre

from queue import Queue
class Stack():
    def __init__(self):
        self.main_queue=Queue()
        self.mirror_queur=Queue()

    def push(self,value):
        self.main_queue.put(value)
    def pop(self):
        if self.main_queue.qsize()==0:
            return None

        while True:
            if self.main_queue.qsize()==1:
                value=self.main_queue.get()
                break
            self.mirror_queur.put(self.main_queue.get())
            self.main_queue,self.mirror_queur=self.mirror_queur,self.main_queue
        return value

