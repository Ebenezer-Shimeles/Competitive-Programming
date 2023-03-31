



def make_goog_min(s: str, c: str, dir: bool):
    N = len(s)
    if N == 1:
      if c ==s[0]:
          return 0
      else: return 1

  
    next = chr(ord(c)+1)

    
    

    last_str = s[N//2:]
    first_str = s[:N//2]
    #print('mode = ', dir, )
    if dir: # take the last
        b_count = 0
        for ch in last_str:
           if ch != c:
              b_count += 1
        return b_count + min(
                make_goog_min(first_str, next, True),
                make_goog_min(first_str, next, False),
            )
    else:
        b_count = 0
        for ch in first_str:
           if ch != c:
              b_count += 1
        return b_count + min(
                make_goog_min(last_str, next, True),
                make_goog_min(last_str, next, False),
            )





import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    # write your code here

    t = int(input())


    for _ in range(t):
        n = int(input())
        s = input()
        #print('given ', s)
    
        print(min(make_goog_min(s, 'a', True), make_goog_min(s, 'a', False)))




if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()




