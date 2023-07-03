n=input()
find=input()

count = 0
index = 0

for i in range(len(n)):
    if index>i:
        continue

    if find == n[i: i+len(find)]:
        count+=1
        index = i + len(find)
        
print(count)