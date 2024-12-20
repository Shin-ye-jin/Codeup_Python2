# 1359 숫자 피라미드 1
# n=int(input())
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# 1360 숫자 피라미드 2
# n=int(input())
#
# for i in range(n,0,-1):
#     for j in range(i):
#         print(i,end=' ')
#     print()

# 1362 숫자 피라미드 3
def r(n):
    if n==1:
        return 1
    else:
        return n+r(n-1)

n=int(input())
re=r(n)

for i in range(1,n+1):
    for j in range(1,i+1):
        print(re,end=' ')
        re-=1
    print()