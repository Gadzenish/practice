#chance = 10
#while True:
#    print("Добро пожаловать в 'Угадай слово':\n")
#    word = 'дом'
#    guess_word = input('Введи слово:\n')
#    if word == guess_word:
#        print("Ты победил:\n")
#        break
#    if word != guess_word:
#        chance -= 1
#    if chance<1:
#        print("Ты проиграл:\n")
#        break

#while True:
#    print("Добро пожаловать в простейший калькулятор!:\n")
#    number_a = int(input('Введите число:\n'))
#    operator = input('Введите математический оператор:\n')
#    number_b = int(input('Введите число:\n'))
#    word = ''
#    if operator == '+':
#        print(number_a + number_b)
#    if operator == '-':
#        print(number_a - number_b)
#    if operator == '/':
#        print(number_a / number_b)
#    if operator == '*':
#        print(number_a * number_b)
#    if operator == '**':
#        print(number_a ** number_b)
#    print("Хотите ли вы продолжить работу с калькулятором?:\n")
#    word = input()
#    if word==('Нет') or word==('нет'):
#        break
#print("Формула вычисления Дискриминанта")
#discriminant = ''
#a = float(input('Введите значение a:\n'))
#b = float(input('Введите значение b:\n'))
#c = 10
#discriminant = b**2 - 4*a*c
#print(discriminant)

#import math
#print("Формула нахождения Площади")
#area = ''
#a = float(input('Введите значение a:\n'))
#area = a**2 * math.sqrt(3)/4
#print(area)

#print("Формула нахождения Радиуса")
#r = ''
#a = float(input('Введите значение a:\n'))
#b = float(input('Введите значение b:\n'))
#c = float(input('Введите значение c:\n'))
#r = (a+b-c)/2
#print(round(r))

#print("Формула нахождения Площади")
#area = ''
#R = float(input('Введите значение R:\n'))
#r = float(input('Введите значение r:\n'))
#Pi = 3.14
#area = Pi*(R**2-r**2)
#print(round((area)))

#print("Формула нахождения Объёма")
#V = ''
#Pi = 3.14
#R = float(input('Введите значение R:\n'))
#h = float(input('Введите значение h:\n'))
#V = (Pi*R**2*h)/3
#print(round(V))

#import math
#print("Формула вычисления Длины")
#l = ''
#h = float(input('Введите значение h:\n'))
#R = float(input('Введите значение R:\n'))
#l = math.sqrt(h**2+R**2)
#print(l)

#print("Формула нахождения Объёма")
#V = ''
#Pi = 3.14
#R = float(input('Введите значение R:\n'))
#V = 4/3*Pi*R**2
#print(round(V))

#import math
#print("Формула нахождения Периметра")
#P = ''
#F = float(input('Введите значение F:\n'))
#v = float(input('Введите значение V:\n'))
#a = float(input('Введите значение a:\n'))
#P = F*v*math.cos(a)
#print(round(P))

#import math
#print("Формула вычисления Силы")
#F = ''
#k = float(input('Введите значение k:\n'))
#q1 = float(input('Введите значение q1:\n'))
#q2 = float(input('Введите значение q2:\n'))
#r = float(input('Введите значение r:\n'))
#F = k*(math.fabs(q1)*math.fabs(q2))/r**2
#print(F)

#import math
#print("Формула вычисления расстояний между точками в системе отчета")
#L = ''
#L0 = 5
#V = float(input('Введите значение V:\n'))
#c = float(input('Введите значение c:\n'))
#L = L0*math.sqrt(1-(V**2/c**2))
#print(round(L))

#a = float(input('Введите значение a:\n'))
#b = float(input('Введите значение b:\n'))
#c = float(input('Введите значение c:\n'))
#if a>0:
#    print(a)
#if b>0:
#    print(b)
#if c>0:
#    print(c)

#a = input('Введите число забитых голов,хозяевами:\n')
#b = input('Введите число забиты голов,гостями:\n')
#if a>b:
#    print("Победили хозяева!")
#if a==b:
#    print("Ничья")
#if a<b:
#    print("Победили гости")

#a = float(input('Введите первое число:\n'))
#b = float(input('Введите второве число:\n'))
#if a % 2:
#    print(a)
#if b % 2:
#    print(b)

#chislo = float(input('Введите число:\n'))
#if chislo % 2:
#    print("Число нечетное")
#if chislo > 9:
#    print("Число двухзначное")
#if chislo % 10 == 5:
#    print("Число заканчивается на 5")
