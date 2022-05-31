def nibun(A, q):
    left = 0
    right = N
    while abs(left-right) > 1:
        mid = (left+right)// 2
        if q > A[mid]:
            left = mid
        else:
            right = mid
            
    return min(abs(q-A[left]), abs(q-A[min(N-1, left+1)]), abs(q-A[max(0, left-1)]))
            

N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for i in range(Q):
    q = int(input())
    print(nibun(A, q))