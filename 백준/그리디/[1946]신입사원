'''
문제유형: 그리디
문제 레벨: 실버1
풀이 : 
1. 서류 심사 성적과 면접 시험 성적을 int형으로 변환하여 a배열에 저장한다.
2. a배열을 서류 심사 성적 기준으로 오름차순 정렬한다.
3. 가장 우수한 지원자의 면접시험 성적을 max변수에 저장한다.
4. 다음 지원자의 면접 시험 성적이 max보다 높을 경우 max를 해당 지원자의 면접 성적으로 업데이트하고, 선발자 수 cnt += 1
'''
t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        s, m = map(int, input().split())
        a.append((s, m))
    
    a.sort()
    
    cnt = 1
    max_interview = a[0][1]
    for i in range(1, n):
        if a[i][1] < max_interview:
            max_interview = a[i][1]
            cnt += 1
    
    print(cnt)
