# 변수 variable
# - 값(literal)을 저장하는 메모리 상의 공간
# - 각 변수마다 이름이 지정되어 있음 (이름을 불러서 사용)

# 변수 선언 방법
# 변수명 = 값
a = 10  # a라는 메모리 상의 공간에 10(literal)을 대입
b = '권세진'

print("a = ", a)
print("b = ", b)

# 대입 연산자 (=)
# - 우항의 값을 좌항의 변수에 대입

num = 100
print("num = ", num)

num = 999
print("num = ", num)

num = "abcdefg"
print("num = ", num)

team_name = "오지라퍼스"
print(team_name)    # 오지라퍼스

# 변수 명명 규칙
# 1. 의미 있는 이름 사용

# 2. 변수명은 snake case를 사용(소문자 + _)
# 단, 대문자도 사용은 가능하고, 소문자와 구분된다
team_name = "오지라퍼스"
Team_name = "Ohgiraffers"
print(team_name)    # 오지라퍼스
print(Team_name)    # Ohgiraffers

# 변수명은 한글도 가능하나 지양함 지양지양
밥조 = "1조"
print(밥조)


# 변수명은 숫자로 시작해서는 안된다
name_1 = "콩쥐"
#1_name = "팥쥐"   # 문법 에러
_1_name = "팥쥐"

# 특수 문자는 언더스코어(_)를 제외하고 사용 불가
#name-2 = "안녕"

# 예약어는 변수명으로 사용 불가
# if, for, else, while, elif


# 파이썬 예약어 종류 확인
import keyword
print(keyword.kwlist)


# 특정 값을 무시
x, _, z = (1,2,3)
print(x)    # 1
print(z)    # 3

# 앞에 *을 추가로 붙여 여러 개의 값 무시
x, *_, y = (1, 2, 3, 4, 5)
print(x)    # 1
print(y)    # 5

