def swap_case(s):
    array = [*s];
    #print(f'Array {array}')
    for i in range(len(array)):
        ch = array[i]
      
        if ch.isupper():
             
            array[i] = ch.lower()
            #print(f'changed {i} from {array[i]} to {ch.lower()}')
                
        elif ch.islower():
            array[i] = ch.upper() 
        else:
            pass
    return "".join(array)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)