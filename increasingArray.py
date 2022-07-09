n=int(input())
l=list(map(int,input().split()))
ans=0
ma=l[0]
for i in range(n-1):
    ma=max(l[i],ma)
    if(l[i+1]<ma):
        ans+=ma-l[i+1]
print(ans)