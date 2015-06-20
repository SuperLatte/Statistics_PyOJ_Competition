#-*- coding:utf-8 -*-

# 描述：
# 
# 利用python实现简化版单因素方差检验函数
# 输入：
# 
# sample1,sample2,... : 不定数量（至少一个）的一维数组；示例输入 : [1.0,2.0,3.0],[2.0,2.0,3.0]
# 
# 输出：
# 
# [F-value, p-value]分别代表检验结果F值与其对应的P值；示例输出：[0.250000，0.643330]
# 
# 注意：
# 
# （1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
# 
# （2）sample_i为空时，返回值为[None,None]
# 
# （3）结果保留6位小数点

from scipy.stats import f as F
class Solution():
    def f_oneway(self, *args):
        m = len(args)
        if m==0:
            return [None,None]
        r = len(args[0])
        if r==0:
            return [None,None]
        
        n = r*m
        mean = self.mean(args)
        
        sa = 0
        for i in args:
            sa = sa + (self.meani(i)-mean)**2
        sa = sa * r
        va = sa/(m-1)
        
        se = 0
        for i in args:
            for j in i:
                se = se + (j-self.meani(i))**2
        ve = se/(n-m)
        f = va/ve
        p = F.sf(f,m-1,n-m)
        return [round(f,6),round(p,6)]
    
    
    def meani(self, x):
        sum = 0
        for i in x:
            sum = sum + i
        return float(sum)/len(x)
       
    def mean(self, x):
        sum = 0
        for i in x:
            for j in i:
                sum = sum + j
        return float(sum)/len(x)/len(x[0])
    
if __name__=='__main__':
    solution = Solution()
    print solution.f_oneway([1.0,2.0,3.0],[2.0,2.0,3.0])