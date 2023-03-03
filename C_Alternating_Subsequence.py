t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mode = True if  a[0] > 0 else False
    current_max = a[0]


    # mdoe => True pos, False=> neg

    return_value = []
    
    for i in range(n):
        if a[i] > 0:
            if mode: #pos mode
                current_max = max(current_max, a[i]) #continue on
            else: # neg mode
                return_value.append(current_max) # save negative
                current_max = a[i]
                mode = True

        else: #neg number

            if mode:
                return_value.append(current_max)
                current_max = a[i]
                mode = False
            else:
                current_max = max(current_max, a[i])
    return_value.append(current_max)
   # print(return_value)


    # pos = float('-inf')
    # neg = float('-inf')
    # for i in range(n):
    #     if a[i] < 0:
    #        neg = max(a[i], neg)
    #     elif 
              

        # if mode: # pos
        #   if a[i] > 0 and current_max < a[i]:
        #     current_max = a[i]
        #   elif a[i] < 0:
        #     mode = False
        #     return_value.append(current_max)
        #     current_max = float('-inf')
        # else: # neg
        #    if a[i] < 0 and current_max < a[i]:
        #        current_max = a[i]
        #    elif a[i] > 0:
        #         mode = True
        #         return_value.append(current_max) 
        #         current_max = float('-inf')
                



    print(sum(return_value))
