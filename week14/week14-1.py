#Leetcode 1436. Destination City
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notAns = set()
        
        for a,b in paths: #先巡第1輪
            notAns.add(a) #出發點,不是答案


        for a,b in paths:  #先巡第2輪
            if b not in notAns:  #b不在出發裡,就是答案
                return b  #b不是"不是答案"