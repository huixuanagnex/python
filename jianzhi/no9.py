'''
题目：
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

class fibonacci():
    def findN(self,n):
        if n<=0:
            return 0
        if n==1:
            return 1
        return self.findN(n-1)+self.findN(n-2)
    #不使用迭代
    def findN2(self,n):
        res = [0,1]
        while len(res) <= n:
            res.append(res[-1]+res[-2])
            #print("n:"+str(res[-1]))
        return res[n]

sol = fibonacci()
print(sol.findN2(6))