#code
#Minimum number to form the sum even
t = int(input())
while t >0:
    a = 0
    n = int(input())
    l = list(map(int,input().split()))
    for i in range(n):
        a += i
    if a%2 == 0:
        print(2)
    else:
        print(1)
    
    t-=1
