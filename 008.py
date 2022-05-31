N = int(input())
S = input()

li = [0]* 8
li[0] = 1

MOD = 10 ** 9 + 7
for i in S:
    if i =='a':
        li[1] += li[0]
        li[1] %= MOD
    elif i == 't':
        li[2] += li[1]
        li[2] %= MOD
    elif i == 'c':
        li[3] += li[2]
        li[3] %= MOD
    elif i == 'o':
        li[4] += li[3]
        li[4] %= MOD
    elif i == 'd':
        li[5] += li[4]
        li[5] %= MOD
    elif i == 'e':
        li[6] += li[5]
        li[6] %= MOD
    elif i == 'r':
        li[7] += li[6]
        li[7] %= MOD
        
print(li[-1])