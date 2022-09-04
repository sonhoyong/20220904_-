"""

함수
Y = F(X)
F = 함수이름
X = 매개변수

사용자한테 금액을 입력받으면

커피 몇잔을 살수있고
감사하다는 인사를 하는 프로그램을
만들어보자
def 감사인사():
    print("커피는 {}잔 구매하실 수 있습니다".format(몇잔))
    print("감사합니다")
    print("다음에 또 찾아와 주세요")
    print("저는 ~~~프로그램입니다")
for _ in range(3):
   while True:
    금액 = input(">>>입력 :")
    몇잔 = 금액 // 300
    감사인사()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~함수 예제
#1
def welcome():
    print("Hellow Python")
    print("Nice to meet you")

welcome()
#2
def adder(*args):
    print('{}의 합은 {}입니다'.format(args,sum(args)))

adder(1,2)
adder(1,2,3)
adder(1,2,3,4)
def 커피머신(money,pick):
    print('{}원에서 {}를 선택하셨습니다.'.format(money,pick))
    menu = {
        '아메리카노':1000,
        '카페라떼':1500,
        '카푸치노':2000
    }

    if pick not in menu:
        print('{}는 판매하지 않습니다'.format(pick))
        return money,'없는메뉴'
    elif menu[pick]>money:
        print('{}는 {}원입니다.'.format(pick.menu[pick]))
        return money,'금액부족'
    else:
        return money -menu[pick],pick

order = input('커피를 선택하세요(아메리카노,카푸치노,카페라떼) >>>')
pay = int(input("얼마를 내시나요? >>>"))

change,coffe = 커피머신(pay,order)
print('잔돈{}원, 커피{}'.format(change,coffe))

#mutable, immutable
a = [1, 2, 3, 4, 5]

b = a
b[0] = 100

print(a) -> [100,2,4,5]
받은돈 = int(input("넣을 돈을 입력하세요 >>>"))

def vending_machine(money):
    음료수값 = 700
    음료수최대개수 = money // 700

    for i in range(음료수최대개수+1):
        print("음료수 = {}개,잔돈 = {}원".format(i,money-음료수값+i))
vending_machine(3000)
"""
def get_average(marks):
    평균 = sum(marks.values() / len(marks.values()))
    return 평균


marks = ['국어': 90,'영어' : 80 ,'수학' : 85]
average = get_average(marks)
print('평균은 {}점입니다.'.format(average))


