



    
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    # write your code here
   
    N, T = map(int, input().split())
 
    a = list(map(int, input().split()))
    s = sum(a)
    N = len(a)

    def check(s, N, l, r):
        if l>r:
            return 0
        
        while s > T and l<=r:
            N -=1
            if a[l] > a[r]:
                s -= a[l]
                l += 1
            elif a[r] > a[l]:
                s -= a[r]
                r -= 1
            else:
                return max(check(s-a[l], N, l+1, r), check(s-a[r], N, l, r-1),)
        
        return N
    print(check(s, N, 0, N-1))

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




