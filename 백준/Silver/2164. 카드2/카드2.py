n = int(input())
cnt = n
gap = 1
while cnt > 1:
    if cnt % 2:
        n -= gap
    cnt = (cnt + 1) // 2
    gap *= 2
print(n)