N = int(input())  # 전체 사람의 수

people = []  # 각 사람의 몸무게와 키를 저장할 리스트
ranks = []  # 각 사람의 덩치 등수를 저장할 리스트

# 각 사람의 몸무게와 키를 입력받아 리스트에 저장
for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

# 각 사람의 덩치 등수를 계산
for i in range(N):
    rank = 1  # 초기 등수는 1로 설정
    for j in range(N):
        if i == j:  # 같은 사람은 비교하지 않음
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1
    ranks.append(rank)

# 각 사람의 덩치 등수를 출력
for rank in ranks:
    print(rank)
