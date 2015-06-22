#-*- coding:utf-8 -*-

# 描述：
# 
# 利用python实现简化版皮尔森相关系数计算函数
# 输入：
# 
# x : 一维数组；y : 一维数组，且x、y长度相同；示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]
# 
# 输出：
# 
# [r-val,p-value]分别代表皮尔森相关系数、检验结果P值；示例输出 : [0.866025,0.333333]
# 
# 注意：
# 
# （1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
# 
# （2）x,y为空时，返回值为[None,None]
# 
# （3）结果保留6位小数点

from scipy.stats import t as T
class Solution():
    def pearsonr(self, x, y):
        n = len(x)
        if n==0:
            return [None,None]
        r = (n*self.proSum(x, y)-self.summary(x)*self.summary(y))/(((n*self.squareSum(x)-self.summary(x)**2)*(n*self.squareSum(y)-self.summary(y)**2))**0.5)
        t = r*(float(n-2)/(1-r**2))**0.5
        p = 2*T.sf(abs(t), n-2)
        return [round(r,6),round(p,6)]
    def mean(self, x):
        sum = self.summary(x);
        mean = float(sum)/len(x)
        return mean
    
    def summary(self, x):
        sum = 0
        for i in x:
            sum = sum + i
        return sum
    
    def squareSum(self, x):
        sum = 0
        for i in x:
            sum = sum + i**2
        return sum
    
    def proSum(self, x, y):
        sum = 0
        for i in range(len(x)):
            sum = sum + x[i]*y[i]
        return sum
    
    
    
if __name__=='__main__':
    solution = Solution()
    print solution.pearsonr([1.0,2.0,3.0],[2.0,2.0,3.0])