'''
题目：请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
class no4:
    def replaceSpace(self,s):
        return s.replace(' ','%20')

s =  no4()
print(s.replaceSpace("we are happy"))