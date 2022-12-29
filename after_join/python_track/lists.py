def process_command(cmd_data: list, l: list) -> None:
    '''This function accepts a list of command and it's data '''
    
    cmd = cmd_data[0]
    if  cmd == 'print':
        print(l)
    elif cmd == 'append':
        l.append(int(cmd_data[1]));
    elif cmd == 'insert':
        l.insert(int(cmd_data[1]), int(cmd_data[2]))
    
    elif cmd == 'remove':
        l.remove(int(cmd_data[1]))
    elif cmd == 'pop':
        l.pop()
    elif cmd == 'reverse':
        l.reverse()
    elif cmd == 'sort':
        l.sort()

if __name__ == '__main__':
    N = int(input())
    l = list()
    for i in range(N):
        #read commands here
        cmd_raw = input()
        cmd = cmd_raw.split()
        process_command(cmd, l)

