import sys

n = int(input())
arr = [0 for j in range(1000001)]
arr[0] = 1
arr[1] = 1
arr[2] = 2
for i in range(3, 1000001):
    arr[i] = arr[i - 1] % 1000000009 + arr[i - 2] % 1000000009 + arr[i - 3] % 1000000009
for i in range(n):
    a = int(input())
    # 이렇게 중복하여 나누는 이유는, 연산 과정에서 결과 값이 매우 커지는 것을 방지하기 위함. 
    # 합의 결과가 매우 커질 수 있으며, 연산 과정에서 오버플로우를 방지하기 위해 연산할 때마다 1000000009로 나누어 나머지 값을 적용
    print(arr[a] % 1000000009) 
