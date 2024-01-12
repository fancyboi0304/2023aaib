#LeetCode 1704. Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        motherA = 0 #a的母音有幾個
        motherB = 0 #a的母音有幾個
        N = len(s) #字串的長度 ex. s='textbook'
        a = s[:N//2] #前半段   a='text'
        b = s[N//2:] #後半段   b='book'
        for c in a: #在a裡面的每一個字母c逐一檢查
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                motherA += 1
            elif c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
                motherA += 1
        for c in b: #在b裡面的每一個字母c逐一檢查
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                motherB += 1
            elif c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
                motherB += 1
        if motherA == motherB: return True
        else: return False

