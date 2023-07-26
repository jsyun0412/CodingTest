def solution(money):
    answer = []
    a = money // 5500
    b = money - a * 5500
    answer.append(a)
    answer.append(b)
    return answer