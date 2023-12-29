#SOIT108_Advance_001
a = int(input())
ans = 0
for i in range(1,1001):
	if i**2 == a:
		ans = i
print(ans,end='')