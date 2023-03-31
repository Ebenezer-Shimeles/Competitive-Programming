n, l, r = map(int, input().split())
a = list(map(int, input().split()))

start, right = 0, 1
curr_sum = a[0]
count = 0
if n == 1:
    if a[0] >= l and a[0] <= r:
         print(1)
    else:
         print(0)
else:
    while right < n:
        if curr_sum >= l and curr_sum <= r:
            count += 1
       
        

        while curr_sum > r:
                curr_sum -= a[start]
                print(start, right, curr_sum)
               
                if start == r:
                    right = start +1
                    start += 1
                    
                    break
                start += 1
        if right < n:
                curr_sum += a[right]

        right += 1
    if curr_sum >= l and curr_sum <= r:
            count += 1

print(count)

