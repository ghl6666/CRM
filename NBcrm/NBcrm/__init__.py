# num=input()
# all_ball=input()
#
#
# #篮子中的球不少于2个
# #多个篮子中可以放同一个颜色的球,
# #如果各个篮子中的彩球的数量是相同的
# def count_num(num,all_ball):
#     all_ball_list=[]
#     all_ball_num=[]
#     all_ball_set=set(all_ball)
#     for i in all_ball:
#         all_ball_list.append(i)
#     for j in all_ball_set:
#         n=all_ball_list.count(j)
#         all_ball_num.append(n)
#         if n<2:
#             return 0
#
#     # print(all_ball_num)
#     min_num=min(all_ball_num)
#     # print(min_num)
#     for i in all_ball_num:
#         if i%min_num!=0:
#             return 0
#
#     else:
#         return int(num)/min_num

# class Node():
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class Sign():
#     def __init__(self):
#         self.head=None
#
#     def add(self,value):#self.head是一直变化的
#         node=Node(value)
#         node.next=self.head
#         self.head=node
#
#     def travel(self):
#         temp=self.head
#         if self.head==None:
#             print('链表为空')
#         while temp:
#             print(temp.data)
#             temp=temp.next
#
#     def isEmpty(self):
#         return not bool(self.head)
#
#     def length(self):
#         if self.head==None:
#             print('链表为空')
#
#         temp=self.head
#         lenth=0
#         while temp:
#             temp=temp.next
#             lenth+=1
#         return lenth
#
#     def search(self,item):
#         """查找元素是否在链表中"""
#         find=False
#         if self.head==None:
#             print('链表为空')
#             return find
#         temp=self.head
#         while temp:
#             if temp.data==item:
#                 find=True
#                 break
#             temp=temp.next
#         return find
#
#     def append(self,item):
#         '''在链表后添加'''
#         node=Node(item)
#         if self.head==None:
#             self.head=node
#             return
#         cur=self.head
#         pre=None
#         while cur:
#             pre=cur
#             cur=pre.next
#         cur.next=node
#
#     def insert(self,pos,item):
#         if pos<0 or pos>self.length():
#             print('put of range')
#             return
#         node=Node(item)
#         cur=self.head
#         for i in range(pos):
#             pre=cur
#             cur=pre.next
#         pre.next=node
#         node.next=cur
#
#     def remove(self,item):
#
#         if self.head==None:
#             print('null')
#         if self.head.data==item:
#             self.head=self.head.next
#         cur = self.head
#         while cur:
#             pre=cur
#             cur=pre.next
#             if cur.data == item:
#                 pre.next=cur.next
#                 return
#     def reverse(self):
#         if self.head==None:
#             print('链表为空')
#         pre=None
#         cur=self.head
#         while cur:
#             next_none=cur.next
#             cur.next=pre
#             pre=cur
#             cur=next_none


# class Node():
#     def __init__(self,item):
#         self.item=item
#         self.next=None
# class Sing():
#     def __init__(self):
#         self.head=None
#
#     def add(self,item):
#         temp=Node(item)
#         pre=self.head
#         self.head=temp
#         temp.next=pre
#
#     def travel(self):
#         if self.head==None:
#             print('链表为空')
#         cur=self.head
#         while cur:
#             print(cur.item)
#             cur=cur.next
#     def isEmpty(self):
#         return not bool(self.head)
#     def search(self,item):
#         if self.head==None:
#             print('链表为空')
#         cur=self.head
#         find=False
#         while cur:
#             if cur.item==item:
#                 find=True
#                 break
#         return find
#     def length(self):
#         cur=self.head
#         length=0
#         while cur:
#             length+=1
#             cur=cur.next
#         return length
#
#     def append(self,item):
#         cur=self.head
#         if cur==None:
#             cur=Node(item)
#             return
#         while cur:
#             pre=cur
#             cur=cur.next
#
#         pre.next=Node(item)
#     def insert(self,pos,item):
#         if pos<0 or pos>self.length():
#             print('out of range')
#             return
#         cur=self.head
#         temp=Node(item)
#         for i in range(pos):
#             pre=cur
#             cur=cur.next
#         pre.next=temp
#         temp.next=cur
#     def remove(self,item):
#         if self.head==None:
#             print('链表为空')
#
#         if self.head.item==item:
#             self.head=self.head.next
#
#         cur=self.head
#         while cur:
#             pre=cur
#             cur=cur.next
#             if cur.item==item:
#                 pre.next=cur.next
#
#     def reverse(self):
#         if self.head==None:
#             print('链表为空')
#         cur=self.head
#         pre=None
#         while cur:
#             next_node=cur.next
#             cur.next=pre
#             pre=cur
#             cur=next_node
#         self.head=pre

from  queue import Queue
class Quenue2():
    def __init__(self):
        self.master_queue=Queue()
        self.mirror_queue=Queue()
    def push(self,item):
        self.master_queue.put(item)
    def pop(self):
        if self.master_queue==0:
            return None
        while True:
            if self.master_queue.qsize()==1:
                value=self.master_queue.get()
                break
            self.mirror_queue.put(self.master_queue.get())

        self.mirror_queue,self.master_queue=self.master_queue,self.mirror_queue
        return value

#冒泡
def sort_m(alist):
    n=len(alist)
    for i in range(n):
        for j in range(n-i-1):
            if alist[j]>alist[j-1]:
                alist[j],alist[j-1]=alist[j-1],alist[j]
    return alist

#选择
def sort(alist):
    for j in range(len(alist),1,-1):
        max_index=0
        for i in range(1,j):
            if alist[max_index]<alist[i]:
                max_index=i
        alist[max_index],alist[j-1]=alist[j-1],alist[max_index]

    return alist

#插入
def sort_c(alist):
    for i in range(1,len(alist)):
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i-=1
            else:
                break
    return alist

#希尔
def sort_x(alist):
    gap=len(alist)//2
    while gap>=1:
        for i in range(gap,len(alist)):
            while i>0:
                if alist[i]<alist[i-gap]:
                    i-=gap
                else:
                    break
        gap//=2
    return alist

            

def sort_cc(alist):
    for i in range(1,len(alist)):
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
            else:
                break
    return alist

def sort_xer(alist):
    gap=len(alist)//2
    while gap>=1:
        for i in range(gap,len(alist)):
            while i>0:
                if alist[i]<alist[i-gap]:
                    i-=gap
                else:
                    break
        gap//=2
    return alist

#选择(将列表中最大的值取出,放置列表的最右侧)
def sort_xz(alist):
    for i in range(len(alist),1,-1):
        max_index=0
        for j in range(1,i):
            if alist[max_index]<alist[j]:
                max_index=j
        alist[max_index],alist[i-1]=alist[i-1],alist[max_index]
    return alist


#插入排序(将乱序列表分成两个部分,一个乱序,一个有序)
def sort_crp(alist):
    for i in range(1,len(alist)):
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i-=1
            else:
                break
    return alist

#希尔排序
def sort_xrp(alist):
    gap=len(alist)//2
    while gap>=1:
        for i in range(gap,len(alist)):
            while i>0:
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    i-=1
                else:
                    break
        gap//=2




#冒泡
def MP(alist):
    n=len(alist)
    for i in range(n):
        for j in range(n-i-1):
            if alist[j]<alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
    return alist


class Node():
    def __init__(self,item):
        self.item=item
        self.next=None

class Link():
    def __init__(self):
        self.head=None

    def add(self,value):
        pre=self.head
        self.head=Node(value)
        self.head.next=pre
    def length(self):
        cur=self.head
        length=0
        while cur:
            cur=cur.next
            length+=1
        return length

    def append(self,item):
        if self.head==None:
            self.head=Node(item)
            return
        cur=self.head
        while cur:
            pre=cur
            cur=cur.next
        pre.next=Node(item)
    def isEmpty(self):
        return not bool(self.head)

    def insert(self,pos,value):
        if pos<0 or pos>self.length():
            print('insert error')
            return
        cur=self.head
        temp=Node(value)

        for i in range(pos):
            pre=cur
            cur=cur.next
        pre.next=temp
        temp.next=cur
    def search(self,item):
        cur=self.head
        find=False
        while cur:
            if cur.item==item:
                find=True
                break
            cur=cur.next
        return find

    def remove(self,item):
        cur=self.head
        if self.head==None:
            print('null')
        if self.head.item==item:
            self.head=cur.next

        while cur:
            pre = cur
            cur=cur.next
            if cur.item==item:
                pre.next = cur.next
                break


    def reverse(self):
        if self.head==None:
            print('NULL')
        cur=self.head
        pre=None
        while cur:
            next_node=cur.next
            cur.next=pre
            pre=cur
            cur=next_node
        self.head=pre






































