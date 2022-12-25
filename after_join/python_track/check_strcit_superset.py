# Enter your code here. Read input from STDIN. Print output to STDOUT

def to_int_set(s: str) -> set:
    l = s.split(' '); 
    tmp_set = set();
    for ch in l:
         tmp_set.add(int(ch)) #assuming every char is an int
    return tmp_set

set_a = to_int_set(input())
n = int(input())

s = []
for i in range(n):
    tmp_set = to_int_set(input())
    if not (set_a.issuperset(tmp_set)) :
        print(str(False))
        exit(0)

print(str(True))
#print(f'set_a = {set_a} sets = {s} and n = {n}')

