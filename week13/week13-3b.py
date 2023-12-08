#SOIT106_BASE_004：基礎題：計程車資計算(解法2)
a = int(input())
if a<=2000:
	prirnt(100)
else: 
	print( 100+(a-2000+499)//500 * 5)