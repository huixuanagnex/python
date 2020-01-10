'''
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
方法一： 循环迭代查找，不是最优
284ms
5760k
'''
class no3_1:
    def Find(self,target,array):
        if not array:
            return
        row = len(array)
        col = len(array[0])

        for i in range(row):
            for j in range(col):
                if target == array[i][j]:
                    return True
        return False

class no3_2:
    def Find(self,target,array):
        if not array:
            return
        row = len(array)
        col = len(array[0])

        i = 0
        j = col-1

        while i < row and j>=0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                 j -=1
            else:
                i+=1
        return False




array = [[1,2,8,9],
         [2,4,9,12],
         [4,7,10,13],
         [6,8,11,15]]

#my_test = no3_1()
my_test = no3_2()
result = my_test.Find(7,array)
if result is True:
    print("find it")






