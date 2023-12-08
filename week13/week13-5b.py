#SOIT106_ADVANCE_009：進階題：函數反序排列數字(解法1)
a = input()
N = len(a)
for i in range(N-1, -1, -1):
	print( a[i], end='')
print() 