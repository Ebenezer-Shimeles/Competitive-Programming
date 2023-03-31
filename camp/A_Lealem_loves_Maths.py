s = input()

nums = []

for ch in s:
    if ch.isnumeric():
        nums.append(ch)

nums.sort()

print("+".join(nums))