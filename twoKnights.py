n=int(input())
ans=[0]
for i in range(2,n+1):
    totalCombination=((i**2)*(i**2-1))//2
    noValid=2*2*(i-1)*(i-2)
    finalAns=totalCombination-noValid
    ans.append(finalAns)
for x in ans:
    print(x)
