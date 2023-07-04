a = []

def solve(a):
    a.sort()
    answer = []
    
    # 9명의 키 중, 7명의 합이 100인 경우 탐색 
    for i in range(9):
        for j in range(i+1, 9):
            # 두 난쟁이의 키를 뺀 나머지 키의 합이 100이 되는지 확인 
            total = sum(a) - (a[i] + a[j])

            if total == 100:
                for idx, x in enumerate(a):
                    if idx != i and idx != j:
                        answer.append(x)
                answer.sort()
                for height in answer:
                    print(height)
                return
    
    # 일곱 난쟁이를 찾을 수 없는 경우
    print("일곱 난쟁이를 찾을 수 없습니다.")

# 아홉 명의 키 입력 받기
for _ in range(9):
    height = int(input())
    a.append(height)

# 문제 해결 함수 호출
solve(a)
