"""
처음에 deque로 풀었는데, vscode에선 정답이 잘 나오는데 채점을 하면 자꾸 런타임에러가 발생하였다.
왜 런타임 에러가 발생하는지 찾지 못했고, heqpq를 사용해서 풀어보니 해결되었다. 
"""

"""
1. deque 활용 코드
"""
from collections import deque
n,m=map(int,input().split())
a = list(map(int,input().split())) #4 2 3 1
a.sort() #1 2 3 4

q = deque(a) #deque으로 구현

if m>0:
    for i in range(m):
        add = q[i] + q[i+1]
        q[i] = add
        q[i+1] = add
        
print(sum(q))

"""
2.heapq 활용 코드
"""
#heapq를 사용하면 카드를 뽑을 때마다 정렬하지 않고 heappop()을 2번 해주기만 하면 가장 작은 값 2개가 알아서 뽑힌다. 
#두 값을 다시 heapq에 넣어주면 끝이다. O(m)*O(logN)

import sys
import heapq

N, M = map(int, input().split())

cards = list(map(int, input().split()))

heapq.heapify(cards) # heapq.heapify(list) : O(N)

for _ in range(M):
    tmp = heapq.heappop(cards) + heapq.heappop(cards) #heapq.heappop(heap) : O(logN)
    heapq.heappush(cards, tmp) #heapq.heappush(heap, data) : O(logN)
    heapq.heappush(cards, tmp)

print(sum(cards))
