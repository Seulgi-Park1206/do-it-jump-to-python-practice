# abs(x) : x의 절댓값 돌려줌
print(abs(3))   # 3
print(abs(-1.2))    # 1.2

# all(x) : 리스트, 튜플, 문자열, 딕셔너리, 집합 등을 x로 받아 x가 모두 참이면 True, 거짓이 하나라도 있으면 False 돌려줌
print(all([1, 2, 3]))   # True
print(all([1, 2, 3, 0]))    # False -> 요소 0은 거짓

# any(x) : x가 모두 거짓일 때에만 False 돌려줌(all(x)의 반대)
print(any([1, 2, 3, 0]))    #True -> 1, 2, 3이 참
print(any([0, ""]))     # False

# chr(i) : ASCII 코드 값 i에 해당하는 문자 출력
print(chr(97))      # 'a'
print(chr(48))      # '0'

# dir : 객체가 자체적으로 가지고 있는 변수나 함수 보여줌
print(dir([1, 2, 3]))      # 리스트 객체가 가지고 있는 변수나 함수 출력
print(dir({1:'a'}))     # 딕셔너리 객체가 가지고 있는 변수나 함수 출력

# divmod(a, b) : a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려줌
print(divmod(7, 3))     # (2, 1)
print(7 // 3)   # 몫
print(7 % 3)    # 나머지

# enumerate : 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력받아 인덱스 값을 포함하는 enumerate 객체 돌려줌
## 보통 for문과 함께 자주 사용됨 / 반복되는 구간에서 객체의 현재 위치를 알려주는 인덱스 값 필요할 때 유용
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)  # 0 body \n 1 foo \n 2 bar

# eval(실행 가능한 문자열) : 문자열 실행 결과값 돌려줌
## 입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용
print(eval('1+2'))  # 3
print(eval("'hi' + 'a'"))    # hia
print(eval('divmod(4, 3)')) # (1, 1)

# filter(함수명, 함수에 들어갈 반복 가능한 자료형) : 두 번째 인수의 요소가 첫 번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 걸러서 돌려줌
##positive.py
def positive(l):    # 양수 값만 돌려주는 함수
    result = [] # 반환 값이 참인 것만 걸러내서 저장할 변수
    for i in l:
        if i > 0:
            result.append(i)
    return result
print(positive([1, -3, 2, 0, -5, 6]))   # [1, 2, 6]

##filter1 : filter 함수를 사용해 positive.py 간소화한 버전
def positive2(x):
    return x > 0

print(list(filter(positive2, [1, -3, 2, 0, -5, 6]))) # [1, 2, 6]
##positive2 함수 -> lambda 사용
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))  # [1, 2, 6]

# hex(X) : 정수 x를 16진수로 변환
print(hex(234)) # '0xea'
print(hex(3))   # '0x3'

# id(object) : 입력받은 객체의 고유 주소 값(래퍼런스) 돌려줌
## 3, a, b 모두 동일한 객체 가리킴
a = 3
print(id(3))
print(id(a))

b = a
print(id(b))
print(id(4))    # 3, a, b와 다른 고유 주소 값 출력

# input([prompt]) : 사용자 입력 받음
a = input()     # prompt 생략
print(a)
b = input("Enter: ")    # prompt : 'Enter: '
print(b)

# int(x) : 입력값을 정수로 돌려줌
print(int('3')) #3
print(int(3.4)) #3
print(int(5))   #5

# int(x, radix) : radix 진수로 표현된 문자열 x를 10진수로 변환
print(int('11',2))  # 3
print(int('1A', 16))    # 26

# isinstance(object, class) : 첫 번째 인수인 인스턴스가 두 번째 인수인 클래스의 인스턴스인지 판단
## 결과값 : True / False
class Person: pass

a = Person()    # Person 클래스의 인스턴스 a 생성
print(isinstance(a, Person))    # True

b = 3
print(isinstance(b, Person))    # False

# len(s) : 입력값 s의 길이(요소의 전체 개수) 돌려줌
print(len("python"))    # 6
print(len([1, 2, 3]))   # 3
print(len((1, 'a')))    # 2

# list(s) : 입력받은 반복 가능한 자료형 s를 리스트로 만들어 반환
print(list("python"))   # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3)))  # [1, 2, 3]

a = [1, 2, 3]
b = list(a)
print(b)    # [1, 2, 3]

# map(f, iterable) : 입력 받은 반복 가능한(iterable) 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려줌
##two_times.py
def two_times(numberList):  # 리스트 요소 각각에 2를 곱한 값 돌려줌
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)   # [2, 4, 6, 8]

##map.py
def two_times2(x): return x*2

print(list(map(two_times2, [1, 2, 3, 4])))   # [2, 4, 6, 8]

##lambda.py
print(list(map(lambda a: a*2, [1, 2, 3, 4])))   # [2, 4, 6, 8]
