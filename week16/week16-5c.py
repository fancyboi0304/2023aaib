#SOIT108_Advance_002B
a = list(map(int,input().split()))
a.sort()

print(a[2]*100+a[1]*10+a[0]*1+1,end='')