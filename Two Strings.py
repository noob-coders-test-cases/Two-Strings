a = int(input())
for i in range(a):
    s1=input()
    s2=input()
    setx=set([a for a in s1])
    sety=set([b for b in s2])
    if setx.intersection(sety)==set():
        print("NO")
    else:
        print("YES")
