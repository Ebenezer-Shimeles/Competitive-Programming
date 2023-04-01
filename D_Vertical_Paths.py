from collections import defaultdict
t = int(input())

def func(m: defaultdict, root: int, c_value:list,t_value: list):
    '''
       Goes to the last and adds the max-path
    '''
    verts = m[root]
    N = len(verts)
    c_value.append(root)
    if N == 0:
        t_value.append(c_value)
    elif N == 1: #only one node
        
        func(m, verts[0], c_value, t_value)
    elif N == 2:
        l_len = max_len(m, verts[0])
        r_len = max_len(m, verts[1])

        if l_len > r_len:
            func(m, verts[0], c_value, t_value)
            func(m, verts[1], [], t_value)
        else:
            func(m, verts[1], c_value, t_value)
            func(m, verts[0], [], t_value)
    else:
        max_vert = -1
        max_l = float('-inf')
        for vert in verts:
            l = max_len(m, vert)
            if l > max_l:
                if max_vert != -1:
                    func(m, max_vert, [], t_value)
                max_l = l
                max_vert = vert
            else:
                func(m, vert, [], t_value)
        func(m, max_vert, c_value, t_value)


def max_len(m: defaultdict, root: int):
    verts = m[root]
    # print(verts)
    N = len(verts)

    if N == 0:
        return 1
    elif N == 1:
        return 1+ max_len(m, verts[0])
    elif N == 2:
        return 1 + max(max_len(m, verts[0]), max_len(m, verts[1]))

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

import sys, threading

input = lambda: sys.stdin.readline().strip()



if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=run)
    main_thread.start()
    main_thread.join()