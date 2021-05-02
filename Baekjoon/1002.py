n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    rsum = r1 + r2
    rsub = abs(r1 - r2)
    if d == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d == rsum or d == rsub:
            print(1)
        elif d < rsum and d > rsub:
            print(2)
        else:
            print(0)
