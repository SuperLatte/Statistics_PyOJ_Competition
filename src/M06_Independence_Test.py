#-coding:utf-8-

# 描述：
# 
# 利用python实现简化版独立检验函数
# 输入：
# 
# A为二维数组，每行代表总体X的一个水平上的取值，每列代表总体Y的一个水平上的取值；示例输入 : [[1.0,2.0,3.0],[2.0,2.0,3.0]]
# 
# 输出：
# 
# [c-val,p-value]分别代表检验结果C值与其对应的P值；示例输出 : [0.257937,0.879002]
# 
# 注意：
# 
# （1）A中只有一行时，返回结果为[0.0,None]
# 
# （2）结果保留6位小数点

from scipy.stats import chi2 as C
class Solution():
    def independence_test(self, A):
        length = len(A)
        if length==1:
            return [0.0,None]
        
        n = 0
        ni = []
        nj = []
        for i in range(length):
            sum = 0
            for ele in A[i]:
                n = n + ele
                sum = sum + ele
            ni.append(sum)
        
        for i in range(len(A[0])):
            sum = 0
            for j in range(length):
                sum = sum + A[j][i]
            nj.append(sum)
            
        T = []
        for i in ni:
            tmp = []
            for j in nj:
                tmp.append(float(i*j)/n)
            T.append(tmp)
        
        c2 = 0
        for i in range(length):
            for j in range(len(A[0])):
                c2 = c2 + (A[i][j]-T[i][j])**2/T[i][j]
        
        p = C.sf(c2, (length-1)*(len(A[0])-1))
        return [round(c2,6),round(p,6)]

        
    
if __name__ == '__main__':
    solution = Solution()
    print solution.independence_test([[1.0,2.0,3.0],[2.0,2.0,3.0]])