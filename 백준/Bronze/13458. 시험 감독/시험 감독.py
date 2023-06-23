n=int(input()) # 시험장 개수 
a=list(map(int,input().split())) # 각 시험장에 있는 응시자의 수 
b,c=map(int,input().split()) # 총감독관, 부감독관이 한번에 관리할 수 있는 응시생의 수 

cnt=0 # 필요한 감독관의 수 

for i in range(n):
    if a[i] >= b:
        a[i] -= b
        cnt+=1
        if a[i] == 0:
            continue
        else:
            if a[i] >= c:
                num = a[i] // c 
                temp = a[i] % c 
                cnt += num 
                if temp > 0:
                    cnt += 1
            else:
                cnt+=1
    else: # 해당 시험장에는 총 감독관만 있으면 되는 경우 
        cnt += 1
        
print(cnt)


