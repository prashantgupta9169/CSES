n=int(input())
l=list(map(int,input().split()))
s=sum(l)
finalSum=(n*(n+1))//2
print(finalSum-s)