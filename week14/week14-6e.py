#SOIT107_Base_011(考試)
a, c, b = input().split()

if c=='+': ans = int(a)+int(b)
if c=='-': ans = int(a)-int(b)
if c=='*': ans = int(a)*int(b)
if c=='/': ans = int(a)//int(b)

print(ans,end='')

