#-*- coding:utf-8 -*-

# 描述：
# 
# 利用python实现简化版描述函数
# 输入：
# 
# a : 一维数组; 示例输入 : [1.0,2.0,3.0]
# 
# 输出：
# 
# [mean,var,skew,kurt]分别代stan_de、方差、偏度、峰度；示例输出 : [2.000000,1.000000,0.000000,-1.500000]
# 
# 注意：
# 
# （1）不能调用math、scipy、numpy包
# 
# （2）数组只有一个元素时，方差值返回None
# 
# （3）结果保留6位小数点

import numpy
class Solution():
    def describe(self, a):
        aver = self.average(a)
        var = self.variance(a, aver)
        skew = self.skewness(a, aver, var)
        kurt = self.kurtosis(a, aver, var)
        
        print[aver,var,skew,kurt]
        
        res = [round(aver,6),None,round(skew,6),round(kurt,6)]
        if var != None:
            res = [round(aver,6),round(var,6),round(skew,6),round(kurt,6)]
        return res
    
    def average(self, a):
        sum = 0;
        for ele in a:
            sum = sum + ele
        return (float(sum)/len(a))
    
    def variance(self, a, aver):
        if len(a)==1:
            return None
        sum = 0;
        for ele in a:
            b = ele - aver
            sum = sum + b**2;
        return (float(sum)/(len(a)-1))
    
    def skewness(self, a, aver, var):
        if var == None:
            return 0
        if var == 0:
            return 0
        b3 = 0
        for ele in a:
            b = ele - aver
            b3 = b3 + b**3;
        b3 = b3/len(a)
        res = float(b3)/((var*(len(a)-1)/len(a))**1.5)
        return res
    
    def kurtosis(self, a, aver, var):
        if var == None:
            return -3
        if var == 0:
            return -3
        b4 = 0
        for ele in a:
            b = ele - aver
            b4 = b4 + b**4;
        b4 = b4/len(a)
        res = float(b4)/((var*(len(a)-1)/len(a))**2)
        return res - 3
    
if __name__ == '__main__':
    solution = Solution();
    solution.describe([1.0,2.0,3.0])
#     solution.describe([1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751])
#     solution.describe([473, 1, 39, 1, 137, 2, 20.33, 30923.406973907633])
#     solution.describe([2])
    

