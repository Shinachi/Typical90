N = int(input())
A, B, C = map(int, input().split())

ans = 100000000
for i in range(10000):
    for j in range(10000):
        coin = A* i + B* j
        if N - coin < 0 or (N - coin)% C != 0:
            continue
        k = (N - coin) // C
        ans = min(ans, i+j+k)
        
print(ans)