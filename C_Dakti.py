n = int(input())  #number of test cases
 
def get_num_word_pair(word: str):
    clean_word = ''
    num = ''
    for ch in word:
 
        if ch.isnumeric():
            num +=ch
        else:
            clean_word += ch
    
    
    return (int(num), clean_word)
 
 
 
for i in range(n):
   #for each test case
   li = []
   words = input().split()
   for word in words:
      li.append('')
   for word in words:
       num, clean_word = get_num_word_pair(word)
       li[num-1] =  clean_word
      # print(f'setting {num-1} to {clean_word}')
 
   print(" ".join(li))