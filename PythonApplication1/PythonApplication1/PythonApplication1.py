from ast import Num
import math
import matplotlib.pyplot as plt


#num1 = int(input('vvedite chislo1'))
#num2 = int(input('vvedite chislo2'))
#num3 = int(input('vvedite chislo3'))
#num4 = int(input('vvedite chislo4'))


#if num1 % 2 == 0:
#    print('chislo chetnoe')
#else:
#    print('chislo ne chetnoe')

#if num1 % 2 == 0 or num2 % 2 == 0 or num3 % 2 == 0 or num4 % 2 == 0:
#    print('est chislo chetnoe')

#if num1 % 2 == 0:
#    if num2 % 2 == 0:
#        if num3 % 2 == 0:
#            if num4 % 2 == 0:
#                print('est chetnoe chislo')
#            else:
#                print('chetnoe chislo v pervix trex')
#        else:
#            print('chetnoe chislo v pervix dvux')
#    else: 
#        print('chetnoe chislo pervoe')
#else:
#    print('net chetnix')

## Напишите программу, которая определяет квартал года по введенному пользователем номеру месяца.
## Если пользователь вводит некорректный номер, то программа сообщает об ошибке

#month = int(input('vvedite mesiach '))

#if 1 <= month <= 3:
#    print('pervii kvartal')
#elif 4 <= month <= 6:
#    print('2 kvartal')
#elif 7 <= month <= 9:
#    print('3 kvartal')
#elif 10 <= month <= 12:
#    print('4 kvartal')
#else:
#    print('eror')


# Пользователь вводит длины трех сторон треугольника и определяет, является ли он прямоугольным.

#a = float(input('vvedite dlinu 1 storoni'))
#b = float(input('vvedite dlinu 2 storoni'))
#c = float(input('vvedite dlinu 3 storoni'))

#if a > 0 and b > 0 and c > 0:
#    if a == math.sqrt(math.pow(b,2) + c**2) or b == math.sqrt(a**2 + c**2) or c == math.sqrt(a**2 + b**2):
#        print('treugolnik priamougolnii')
#    else:
#        print('ne primougolnii')
#else:
#    print('eror!!!')

number = 5
factorial = math.factorial(number)
print('factorial chisla ', number, "raven: ", factorial)

#построим график функции y = x^2

x = range(-10, 11)
y = [x_val**2 for x_val in x]
5
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphic funcii y = x^2')
plt.grid(True)
plt.show()

