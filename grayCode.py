def dfs(n,arr):
    for i in range(1 << n):
        val = (i ^ (i >> 1))
        s = bin(val)[2::]
        if(len(s)!=n):
            s="0"*(n-len(s))+s
        arr.append(s)
    return arr
n=int(input())
arr=[]
ans=dfs(n,arr)
for x in ans:
    print(x)