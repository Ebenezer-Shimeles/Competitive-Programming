# Enter your code here. Read input from STDIN. Print output to STDOUT

N_ENGLISH = int(input())

english = set(input().split())

N_French = int(input())

french = set(input().split())

print(len(english | french))