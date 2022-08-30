def dfs(i,j,n,ans,path):
    print("i and j",i,j)
    if(i<0 or j<0 or i>=n or j>=n):
        return
    if(i==0 and j==0):
        ans.append(path[::-1])
        return
    dfs(i-1,j,n,ans,path+"U")
    dfs(i,j-1,n,ans,path+"L")
    dfs(i,j+1,n,ans,path+"R")
    dfs(i+1,j,n,ans,path+"D")
    return ans
ans=dfs(1,1,2,[],"")
print(ans)