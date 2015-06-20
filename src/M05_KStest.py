#-*- coding:utf-8 -*-


# 描述：
# 
# 利用python实现简化版双样本K-S检验函数
# 输入：
# 
# a,b分别为非空一维数组；示例输入 : [1.0,2.0,3.0],[1.0,2.0,3.0]
# 
# 输出：
# 
# ks-value为检验结果KS值；示例输出 : 0.333333
# 
# 注意：
# 
# （1）不能调用math、scipy、numpy包

from scipy.stats import ks_2samp as KS
class Solution():
    def ks_2samp(self, data1, data2):
        ks = 0
        len1 = len(data1)
        len2 = len(data2)
        for i in data1:
            n1 = 0
            for f in data1:
                if f <= i:
                    n1 = n1 + 1
            n2 = 0
            for g in data2:
                if g <= i:
                    n2 = n2 + 1
            tmp = abs(float(n1)/len1-float(n2)/len2)
            if tmp>ks:
                ks=tmp
        return round(ks,6)

if __name__ == '__main__':
    solution = Solution()
    print solution.ks_2samp([1.1,2.3,3.5],[2.6,2.7,3.8,4.9])
