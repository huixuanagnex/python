'''
题目：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减排序的数组的一个旋转，输出旋转数组的
最小元素。例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。NOTE：给出的所有元素都大于0，若数组大小为0，
请返回0。
'''
class turnList():
    def findMin(self,arr):
        index1 = 0
        index2 = len(arr)-1
        mid = 0
        while arr[index1] >= arr[index2]:
            if index2-index1 ==1:
                mid = index2
                break
            mid = (index1 + index2)//2
            #如果存在三者相同的情况
            if arr[mid] == arr[index1] and arr[mid] == arr[index2]:
                #print(index1,index2 )
                return self.findinorder2(index1,index2,arr)

            if arr[index1] <= arr[mid]:
                index1 = mid
            elif arr[index2] >= arr[mid]:
                index2 = mid
        return arr[mid]
    def findinorder(self,index1,index2,arr):
        temp = arr[index1]
        while index2>=index1:
            if arr[index1]<temp:
                temp = arr[index1]
            index1+=1
        return temp
    #另一种
    def findinorder2(self,index1,index2,arr):
        result = arr[index1]
        for i in arr[index1:index2+1]:
            if i<result:
                result = i
        return result
mysolve = turnList()
list = [3,4,5,1,2]
list2 = [9,10,11,1,2,3,4,5,6,7,8]
list3 = [2,3,3,4,1,2]
min = mysolve.findMin(list3)
print(min)







            

