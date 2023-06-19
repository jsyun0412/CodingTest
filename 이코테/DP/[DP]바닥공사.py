n = int(input())

d = [0] * 1001

d[1] = 1 # n = 1 일때 경우의수는 1
d[2] = 3 # n = 2 일때 경우의수는 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] *2) % 796796

print(d[n])