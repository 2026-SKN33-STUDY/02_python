# number (숫자형)
# - 정수
# - 실수
# - 복소수
#from collections.abc import bytes_iterator

# type (변수명 | 값) 함수: 변수 또는 값의 타입을 확인하는 내장함수

# 정수 int
num = 123
print(num, type(num))

price = 1_000_000_000;  # 정수 자릿수 구분
print(price, type(price))

# 자료형마다 차지할 수 있는 용량
# int 최대값
import sys
print(sys.maxsize, type(sys.maxsize))
#992경 =~ 8 Byte ==~ 2^64 bit
# 1 byte == 8 bit

# 2진법, 8진법, 16진법
a = 0b100   #4
print(a, type(a))

b = 0o23    #19
print(b, type(b))

c = 0xff    #255
print(c, type(c))

#---------------------------------------------------------------
# 실수 float
f1 = 123.456
print(f1, type(f1))

f2 = -99999.999999
print(f2, type(f2))

f3 = 1.5757575757575757575757575757575575757575
print(f3, type(f3))
# 소수점 아래 16자리까지 출력

#---------------------------------------------------------------
# 복소수 complex
c = 2j
print(c, type(c))

d = 3 + 4j
print(d, type(d))

#---------------------------------------------------------------
# 산술연산 (+, -, *, /, //(몫), %(modulo), **(거듭제곱))
print("----산술연산----")
print(1+2)
print(1-2)
print(1*2)
print(1/2)      # 나누어떨어질 때까지의 몫을 구함
print(1//2)     # 정수 영역에서의 몫을 구함
print(1%2)      # 정수 영역에서의 나머지를 구함
print(2**3)     # 2^3
print(2**63)    # int 양의 최댓값

