n = int(input())

def least_common(p1:str, p2: str):
   #print(f'compaing {p1} and {p2}')
   return_value = ''

   for i in range(len(p1)):
      
      if p1[i] == '?' and p2[i] == '?':
        return_value += '?'
      elif p1[i] == 'U':
        return_value += p2[i]
      elif p1[i] == 'A':
        return_value += p1[i]
      

      elif p1[i] == '?' and p2[i] != '?':
        return_value += p2[i]
      elif p1[i] != '?' and p2[i] == '?':
        return_value += p1[i]
    
      elif p1[i] != p2[i]:
        return_value += 'A'
      elif p1[i] == p2[i]:
        return_value += p2[i]
   return return_value


patterns = []
for i in range(n):
    patterns.append(input())

l = len(patterns[0])
fp = ''
for i in range(l):
    fp += 'U'

if len(patterns) == 1:
    print(least_common(fp, patterns[0]).replace('?', 'c').replace('A', '?'))
else:
   

    for i in range(n):
        fp = least_common(fp, patterns[i])
    
    print(fp.replace('?', 'b').replace('A', '?'))