class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:  #因為1是2^0不用再除了
            if n % 2 != 0:
                return False
            n = n // 2
        return True