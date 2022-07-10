for _ in range(int(input())):
    a,b=map(int,input().split())
    x = 2 * b - a; y = 2 * a - b
    if x < 0 or y < 0:
        print("NO")
        continue
    ans=not (x % 3) and not (y % 3)
    if(ans):
        print("YES")
    else:
        print("NO")