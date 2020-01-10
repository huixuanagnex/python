"""
用python实现链表，二叉树，栈，队列
"""

#节点
class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    def set_value(self,new_value):
        self.value = new_value
    def set_next(self,new_next):
        self.next = new_next
    def __str__(self):
        return "Value = %s" % self.value

class TreeNode:
    def __init__(self,value,left = None,right = None):
        self.value = value
        self.Lchild = left
        self.Rchild = right
    def set_value(self,value):
        self.value = value
    def set_Lchild(self,left):
        self.Lchild = left
    def set_Rchild(self,right):
        self.Rchild = right








#链表
