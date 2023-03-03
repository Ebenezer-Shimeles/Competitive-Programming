t = int(input())

for i in range(t):
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    
    if ( ((x+b) == a ) and (a == y) ) or ((a+y) == x and (b == x)) or ((a+x) == b and b == y) or ((b+y) ==x and x == a ):
        print('Yes')
    else:
        print("No")