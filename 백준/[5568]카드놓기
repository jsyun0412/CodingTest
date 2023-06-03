import itertools

n = int(input())  # 카드의 개수
k = int(input())  # 선택할 카드의 개수

cards = []  # 카드 입력 받을 리스트

for _ in range(n):
    cards.append(input())

combinations = itertools.permutations(cards, k)  # 카드로 만들 수 있는 순열 생성
result = set()  # 중복을 제거한 숫자 조합 결과를 담을 집합

for i in combinations:
    result.add(''.join(i))  # 숫자 조합을 결합하여 하나의 문자열로 만든다. ('7','2','1') -> 721

print(len(result))  # 결과 집합의 길이 출력
