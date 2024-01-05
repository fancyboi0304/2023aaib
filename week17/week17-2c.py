#SOIT108_Advance_011
a = int(input())

hour = a//60//60
minute = a//60%60
second = a%60

print(f'{hour:02}:{minute:02}:{second:02}',end='')