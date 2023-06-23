# 숫자의 개수
n = int(input())

# 주어진 수열
numbers = list(map(int, input().split()))

# 덧셈, 뺄셈, 곱셈, 나눗셈 연산자의 개수
add, subtract, multiply, divide = map(int, input().split())

# 최댓값과 최솟값 초기화
max_value = float('-inf')
min_value = float('inf')

# 백트래킹 알고리즘을 이용하여 모든 경우의 수 탐색
def backtrack(idx, result, add, subtract, multiply, divide):
    global max_value, min_value

    # 모든 숫자를 사용한 경우 최댓값과 최솟값 갱신
    if idx == n:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return

    # 덧셈 연산자 사용
    if add > 0:
        backtrack(idx + 1, result + numbers[idx], add - 1, subtract, multiply, divide)
    # 뺄셈 연산자 사용
    if subtract > 0:
        backtrack(idx + 1, result - numbers[idx], add, subtract - 1, multiply, divide)
    # 곱셈 연산자 사용
    if multiply > 0:
        backtrack(idx + 1, result * numbers[idx], add, subtract, multiply - 1, divide)
    # 나눗셈 연산자 사용
    if divide > 0:
        # 나눗셈 연산은 음수를 양수로 나눌 때와 같은 효과를 가지지 않으므로 주의해야 합니다.
        if result < 0:
            backtrack(idx + 1, -(-result // numbers[idx]), add, subtract, multiply, divide - 1)
        else:
            backtrack(idx + 1, result // numbers[idx], add, subtract, multiply, divide - 1)

# 백트래킹 알고리즘 호출
backtrack(1, numbers[0], add, subtract, multiply, divide)

# 결과 출력
print(max_value)
print(min_value)
