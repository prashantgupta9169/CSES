n=int(input())
finalSum=(n*(n+1))//2
if(finalSum%2!=0):
    print("NO")
else:
    print("YES")
    target=finalSum//2
    dp=[1]*(n+1)
    arr=[]
    while(target!=0):
        if(target>=n):
            target-=n
            arr.append(n)
            dp[n]=0
            n-=1
        else:
            arr.append(target)
            dp[target]=0
            target=0
    rem=[]
    for i in range(1,n+1):
        if(dp[i]==1):
            rem.append(i)
    print(len(arr))
    print(*arr)
    print(len(rem))
    print(*rem)