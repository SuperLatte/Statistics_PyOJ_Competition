#-*- coding:utf-8 -*-

# 描述：
# 
# 仍然利用NSFG数据（url为http://112.124.1.3:8050/getData/101），验证母亲年龄Y对婴儿出生体重W是否有影响。假设Y=a+bW， 试写函数solve利用最小二乘法拟合a,b的值，并且计算其测定系数r2
# 输入：
# 
# 调查样本数据，格式为{“status”:"ok","data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}
# 
# 输出：
# 
# [a,b,r2]
# 
# 注意：

import urllib
import json
class Solution:
    def solve(self):
        html = self.getHtml('http://112.124.1.3:8050/getData/101')
        data = json.loads(html)["data"]
        n = len(data)
        Y=[]
        W=[]
        for i in range(n):
            W.append(data[i][6])
            Y.append(data[i][4])
        n = len(Y)

        Ymean = self.mean(Y)
        Xmeam = self.mean(W)
        lxy = self.proSum(W, Y)-(1/float(n))*self.sum(W)*self.sum(Y)
        lxx = self.var(W)
        
        b = lxy/lxx
        a = Ymean-b*Xmeam
        
        sr = 0
        st = 0
        for i in range(n):
            sr = sr + (a+b*W[i]-Ymean)**2
            st = st + (Y[i]-Ymean)**2
        r2 = sr/st
        return [a,b,r2]
        
        
    def sum(self, x):
        sum = 0
        for i in x:
            sum = sum + i
        return sum
    
    def mean(self, x):
        mean = float(sum(x))/len(x)
        return mean

    def var(self, x):
        mean = self.mean(x)
        var = 0
        for i in x:
            var = var + (i-mean)**2
        return var
    
    def proSum(self, x, y):
        sum = 0
        for i in range(len(x)):
            sum = sum + x[i]*y[i]
        return sum
        
    def getHtml(self, url):
        page = urllib.urlopen(url)
        html = page.read()
        return html
    
if __name__=='__main__':
    solution = Solution()
    print solution.solve()