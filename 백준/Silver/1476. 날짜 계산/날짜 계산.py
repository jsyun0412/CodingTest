E, S, M = map(int, input().split())  # 연도, 월, 일을 입력

year = 1 # 시작 연도를 1로 설정 
while True:

    if ((year-E) % 15 == 0 and (year-S) % 28 == 0 and (year-M) % 19 == 0):
        break
    year += 1

print(year)
