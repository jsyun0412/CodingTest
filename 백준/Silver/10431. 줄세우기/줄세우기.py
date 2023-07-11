P = int(input())  # 첫 줄에서 테스트 케이스의 수 P를 입력 받습니다.

for _ in range(P):
    T, *heights = map(int, input().split())  # 각 테스트 케이스에서 번호 T와 키 값들을 입력 받습니다.

    steps = 0  # 뒤로 물러선 걸음 수
    for i in range(1, len(heights)):
        for j in range(i):
            if heights[j] > heights[i]:
                steps += 1

    print(f"{T} {steps}")

