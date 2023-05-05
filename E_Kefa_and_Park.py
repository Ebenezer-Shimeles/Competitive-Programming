from collections import defaultdict




import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n, J = map(int, input().split())
 
    a = list(map(int, input().split()))
    m = defaultdict(list)
    m[1] = []
    k = set()
    def ways(root, b_count):
        print(' bad')
        global k
        if a[root-1] == 1:
            b_count +=1
        else:
            b_count = 0
        if b_count > J:
        
            return
        
        children = m[root]
        if not len(children) or not children:
            k.add(root)
            #(f'root: {root} {children} {m}')
        for child in children:
            ways(child, b_count)


    ###
   
    for i in range(n - 1):
        x, y = map(int, input().split())
        m[x].append(y)
        m[y].append(x)
    ways(1, 0)
    # print(m)
    print(len(k))
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()