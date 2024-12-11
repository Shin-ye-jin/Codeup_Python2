#1287 구구단을 *로 출력하기
# n=int(input())
#
# for i in range(1,10):
#     print("*"*n*i)

# 1288 nCr (Tiny)
# def f(n):
#     if n<=1:
#         return 1
#     else:
#         return n*f(n-1)
#
# n,r=map(int,input().split())
# result = f(n)/(f(n-r)*f(r))
# print("%d" % result)

# 1289 가장 큰 운동장
re,max=0,0
for i in range(3):
    h,w=map(int,input().split())
    re=h*w
    if max < re:
        max = re
print(max)