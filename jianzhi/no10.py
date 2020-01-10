'''
题目：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n<0:
            n = n & 0xffffffff
            print(n)
        while n:
            count += 1
            n = n & (n-1)
        return count


my = Solution()
print(my.NumberOf1(-11))




