#-*- coding:utf-8 -*-

# 描述：
# 
# 利用python实现简化版单总体T检验函数
# 输入：
# 
# a : 非空一维数组；popmean：假设总体期望值；示例输入 : [1.0,2.0,3.0],2.0
# 
# 输出：
# 
# [t-val,p-value]分别代表检验结果T值与其对应的P值；示例输出 : [0.000000,1.000000]
# 
# 注意：
# 
# （1）scipy包只能使用scipy.x.ppf或scipy.x.sf函数
# 
# （2）结果保留6位小数点

from scipy.stats import t as T
class Solution():
    def ttest_1samp(self, a, popmean):
        n = len(a)
        mean = self.mean(a)
        
        t = (mean-popmean)/(self.stan_de(a, mean)/(n**0.5))
        p = 2*T.sf(abs(t),n-1)
        return [round(t,6),round(p,6)]
    
    def stan_de(self, x, mean):
        sum = 0
        for i in x:
            sum = sum + (i-mean)**2
        var = sum/(len(x)-1)
        return var**0.5
        
    
    def sum(self, x):
        sum = 0
        for i in x:
            sum = sum + i
        return sum
    
    def mean(self, x):
        sum = self.sum(x)
        mean = float(sum)/len(x)
        return mean
    
if __name__=='__main__':
    solution = Solution()
#     print solution.ttest_1samp([1.0,2.0,3.0],2.0)
    print solution.ttest_1samp([159,280,101,212,224,379,179,264,222,362,168,250,149,260,485,170],225)