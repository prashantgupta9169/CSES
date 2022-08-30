n=int(input())
arr=[]
for i in range(n):
    p,s=map(int,input().split())
    arr.append((p,s))
arr.sort(key=lambda x:(x[0],-x[1]))
print(arr)