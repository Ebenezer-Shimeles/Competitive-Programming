def solution():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        if n == 1:
            print('YES')
            continue
      
        '''
            We need to sort this 
            then check if adjecent number's difference is <=1 
        '''
        yes = True
        nums.sort()
        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) > 1:
                print('NO')
                yes = False
                break
        if yes:
            print('YES')

if __name__ == '__main__':
    solution()