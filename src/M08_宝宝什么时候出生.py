#-*- coding:utf-8 -*-
'''
Created on 2015年6月18日

@author: puddi_000
'''

# 描述：
# 
# 美国疾病控制与预防中心（CDC）从1973年开始推行全国家庭成长调查（NSFG），目的是收集（美国）“家庭的生活、婚姻状况、生育、避孕和男女健康信息。”
# 现有从2002年1月到3月收集的调查数据（url为http://112.124.1.3:8050/getData/101），包含上万条调查数据，每条数据包括 caseid（标识符）, prglength（婴儿第几周出生）, outcome（怀孕结果，1表示活产）, totalwgt_oz（婴儿出生重量，单位盎司）, birthord（第几胎,1表示第一胎）, agepreg（怀孕时年龄）, finalwgt（被调查者的统计权重，表明这名调查者所代表的人群在美国总人口中的比例。过采样人群的权重偏低）等信息
# 另据某研究显示，婴儿出生周数符合方差为16的正态分布，试写函数solve估计婴儿平均出生周数的置信区间（置信水平为95%）。
# 输入：
# 
# 调查样本数据，格式为{“status”:"ok","data":[[1, 1, 39, 1, 141, 1, 33.16, 6448.271111704751], [1, 2, 39, 1, 126, 2, 39.25, 6448.271111704751], ...]}
# 
# 输出：
# 
# [lower,upper]分别代表平均出生周数的估计下限与上限
# 
# 注意：
# 
# （1）婴儿第几周出生数据由于被调查人选填错误等原因出现了一些不合理数据，比如错填了月份（5<prglength<=10），其他错填（prglength<=5, 10<prglength<=25, prglength>=49），对于错填月份的情况，将月份*4.33作为其周数，对于其他错填情况则舍弃此条数据

import urllib
import json
from scipy.stats import norm as N
class Solution:
    def solve(self):
        html = self.getHtml("http://112.124.1.3:8050/getData/101")
        data = json.loads(html)["data"]
        aver = 0;
        n = 0
        for i in range(len(data)) :
            a = data[i][2]
            if ((a<=5) | (a>=49) | ((a>10)&(a<=25))):
                continue
            if ((a<=10)&(a>5)):
                a = 4.33*a
            aver = aver + a
            n = n + 1
        aver = aver / n
        return [aver-(4/n**0.5)*N.ppf(0.975), aver+(4/n**0.5)*N.ppf(0.975)]
    
    def getHtml(self, url):
        page = urllib.urlopen(url)
        html = page.read()
        return html
    
if __name__=="__main__":
    solution = Solution()
    solution.solve() 
    
    
    N.s