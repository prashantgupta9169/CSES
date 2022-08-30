class Solution:
    def __init__(self) -> None:
        self.ans=float('inf')
    def dfs(self,i,arr,l,r):
        if(i==-1):
            self.ans=min(self.ans,abs(l-r))
            return
        self.dfs(i-1,arr,l+arr[i],r)
        self.dfs(i-1,arr,l,r+arr[i])
if __name__=="__main__":
    n=int(input())
    l=list(map(int,input().split()))
    s=Solution()
    s.dfs(n-1,l,0,0)
    print(s.ans)
