# 1290 대금 만들기
# n = int(input())
# cnt=0
# for i in range(n-1,0,-1):
#     if n%i==0:
#         cnt+=1
# print(cnt)

# 1291 바이러스 백신
# a,b,c=map(int,input().split())
# for i in range(a,0,-1):
#     if a%i==0 and b%i==0 and c%i==0:
#         print(i)
#         break

# 1292 범인을 잡아라 1
# a = int(input())
# n,sum=10,0
#
# for i in range(10):
#     sum +=a%10
#     a //= 10
#
# if sum%7==4: print("suspect")
# else: print("citizen")

# 1293 1등과 꼴등
# n=int(input())
# a = list(map(int,input().split()))
#
# max = a[0]
# min = a[0]
#
# for i in range(1,n):
#     if max < a[i]:
#         max = a[i]
#     if min>a[i]:
#         min = a[i]
#
# print(max, min)

# 1296 직사각형의 최대 넓이
# n=int(input())
# ln = n/4
# print("%d" % (ln*ln))