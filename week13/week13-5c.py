#SOIT106_ADVANCE_009：進階題：函數反序排列數字(解法2)
a = int(input())
while a>0:
	print(a%10, end='')
	a = a // 10
print()