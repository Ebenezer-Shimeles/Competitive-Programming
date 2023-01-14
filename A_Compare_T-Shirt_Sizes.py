'''We just need to check if it"s not only m, s or l come last or s and l are mixed'''

t = int(input())

for i in range(t):
    size_one, size_two = input().split()
    l_one = len(size_one)
    l_two = len(size_two)

    if size_one[-1] == 'L':
        if size_two[-1] != 'L':
            print('>')
        else:
            if l_one == l_two:
                print('=')
            else:
                print('>' if l_one > l_two else '<')
    elif size_one[-1] == 'M':
        if size_two[-1] == 'L':
            print('>')
            
        elif size_two[-1] == 'S':
            print('<')
        else:
            if l_one == l_two:
                print('=')
            else:
                print('>' if l_one > l_two else '<')
    elif size_one[-1] == 'S':
        if size_two[-1] != 'S':
            print('<')
        else:
            if l_one == l_two:
                print('=')
            else:
                print('<' if l_one > l_two else '>')

    