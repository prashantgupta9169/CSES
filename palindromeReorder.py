n=input()
d=dict()
for x in n:
    d[x]=d.get(x,0)+1
front=""
back=""
odd=0
oddChar=""
for i in d:
    c=d[i]
    if(c%2==0):
        y=c//2
        front+=y*i
        back+=y*i
    else:
        odd+=1
        oddChar+=i
        y=c//2
        front+=y*i
        back+=y*i
if(odd>1):
    print("NO SOLUTION")
else:
    back=back[::-1]
    front+=oddChar+back
    print(front)
