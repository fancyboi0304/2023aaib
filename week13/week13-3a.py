#SOIT106_BASE_004：基礎題：計程車資計算(解法1)
a = int(input())
if a <= 2000:
	ans = 100
else:
	a -= 2000
	ans = 100 + a//500 * 5
	if a%500: ans += 5

print(ans)