class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        ans = 1
        for i in nums:
            ans *= i
        
        if ans>0: return 1
        if ans==0: return 0 
        if ans<0: return -1