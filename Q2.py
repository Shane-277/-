D=int(input())
E=int(input())
R=D
for i in range(0,E):
    symbol=str(input())
    number=int(input())
    if symbol=='+':
        R+=number
    if symbol=='-':
        R-=number
print(R)