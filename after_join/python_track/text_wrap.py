import textwrap

def wrap(string, max_width):
    s = [*string]
    
    i = 1
    
    while i < len(s):
       
      
    
       if (i+1) % (max_width + 1) == 0:
        s.insert(i, '\n')
       i += 1
    return "".join(s)
    #return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)