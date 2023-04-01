from collections import defaultdict
t = int(input())

def func(m: defaultdict, root: int, c_value:list,t_value: list):
    '''
       Goes to the last and adds the max-path
    '''
    verts = m[root]
    c_value.append(root)
    
    N = len(verts)
    if N == 0:
        t_value.append(c_value)
        return
    
    for i in range(1, N):
        func(m, verts[i],[], t_value)
    func(m, verts[0], c_value, t_value)
  

# def max_len(m: defaultdict, root: int):
#     verts = m[root]
#     # print(verts)
#     N = len(verts)

#     if N == 0:
#         return 1
#     elif N == 1:
#         return 1+ max_len(m, verts[0])
#     elif N == 2:
#         return 1 + max(max_len(m, verts[0]), max_len(m, verts[1]))



import sys, threading

input = lambda: sys.stdin.readline().strip()


def run():
    for _ in range(t):
        n = int(input())
        ords = list(map(int, input().split()))
    
        m = defaultdict(list)
        root = None
        result = []
        for i, o in enumerate(ords):
            if o != i +1:
                m[o].append(i+1)
            else:
                root = i + 1
        func(m, root, [], result)
        # print(root, m)
        print(len(result))
        for res in result:
            print(len(res))
            print(*res)
        print('')
        #print(max_len(m, root))



if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=run)
    main_thread.start()
    main_thread.join()