n=input()
ans=1
ma=1
prev=n[0]
for i in range(1,len(n)):
    if(n[i]==prev):
        ans+=1
    else:
        prev=n[i]
        ans=1
    ma=max(ma,ans)
print(ma)