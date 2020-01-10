from jianzhi.shujujiegou_shixian import TreeNode
"""
输入二叉树的前序遍历和中序遍历结果，重建该二叉树
"""
class no6:

    def biTree(self,pre,mid):
        if not pre or not mid:
            return None
        root = TreeNode(pre[0])
        count = mid.index(root.value)
        #print(count)

        root.Lchild = self.biTree(pre[1:count+1],mid[:count])
        root.Rchild = self.biTree(pre[count+1:],mid[count+1:])
        return root
    #后序遍历
    def postTravel(self,root):
        if not root:
            return None
        self.postTravel(root.Lchild)
        self.postTravel(root.Rchild)
        print(root.value)
    #按层遍历，使用队列
    def printFromTop(self,root):
        outList = []
        queue = [root]
        while queue!=[] and root:
            outList.append(queue[0].value)
            if queue[0].Lchild!=None:
                queue.append(queue[0].Lchild)
            if queue[0].Rchild!=None:
                queue.append(queue[0].Rchild)
            queue.pop(0)
        return outList
    #按层遍历，不使用队列
    def printFromtop2(self,root):
        if not root:
            return []
        currentStack = [root]
        outlist = []
        while currentStack:
            nextStack = []
            for item in currentStack:
                if item.Lchild:
                    nextStack.append(item.Lchild)
                if item.Rchild:
                    nextStack.append(item.Rchild)
                outlist.append(item.value)
            currentStack = nextStack
        return outlist
    #按层输出,输入为根节点，用队列实现
    def printbylevel(self,root):
        queue = [root]
        res = []   #最终输出的数组
        if not root:
            return []
        while queue!=[]:
            templist = []   #每一层形成的数组
            templen = len(queue) #每层数组的长度
            for i in range(templen):
                temp = queue.pop(0)
                templist.append(temp.value)
                if temp.Lchild:
                    queue.append(temp.Lchild)
                if temp.Rchild:
                    queue.append(temp.Rchild)
            res.append(templist)
        return res
    #按层输出，输入为根节点，不用队列实现
    def printbylevel2(self,root):
        queue = [root]
        res = []
        if not root:
            return []
        while queue:
            nextqueue = []   #当前数组
            templist = []   #每一层形成的数组
            for point in queue:
                templist.append(point.value)
                if point.Lchild:
                    nextqueue.append(point.Lchild)
                if point.Rchild:
                    nextqueue.append(point.Rchild)
            queue = nextqueue
            res.append(templist)
        return res






mytree = no6()
pre = [1,2,4,7,3,5,6,8]
mid = [4,7,2,1,5,3,8,6]
root = mytree.biTree(pre,mid)
mytree.postTravel(root)
list = mytree.printFromTop(root)
print(list)
list2 = mytree.printFromtop2(root)
print(list2)
list3 = mytree.printbylevel(root)
print(list3)
list4 = mytree.printbylevel2(root)
print(list4)



