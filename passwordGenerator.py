import random # random, randint, choice

Lalpha = "abcdefghijklmnopqrstuvwxyz"
Ualpha = Lalpha.upper()
length = 16

nums = []
lower = []
upper = []

for num in range(0, 10):
    nums.append(str(num))
for char in Lalpha:
    lower.append(char)
for char in Ualpha:
    upper.append(char)

Pass = ""
already = []
c = 0

while c < length:
    x = random.randint(1, 3) # 1, 2, 3
    if x not in already:
        if x == 1:
            already.append(1)
            j = random.choice(nums)
            Pass += j
        elif x == 2:
            already.append(2)
            j = random.choice(lower)
            Pass += j
        elif x == 3:
            already.append(3)
            j = random.choice(upper)
            Pass += j
    else:
        already = []
        c -= 1
    c += 1


print(Pass)
