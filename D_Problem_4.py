s = input()


final_word = ''
prev = 'H'
l_count = 0


# for i in range(len(s)):
    
    
#     if s[i] != prev:
#         final_word += s[i]
#         l_count = 0
#     elif s[i] == 'l':
#         if l_count < 1:
#             final_word += s[i]
#             l_count +=1
       
#     prev = s[i]
# i = 0
# ls = 0
# lock = False
# while i < len(s):
#     c_char  = s[i]
#     if c_char == 'l':
#         final_word += 'l'
#     while   i<len(s) and c_char == s[i] and c_char:
#         i += 1
#         ls += 1
    
#     if (c_char == 'l' and ls > 0) or c_char != 'l':
#         final_word += c_char
#         ls = 0

# if 'hello' in final_word :
#     print('YES')
# else:
#     print('NO')

i = 0
j = 0
c = 0
ss = 'hello'
while i < len(s):
  
    if  s[i]== ss[j] : 
        c += 1
        j += 1
    i += 1
    if j == 5:
        break

if c == 5:
    print('YES')
else:
    print('NO')