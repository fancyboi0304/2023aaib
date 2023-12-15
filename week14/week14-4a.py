#SOIT107_Base_002(解法1)
a = int(input())

if a <= 1500: ans = 100
else:
	ans = 100 + (a-1500)// 250 * 5
	if ((a-500) % 250) > 0:
		ans += 5
		
print(ans,end='')