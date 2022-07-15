s=input()
ans=[]
def permutations(nums, asf):
    if len(nums) == 0:
        ans.append(asf)

    for i in range(len(nums)):
        ele = [nums[i]]
        remaining_arr = nums[:i] + nums[i+1:]
        permutations(remaining_arr, asf + ele)
s=list(s)
permutations(s,[])
s=set()
for i in range(len(ans)):
    x="".join(ans[i])
    s.add(x)
s=list(s)
s.sort()
print(len(s))
for x in s:
    print(x)