# 1124 분자량 구하기 1
# n=input()
# matrix=list(n)
# n1 = matrix[1]
# n2 = matrix[3]
# print(int(n1)*12+int(n2)*1)

# import re
# str = input()
# numbers = re.findall('\\d+',str) # 문자에서 숫자 분리
# n1 = numbers[0]
# n2 = numbers[1]
# print(int(n1)*12+int(n2)*1)

# 1126 정수 계산기
# a,b=map(int,input().split())
# print("%d + %d = %d" % (a,b,a+b))
# print("%d - %d = %d" % (a,b,a-b))
# print("%d * %d = %d" % (a,b,a*b))
# print("%d / %d = %d" % (a,b,a//b))
# print(a,"%",b,"=",a%b)

# 1127 성적 계산
# sum=0.0
# for i in range(3):
#     a,b=map(float,input().split())
#     sum = sum+a*b
# print(round(sum,1))

# 1128 n*123456789
n=int(input())
print(n*123456789)