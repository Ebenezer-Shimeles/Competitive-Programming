n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
 
def get(num):
    l, r,last = 0, N - 1, N-1
    while l <=r:
            mid = (l+r)//2

            if a[mid] <= num:
                if mid == N-1:
                    return N
                if a[mid+1] > num:
                    return mid + 1
                else:
                    l = mid + 1
            else:
                r = mid - 1
N = len(a)
res = []
for num in b:
   
    if num < a[0]:
        print(0, end = ' ')
    else:
        print(get(num), end = ' ')
       





print(*res)