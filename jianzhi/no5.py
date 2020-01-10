'''
题目：输入一个链表，从尾到头打印链表每个节点的值
'''
'''
方法一：使用extend，在尾部插入，其实最关键在于[::-1],只不过输入数据多样化，有可能还是集合，所以转成列表
这个方法效率应该还可以，先存入vector，再反转vector
26ms
5512k
'''
from jianzhi.shujujiegou_shixian import Node

headNode = Node('a',Node('b',Node('c',Node('d',Node('e',Node('f'))))))

class no5:
    def reverse(self,head):
        if head == None:
            return []
        result = []
        while head.next is not None:
            result.append(head.value)
            head = head.next

        result.append(head.value)
        return result[::-1]
my_rever = no5()
print(my_rever.reverse(headNode))









