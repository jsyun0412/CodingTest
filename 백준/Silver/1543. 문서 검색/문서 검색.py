document = input()  # 문서를 입력 받습니다.
word = input()  # 찾고자 하는 단어를 입력 받습니다.

count = 0  # 최대 횟수를 저장할 변수를 초기화합니다.
index = 0  # 문서 내에서 현재 위치를 나타내는 변수를 초기화합니다.

while index <= len(document) - len(word):  # 현재 위치가 문서의 범위 내에 있는 동안 반복합니다.
    if document[index:index + len(word)] == word:  # 현재 위치부터 찾고자 하는 단어의 길이만큼을 비교하여 일치하는지 확인합니다.
        count += 1  # 일치하면 카운트를 증가시킵니다.
        index += len(word)  # 다음 비교를 위해 현재 위치를 찾고자 하는 단어의 길이만큼 이동시킵니다.
    else:
        index += 1  # 일치하지 않으면 다음 위치로 이동합니다.

print(count)  # 최대 횟수를 출력합니다.
