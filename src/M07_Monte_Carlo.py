#-*- coding:utf-8 -*-

# 描述：
# 
# 蒙特卡罗方法，或称计算机随机模拟方法，是一种基于随机数的计算方法，在金融工程学，宏观经济学，计算物理学等领域应用广泛。
# 试编写函数solve(a,b)，利用蒙特卡罗方法计算函数f(x)=(e^(-x²/2))/√2√π在区间[a,b]上的定积分并返回，其中b>a>0。
# 
# 输入：
# 
# a,b分别为正浮点数
# 
# 输出：
# 
# m: 定积分值
# 
# 注意：
# 
# （1）为保证精确性，蒙特卡罗模拟次数至少为100000
# 
# （2）不能使用scipy.integrate库

import math
import random
# class Solution:
#       
#     def solve(self,a,b):
#         n = 100000
#         l = (float(b)-float(a))/n
#         m = 0
#         y = lambda x: (math.exp(-x*x/2))/math.sqrt(2*math.pi)
#         for i in range(n) :
#             m = m + l*y(a+l*i)
#         return m

class Solution:
       
    def solve(self,a,b):
        n = 1000000
        m = 0
        y = lambda x: (math.exp(-x*x/2))/math.sqrt(2*math.pi)
        for i in range(n):
            if random.uniform(0,1) <= y(random.uniform(a,b)):
                m += 1
        return float(m)/n*(b-a)
   
if __name__ == '__main__':
    solution = Solution();
    print solution.solve(1,2.5)