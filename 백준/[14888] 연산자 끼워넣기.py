# 숫자의 개수
n = int(input())

# 주어진 수열
numbers = list(map(int,input().split()))

# 덧셈, 뺄셈, 곱셈, 나눗셈 연산자의 개수
add, subtract, multiply, divide = map(int,input().split())

# 최댓값과 최솟값 초기화 

# 처음에 max_value를 음의 무한대로 초기화하면, 
# 이후 탐색 과정에서 max_value보다 큰 값이 나오면 해당 값으로 max_value를 갱신할 수 있다. 

# 마찬가지로 min_value를 양의 무한대로 초기화하면, 
# 탐색 과정에서 min_value보다 작은 값이 나오면 해당 값으로 min_value를 갱신할 수 있다.

max_value = float('-inf')
min_value = float('inf')

# 백트래킹 알고리즘을 이용하여 모든 경우의 수 탐색
def backtrack(idx, result, add, subtract, multiply, divide): # idx는 현재까지 고려한 숫자들의 개수를 나타냄 
    global max_value, min_value

    # 모든 숫자를 사용한 경우 최댓값과 최솟값 갱신 
    if idx == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return 
    
    # 덧셈 연산자 사용
    if add > 0:
        backtrack(idx + 1, result + numbers[idx], add + 1, subtract, multiply, divide)

    # 뺄셈 연산자 사용
    if add > 0:
        backtrack(idx + 1, result - numbers[idx], add, subtract + 1, multiply, divide)
    
    # 곱셈 연산자 사용
    if add > 0:
        backtrack(idx + 1, result * numbers[idx], add, subtract, multiply + 1, divide)
    
    # 나눗셈 연산자 사용
    if divide > 0:
        # 나눗셈 연산은 음수를 양수로 나눌 때와 같은 효과를 가지지 않으므로 주의해야 한다 !
        if result < 0:  #현재 결과가 음수 일 때 
            backtrack(idx + 1, -(-result // numbers[idx]), add, subtract, multiply, divide - 1)
        else: #양수 일 때
            backtrack(idx + 1, result // numbers[idx], add, subtract, multiply, divide - 1)

# 백트래킹 알고리즘 호출 
# 초기 호출에서 idx가 1인 이유는, 1로 시작하는 이유는 입력된 숫자들을 순서대로 고려하기 위해서이다.

# 이미 numbers[0]에 해당하는 첫 번째 숫자를 이미 고려했으므로,
# 따라서 다음에 고려해야 할 숫자는 numbers[1]이 되고, 
# 그 이후 숫자들을 차례대로 고려하면서 백트래킹 알고리즘을 수행

backtrack(1, numbers[0], add, subtract, multiply, divide)


print(max_value)
print(min_value)
