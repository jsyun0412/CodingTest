n = int(input())

array=list(map(int,input().split()))

#DP테이블 초기화 
d = [0] * 100

#DP 진행 (반복문)
d[0] = array[0]
d[1] = max(array[0],array[1])

for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])