from django.shortcuts import render
import random
import requests

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def foodmenu(request, name, time):
    time = time
    breakfastmenu = ['프렌치토스트','스크램블에그','후랑크소세지','잉글랜드머핀']
    lunchmenu = ['짜장면','짬뽕','떡볶이','오뎅','비빔냉면','물냉면']
    suppermenu = ['스테이크','삼겹살','설렁탕','순대국밥']
    if time == '아침':
        breakfastpick = random.choice(breakfastmenu)
        context = {
            'name' : name,
            'time' : time,
            'pick' : breakfastpick       
        }
    elif time == '점심':
        lunchpick = random.choice(lunchmenu)
        context = {
            'name' : name,
            'time' : time,
            'pick' : lunchpick       
        }
    elif time == '저녁':
        supperpick = random.choice(suppermenu)
        context = {
            'name' : name,
            'time' : time,
            'pick' : supperpick       
        }
    return render(request, 'pages/foodmenu.html', context)

# 1. 사용자가 url경로에 이름을 입력하면
# 2. 그 이름과 무작위 음식 하나 보여주는 페이지 작성
# 2-1. random.choice(menu)
# urls -> views -> templates(html)

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'pages/catch.html', context)

# 1. 폼 태그 활용하여 사용자가 숫자 입력(로또 n장 사기)
# 2. 입력 받은 회수 만큼 반복해서
# 3. 리스트에 로또 번호를 담는다. (n번 만큼 로또 구매)
# 3-1. random.sample(range(1,46), 6)
# 4. 사용자가 입력한 숫자와 로또번호가 담긴 리스트를 출력
# 5. ul 태그를 사용하여 각 번호들을 한줄 씩 출력
# 6. urls -> views -> template
# 7. 항상 다수의 요소를 작성할 때에는 쉼표 잊지말자.
def lottobuy(request):
    return render(request, 'pages/lottobuy.html')

def lottoresult(request):
    num = int(request.GET.get('num'))
    
    lottos = []
    for data in range(num):
        lottos.append(random.sample(range(1, 46), 6))
    print("*"*30)
    for lotto in lottos:
        print(lotto.sort())
    print("*"*30)
    for lotto in lottos:
        print(sorted(lotto))
    
# 1-45 숫자 중 6개 출력
# data = random.sample(range(1, 46), 6)
# print(lotto)
# # iterable 객체로부터 정렬된 리스트를 생성
# print(sorted(lotto))
# print(lotto)
# # 리스트를 정렬된 형태로 변경
# print(lotto.sort())
# print(lotto)
    context = {
        'num' : num,
        'lottos' : lottos
        
    }
    return render(request, 'pages/lottoresult.html', context)

def artii(request):
    return render(request, 'pages/artii.html')

def result(request):
    message = request.GET.get('message')
    result = requests.get(f'http://artii.herokuapp.com/make?text={message}').text
    context = {
        'result' : result
    }
    return render(request, 'pages/result.html', context)