#-*- coding:utf-8 -*-

# 描述：
# 
# 仍然利用NSFG数据（url为http://112.124.1.3:8050/getData/101），但这次我们想验证第一胎婴儿是否更倾向于更早或更晚出生而较少准时出生的假设，因此需要利用卡方检验计算出其卡方值chisq及推翻假设的p值。
# 试写函数solve计算卡方值chisq及p值
# 输入：
# 
# 调查样本数据，格式为{“status”:"ok","data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}
# 
# 输出：
# 
# [chisq,p]
# 
# 注意：
# 
# （1）婴儿第几周出生数据由于被调查人选填错误等原因出现了一些不合理数据，比如错填了月份（5<prglength<=10），其他错填（prglength<=5, 10<prglength<=25, prglength>=49），对于错填月份的情况，将月份*4.33作为其周数，对于其他错填情况则舍弃此条数据
# 
# （2）一般认为，如果婴儿在第37周或更早出生，那就是提前出生；准时出生则是在第38周到第40周；而延后出生则是在41周或更晚


import urllib
import json
from scipy.stats import chi2 as C
class Solution:
    def solve(self):
        html = self.getHtml('http://112.124.1.3:8050/getData/101')
        data = json.loads(html)["data"]
        
        T1 = []
        T2 = []
        
        for i in range(len(data)):
            a = data[i][2]
            if ((a<=5) | (a>=49) | ((a>10)&(a<=25))):
                continue
            if ((a<=10)&(a>5)):
                a = 4.33*a 
            if (data[i][5] == 1):
                T1.append(a)
            T2.append(a)
        
        n1 = len(T1)
        n2 = len(T2)
        
        a1=0
        b1=0
        d1=0
        for i in T1:
            if (i < 38):
                a1 = a1 + 1
            elif i>=41:
                d1 = d1 +1
            else:
                b1 = b1 + 1
        a2=0
        b2=0
        d2=0
        for i in T2:
            if (i < 38):
                a2 = a2 + 1
            elif i>=41:
                d2 = d2 +1
            else:
                b2 = b2 + 1
        
        t1 = float(a2)*n1/n2
        t2 = float(b2)*n1/n2
        c2 = float(a1**2)/(n1*float(a2)/n2)+float(b1**2)/(n1*float(b2)/n2)+float(d1**2)/(n1*float(d2)/n2)-n1
        p = C.sf(c2,2)
        return [c2,p]
    
    def getHtml(self, url):
        page = urllib.urlopen(url)
        html = page.read()
        return html
    
if __name__=='__main__':
    solution = Solution()
    print solution.solve()