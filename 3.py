def solve(n):
    
    lcd=[0,1,2,5,6,8,9]
    count=0
    for i in range(1,99999):
        s=str(i)
        for j in s:
            if int(j) not in lcd:
                break
        else:
            count+=1
            if count==n:
                return i
a=int(input())
print(solve(a))
