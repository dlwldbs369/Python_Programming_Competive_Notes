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

from math import * # math 모듈 안에 있는 것을 모두 쓰겠다.

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
