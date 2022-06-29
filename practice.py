# 숫자 자료형
print(5) # 5
print(-10) # -10
print(3.14) # 3.14
print(1000) # 1000
print(5+3) # 8
print(2*8) # 16
print(3*(3+1)) # 12

# 문자열 자료형
print("풍선")
print("나비")
print("ㅋ"*9)

# boolean 자료형 
print(5 > 10) # false
print(5 < 10) # true
print(True) # True
print(not True) # False
print(not False) # True
print(not (5>10)) # True

# 애완동물을 소개해주세요 !
animal = "강아지"
name = "초코"
age = 4
hobby = "산책"
is_adult = age > 3
# print는 문자열을 출력하기 위한 함수이므로, 문자열이 아닌 자료형은 문자열로 형변환을 해야한다
print("우리집 " + animal + "의 이름은 초코입니다.")
print(name + "는 " +str(age)+"살이며, "+ hobby+ "을 아주 좋아합니다.")
print("초코는 어른일까요? " + str(is_adult))

# BUt 문자를 이어줄때 '+'가 아니라 ',' 를 사용한다면 형변환을 해줄 필요가 없다.
print("우리집 " , animal , "의 이름은 초코입니다.")
print(name , "는 ",age, "살이며, ", hobby, "을 아주 좋아합니다.")
print("초코는 어른일까요? " , is_adult)

# 주석처리
# 한 문장 주석처리
'''
    여러 문장 
    주석이지롱
    ~~
'''
# ctrl + / 선택한 문장들 주석처리

# 중간 Quiz 변수를 이용하여 다음 문장을 출력하시오
'''
    변수명 : station
    변수값 : 사당, 신도림, 인천공항 순서대로 입력
    출력 문장 : xx행 열차가 들어오고 있습니다.
'''

station = "사당" # 이 부분 수정
print(station + "행 열차가 들어오고 있습니다.")

# 연산자
print(1 + 1) # 2
print(3 - 2) # 1
print(3 * 2) # 6
print(6 / 2) # 3 
print(2 ** 3) # 8 지수승
print(5 % 3) # 2 나머지
print(5 // 3) # 1 몫
print(10 > 3) # True 비교연산자
print(4 >= 10) # False
print(3 == 3) # True
print(1 != 3) # True
print(not (1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) and (3 < 5)) # True & ==> and 와 같은 표현

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True | ==> or과 같은 표현

print(5 > 4 > 3) # True
print(5 > 4 > 10) # False

# 간단한 수식
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2 # number = number + 2
number *= 2 # number = number * 2
number /= 2 # number = number / 2
number -= 2 # number = number -2 

# 숫자처리 함수

print(abs(-5)) # 5
print(pow(4, 2)) # 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.88)) # 5

from math import *
from tkinter.font import names
from tkinter.tix import Balloon # math 모듈 안에 있는 것을 모두 쓰겠다.

print(floor(4.66)) # 4 내림
print(ceil(3.14)) # 4 올림
print(sqrt(16)) # 4 제곱근

# 랜덤함수

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값을 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 값 생성 

# 로또 숫자 출력 1~45

# randrange
print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 값 생성

#randint
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# 중간 Quiz)
'''
    당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
    월 4회 스터디를 하는데 3번은 온라인으로하고, 1번은 오프라인으로 하기로 했습니다.
    아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오
    
    조건1 : 랜덤으로 날짜를 뽑아야함
    조건2 : 월별 날짜는 다름을 감안하여 최고 일수인 28 이내로 정함
    조건3 : 매월 1 ~ 3일은 스터디 중비를 해야하므로 제외
    
    (출력문 예시)
    오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''

from random import *

study_date = randint(4,28)
#study_date = randrange(4, 29)
print("오프라인 스터디 모임 날짜는 매월 " + str(study_date) + "일로 선정되었습니다.")

# 문자열
sentence = '나는 소년입니다.'
print(sentence)

sentence2 = '파이썬은 쉬워요'
print(sentence2)

sentence3 = """
    나는 소년이고,
    파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱

jumin = "990503-1234567"
print("성별 : " + jumin[7]) # 1
print("연 : " + jumin[0:2]) # 0 ~ 1까지 
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[0:6]) 
print("생년월일 : " + jumin[:6]) # 0 ~ 5 까지
print("뒤 7자리 : " + jumin[7:14])  
print("뒤 7자리 : " + jumin[7:]) # 7 ~ 끝까지
print("뒤 7자리 (뒤에 부터): " + jumin[-7:])
# 맨 뒤에서 7번째 끝까지 
# 1234567

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 0번째가 대문자인지 확인
print(len(python))
print(python.replace("Python", "Java")) # Python을 찾아 Java로 바꿔준다.

index = python.index("n")
print(index) 
# "n" 몇번째에 있는지 알려준다.

index = python.index("n", index + 1)
print(index)
# "시작 위치를 지정해주고 "n" 이 몇번째에 있는지 위치를 알려준다

print(python.find("n")) # index와 같이 위치를 반환해준다.
# find와 index의 차이
# print(python.index("Java")) # 오류 발생 -> 프로그램 종료
print(python.find("Java")) # -1 출력

print(python.count("n")) # 2

# 문자열 포맷

#방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % "A")
print("나는 %s 색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {} 색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {0} 색과 {1}색을 좋아해요.".format("파란","빨간")) # 파란, 빨간
print("나는 {1} 색과 {0}색을 좋아해요.".format("파란","빨간")) # 빨간, 파란

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요" .format( color = "빨간", age = 20))

# 방법 4 (v3.6 이상 ~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출 문자
print("백문이 불여일견 \n 백견이 불여일타") # 문장 내 줄바꿈
print("저는 \"나도코딩\"입니다.") # \" \' : 문장 내에서 따옴표로 사용

# \\ : 문장 내에서 \ 
print(" C:\\Users\\dlwld\\Documents\\GitHub\\Python_Study")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple

# \t : 탭
print("Red\tApple") # Red   Apple

# 중간 Quiz
'''
    사이트 별로 비밀번호를 만들어주는 프로그램을 작성하시오
    
    예) http://naver.com
    규칙1 : http:// 부분은 제외 => naver.com
    규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
    규칙3 : 남은 글자 중 처음 세자리 + 글자 개수 + 글자 내 'e' 개수 + "!" 로 구성
                            (nav)       (5)         (1)                 (!)
                        
    예) 생성된 비밀번호 : nav51!
'''

domain = "http://naver.com" 
domain_slice = domain[7:]
index = domain_slice.index(".")
redomain = domain_slice[:index] # naver
three_domain = redomain[:3] 
number_domain = len(redomain)
e_domain = redomain.count("e")
result = three_domain + str(number_domain) + str(e_domain) + "!"
print(f"생성된 비밀번호 : {result}")


# 나도코딩님 풀이
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))

# 리스트

subway = [10, 20, 30]
subway_person = ["유재석","박명수","조세호"]

# 조세호씨가 몇 번째 칸에 타고 있는가 ?
print(subway_person.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
print(subway_person.append("하하"))

# 정형돈씨를 유재석과 조세호 사이에 태우자
subway_person.insert(1, "정형돈") # 정형돈을 1번지에 태우는 것

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway_person.pop()) # 남아있는 사람은 유재석 박명수 조세호

# 같은 이름의 사람이 몇 명 있는지 확인
subway_person.append("유재석")
print(subway_person)
print(subway_person.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list) # 아무것도 출력되지 않음

# 리스트는 자료향에 구애받지 않고 쓸 수 있다.
# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
#print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# dictionary 
# key : value 
cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호
# print(cabinet[5]) # 오류 발생 -> 프로그램 종료

print(cabinet.get(3)) # 유재석
print(cabinet.get(5)) # None을 출력

print(cabinet.get(5, "사용 가능")) # None 대신 사용 가능이 출력된다

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"]) # key가 문자열이여도 가능하다
print(cabinet["B-100"])

# 새 손님
cabinet["C-20"] = "조세호" 
# 1. C-20이 없을 시 새로운 key와 value가 만들어지고
# 2. 있을 시 C-20의 value값이 업데이트가 된다.

# 간 손님
del cabinet["A-3"] # 값 삭제
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key : value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear() # 모든 값을 다 지운다 {} 출력

# 튜플 
# -> 리스트와 다르게 내용 변경, 추가를 할 수 없다
# -> 다만, 속도는 리스트보다 빠르다.
# -> 잘 변경되지 않는 목록을 사용할 때 튜플을 사용

menu = ("돈까스", "치즈까스")
print(menu[0])

# name = "김종국"
# age = "20"
# hobby = "코딩"
# print(name,age,hobby) 
# 이걸 튜플로 바꾸면?

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 세트 (set)
# -> 집합을 말함
# -> 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세호"}
python = set(["유재석", "박명수"]) # 리스트를 집합으로 

# 교집합 (java와 python을 모두 할 수 있는 사람)
print(java & python) # 유재석 출력
print(java.intersection(python))

# 합집합 (Java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # 김태호, 박명수, 유재석, 양세호 출력

# 차집합 (java는 할 수 있지만, python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹음
java.remove("김태호")
print("김태호")

# 자료구조의 변경
# 카페
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # <class 'set'>

menu = list(menu)
print(menu, type(menu)) # <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # <class 'set'>

# 퀴즈
'''
    당신의 학교에서는 파아썬 코딩 대회를 주최합니다.
    참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
    댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
    추첨 프로그램을 작성하시오
    
    조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 가정
    조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
    조건3 : random모듈의 shuffle과 sample을 활용
    shuffle -> 무작위로 리스트 내용의 순서를 바꿈
    sample -> sample(리스트 변수명, 숫자) 리스트에서 숫자만큼 랜덤으로 뽑겠다
    
    (출력 예제)
    -- 당첨자 발표 --
    치킨 당첨자 : 1
    커피 당첨자: [2, 3, 4]
    -- 축하합니다. --
    
    (활용 예제)
'''
from random import *
# lists= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(lists) # 순서 섞음
# chs = set(sample(lists, 1)) # 치킨 선발
# ch = set(sample(lists, 1)) # 치킨 선발
# lists = set(lists) -ch 
# lists = list(lists)

# coffce = sample(lists, 3) # 커피 선발

# print("""
#         -- 당첨자 발표 --
#         치킨 당첨자 : {0}
#         커피 당첨자 : {1}
#         -- 축하합니다.
#       """ .format(ch, coffce))

# 나도 코딩님 풀이

users = range(1, 21) # 1부터 20까지 숫자를 생성
print(type(users)) # <class 'range'>
users = list(users)

shuffle(users) # 순서 섞음

winners = sample(users, 4) # 3명은 커피 1명은 치킨

print("""
        -- 당첨자 발표 --
        치킨 당첨자 : {0}
        커피 당첨자 : {1}
        -- 축하합니다.
      """ .format(winners[0], winners[1:]))


# if 
#weather = "비"
weather = input("오늘 날씨는 어때요?")
# if 조건 : 
#   실행 명령문

if weather == "비" or weather == "눈": # 두개 중 하나 성립
        print("우산을 챙기세요")
elif weather == "미세먼지" :
        print("마스크를 챙기세요")
else :
        print("준비물 필요 없어요.")

temp = int(input("기옥은 어때요?"))
if 30 <= temp :
    print("너무 더워요 나가지 마세요")
elif 10 <= temp and temp < 30 : # 모두 성립
    print("괜찮은 날씨")
elif 0 <= temp < 10 :
    print("외투를 챙기세요")
else :
    print("너무 추워요 나가지 마세요")
    
    
# for
# print("대기번호 1")
# print("대기번호 2")
# print("대기번호 3")
# print("대기번호 4")

# 간단하게 줄일 수 있음
for waiting_no in [0, 1, 2, 3, 4] :
    print("대기번호 : {0}" .format(waiting_no))
    
for waiting_no in range(5) : # 0 1 2 3 4 까지
    print("대기번호 : {0}" .format(waiting_no))
    
for waiting_no in range(1, 6) : # 1 2 3 4 5 까지
    print("대기번호 : {0}" .format(waiting_no))
    
starbucks = ["아이언맨","토르","아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다." .format(customer))
    
# while
# 1. 5번 호출 시 응답이 없으면 폐기처분 
customer = "토르"
index = 5
while index >= 1 :
    print("{0}, 커피가 준비되었습니다. {1} 번 남았습니다." .format(customer, index))
    index -= 1
    if index == 0 :
        print("커피는 폐기되었습니다.")
        
# 2. 응답할 때 까지 계속 호출
customer = "아이언맨"
index = 1
# 무한반복 되므로 잠시 주석처리
# while True :
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회" .format(customer, index)) 
#     index += 1

# 3. 이름을 입력받아 주문한 고객이 맞을때까지 반복문을 돌린다.
customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비되었습니다." .format(customer))
    person = input("이름이 어떻게 되세요?")
    
# continue와 break
absent = [2, 5] # 결석한 학생
no_book = [7] # 책을 깜빡함
for student in range(1, 11):
    if student in absent:
        continue # 아래 있는 문장을 실행하지 않고 다음 조건문으로 가는거임
    elif student in no_book:
        print("오늘 수업은 여기까지, {0}는 교무실로 따라와" .format(no_book))
        break
    print("{0}야, 책 좀 읽어줘" .format(student))
    
# 출석번호가 1 2 3 4가 있는데 앞에 100을 붙이기로 함 -> 101 102 103 104
student = [1,2,3,4,5]
print(student)
student = [i + 100 for i in student]
# 조건문 먼저
# student에 있는 값 하나씩 100을 더해서 리스트로 저장하라는 의미

# 학생들이름을 길이로 바꿔보자
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper for i in students]
print(students)

# 중간 Quiz
'''
    당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
    50명의 승객과 매칠 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오
    
    조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
    조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
    
    (출력문 예제)
    [0] 1번째 손님 (소요시간 : 15분)
    [ ] 2번째 손님 (소요시간 : 50분)
    [0] 3번째 손님 (소요시간 : 5분)
    ...
    [ ] 50번째 손님 (소요시간 : 16분)

    총 탑승 승객 : 2 분
'''

customer = 1
success = [0]
customer_len = 0
while customer <= 50 :
    time = int(random() * 50 + 1) 
    if 5 <= time <= 15 : 
        print("{0} {1}번째 손님 (소요시간 : {2}분)" .format(success, customer, time))
        customer_len += 1
    else :
        print("{0} {1}번째 손님 (소요시간 : {2}분)" .format("[ ]", customer, time))
    customer += 1
print("총 탑승 승객 : {0} 분" .format(customer_len))

# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account() # 함수 호출

# 전달값과 반환값
def deposit(balance, money): # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다." .format(balance+money))
    return balance + money

def withdraw(balance, money): # 출금
    if balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance - money))
        return balance - money
    else :
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다." .format(balance))
        return balance
    
def withdraw_night(balance, money) : # 저녁에 출금
    commission = 100 # 수수료
    return commission , balance - money - commission

balance = 0 # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000) # 출금되지 않음
comission, balance = withdraw_night(balance, 500)
print("수수료 {0}원 이며, 잔액은 {1} 원입니다." .format(comission, balance))
 
# def profile(name, age, main_lang) :
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}" \
#         .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업일 경우
# 기본값을 사용 
def profile(name, age = 17, main_lang = "파이썬") :
    print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")

# 키워드 값을 이용한 함수 호출
def profile(name, age, main_lang) :
    print("이름 : {0}\t나이 : {1}\t 주 사용 언어 : {2}" \
        .format(name, age, main_lang))
    
profile(name = "유재석", main_lang = "파이썬", age = 20)

# 가변인자
# def profile(name, age, lan1, lan2, lan3, lan4, lan5):
#     print("이름 : {0}\t 나이 : {1}\t" .format(name, age), end = " ")
#     print(lan1, lan2, lan3, lan4, lan5)
    # end = " " 를 통해 두 개의 프린트 문장이 한 문장으로 출력된다.
    # 줄바꿈을 하지 않기 위해 쓰는 것.
# profile("유재석", 20, "python", "java", "c", "c++", "c#")
# profile("김태호", 25, "kotlin", "Swift", "", "", "")
''' 유재석 학생이 할 줄 언어가 늘었다면 ? 함수의 매개인자를 수정해야한다.
 하지만 그렇게 하면 유지보수가 힘들어 가변인자를 사용한다.
 '''
 
def profile(name, age, *language):
    print("이름 : {0}\t 나이 : {1}\t" .format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()
    
profile("유재석", 20, "python", "java", "c", "c++", "c#", "Javascript")
profile("김태호", 25, "kotlin", "Swift")

# 지역변수와 전역변수

gun = 10

# def checkpoint(soldiers) : #경계근무
#     gun = gun - soldiers 
'''
    gun에서 오류 발생
    함수 내에 있는 gun은 밖에 있는 gun이 아닌 함수 내에서 사용하는
    변수 이므로 할당이 되지 않았기 때문에 오류가 발생
'''
#     print("[함수 내] 남은 총 : {0}" .format(gun))
    
    
def checkpoint(soldiers) : #경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))
    
print("전체 총 : {0}" .format(gun))
checkpoint(2)
print("남은 총 : {0}" .format(gun))

'''
    전역변수를 많이 사용하면 코드 관리가 어려워 
    권장되지 않는다.
    전달값과 반환값을 통해 작성하는 것이 좋다
'''

def checkpoint_ret(gun, soldiers) : #경계근무
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun
    
print("전체 총 : {0}" .format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}" .format(gun))

# 중간 Quiz
'''
    표준 체중을 구하는 프로그램을 작성하시오
    
    * 표준 체중 : 각 개인의 키에 적당한 체중
    
    (성별에 따른 공식)
    남자 : 키(m) x 키(m) x 22
    여자 : 키(m) x 키(m) x 21
    
    조건1 : 표준 체중은 별도의 함수 내에서 작성
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)
    조건2 : 표준 체중은 소수점 둘째자리까지 표시
    
    (출력 예제)
    키 175cm 남자의 표준 체중은 67.38kg입니다.
'''

def std_weight(height, gender):
    if gender == "여자" :
        return height * height * 21 
    else :
        return height * height * 22

height = 175
gender = "남자"
weight = round(std_weight(height / 100 , gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height, gender ,weight))

# 표준입출력
print("python", "java", sep = ",")
print("python", "java", sep = " vs ")
print("python", "java", sep = ",", end = "?")
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file = sys.stdout) # 표준 출력
print("Python", "Java", file = sys.stderr) # 표준 에러

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":")
    
# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21) :
    print("대기번호 : " + str(num).zfill(3))
    # 3자리를 확보하는데 값이 안들어가는 자리는 0으로 채우는 것
     
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은" + answer + "입니다.")

# 다양한 출력포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 차지
print("{0: >10}" .format(500)) # -500이라고 적으면 -500이라고 나오지만 500이라고 하면 그냥 500으로 나온다.
# 출력 값 :          500  
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}" .format(500)) # +500

# 왼쪽 정렬하고, 빈칸으로 _채움
print("{0:_<+10}" .format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(1000000000))
# 3자리마다 콤마를 찍어주기, +-부호도 붙이기
print("{0:+,}".format(1000000000))
# 3자리마다 콤마를 찍어주되 부호도 붙이고 자리수도 확보
# 돈이 많으면 행복하니 빈 자리는 ^ 채우기
print("{0:^<+30,}".format(10000000000))
# 소수점 출력
print("{0:f}" .format(5/3)) #1.666667
# 소수점 특정 자리수 까지만 표시
print("{0:.2f}".format(5/3))

# 파일입출력
score_file = open("score.txt","w",encoding="utf8")
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") #파일 불러와서 내용 덧붙이기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # 파일의 모든 내용을 불러옴
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(), end = "") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
score_file.close() 

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() # list형태로 저장
for line in lines:
    print(line, end = "")
score_file.close()

# pickle -> 프로그램 상에서 사용하고 있는 데이터를 파일로 저장하는 것
import pickle
# pickle을 쓰기 위해 바이너리로 써야한다. 인코딩은 따로 설정할 필요없다
profile_file = open("profile.pickle","wb")
profile = {"이름" : "박명수", "나이" : 20, "취미" : ["축구","골프 ","코딩"]}
print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()

# with
import pickle
# close를 해줄 필요가 없음
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
    
with open("study.txt", "w", encoding= "utf8") as study_file:
    study_file.write("파이썬을 공부하고있어요")
    
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
    
# 중간 Quiz
'''
    당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있다
    보고서는 항상 아래와 같은 형태로 출력되어야 한다.
    
    -X 주차 주간보고-
    부서 :
    이름 :
    업무 요약 :
    
    1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성
    
    조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만든다
'''

for i in range(1, 51):
    document_file = open(f"{i}주차.txt", "w", encoding= "utf8")
    print(f" - {i}주차 주간보고 - \n부서 : \n이름 : \n업무 요약 : " , file = document_file)
    document_file.close()
    
# class
# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다." .format(name))
print("체력 {0}, 공격력 {1}\n" .format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포를 쓸 수 있는데 일반모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다." .format(tank_name))
print("체력 {0}, 공격력 {1}\n" .format(tank_hp, tank_damage))

def attack(name, location, damage) :
    print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}]" \
        .format(name, location, damage))
    
attack(name , "1시", damage)
attack(tank_name , "1시", tank_damage)
# 만약 유닛이 더 늘어난다면 또 유닛을 생성해야함.
# 쉽게 생성될 수 있게 클래스를 사용함.
# 클래스는 붕어빵 틀이라고 생각 
# 틀은 하나인데 무한개 만들 수 있다.

# 위에 한 것을 클래스 부분으로 만들어보자
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다." .format(self.name))
        print("체력 {0}, 공격력 {1}\n" .format(self.hp, self.damage))
        
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__ -> 파이썬에서 쓰이는 생성자
# 객체가 만들어질때 호출되는 함수

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}" .format(wraith1.name, wraith1.damage))
# 이렇게 멤버변수를 통해 클래스 안에 있는 변수에 접근할 수 있다.

# 마인트 컨트롤 : 상대방 유닛이 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True # 기능 업그레이드라 가정
# 외부에서 변수를 추가로 할당한 것
# wraith1에는 clocking이 없다!!!!!!!
if wraith2.clocking == True :
    print("{0} 는 현재 클로킹 상태입니다." .format(wraith2.name))


# 메소드

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격한다 [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))
            

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50 , 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 상속
# 위 클래스 예제를 다시 들어 상속을 해보자

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed  = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))
        
class AttackUnit(Unit): # 상속
    def __init__(self, name, hp, damage, speed):
        # self.name = name # 위 클래스와 겹침
        # self.hp = hp # 위 클래스와 겹침
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격한다 [공격력 {2}]"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다." .format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다." .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다." .format(self.name))    
            
# 드랍쉽 : 공중 유닛, 수송기, 마린/ 파이어뱃/ 탱크 등을 수송, 공격 기능 x
class Flyable :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location) :
        print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]" \
            .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
# 다중 상속
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        # 지상 스피드는 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)
        
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 메소드 오버라이딩
# 벌쳐 : 지상 유닛, 기동성이 좋음
valture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
valture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move(battlecruiser.name, "9시")

# pass
# 건물
