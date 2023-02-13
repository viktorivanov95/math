# 1. Введение оснований и чисел
import numpy
print('Основания нужно вводить в порядке возрастания: сначала информационные, затем контрольные. Они должны быть взаимно простыми')
osn_inform_kolvo = int(input('Введите количество информационных оснований '))
osn_kontrol_kolvo = int(input('Введение количество контрольных оснований '))
osn_inform = numpy.zeros((osn_inform_kolvo), dtype=int)
osn_kontrol = numpy.zeros((osn_kontrol_kolvo), dtype=int)
osn_kolvo = osn_inform_kolvo + osn_kontrol_kolvo
chisl = numpy.zeros((osn_kolvo), dtype=int)
for i in range(osn_inform_kolvo):
    osn_inform[i] = int(input(f'Введите {i+1} информационное основание '))
for i in range(osn_kontrol_kolvo):
    osn_kontrol[i] = int(input(f'Введите {i+1} контрольное основание '))
for i in range(osn_kolvo):
    chisl[i] = int(input(f'Введите {i+1} число '))
print('Введенные информационные основания = ', osn_inform)
print('Введенные контрольные основания = ', osn_kontrol)
osn = numpy.concatenate((osn_inform, osn_kontrol))
print('Информационные и контрольные основания = ', osn)
print('Введенное число = ', chisl)
#2. Вычисление ортогональных базисов на основе китайской теоремы об остатках
# (для проверки одиночной ошибки)
print('Вычисление ортогональных базисов на основе китайской теоремы об остатках (для проверки на наличие ошибок в числе):')
#2.1 Поиск рабочего R и полного P диапазонов
print('1. Поиск рабочего R и полного P диапазонов: ')
work_diapazon = numpy.prod(osn_inform) 
print('Рабочий диапазон R (произведение информационных оснований) = ', work_diapazon)
full_diapazon = numpy.prod(osn)
print('Полный диапазон P (произведение всех оснований) = ', full_diapazon)
#2.2 Поиск величины P/pi = Pi для каждого основания
print('2. Поиск величины P/pi = Pi для каждого сонования, где P - полный диапазон, pi - i-ое основание:') 
P = numpy.zeros(osn_kolvo)
for i in range(osn_kolvo):
    P[i] = full_diapazon/osn[i]
print('Величина P = ', P)
#2.3 Поиск величины βi = Pi(modpi)
print('3. Поиск величины βi = Pi(modpi):')
beta = numpy.zeros(osn_kolvo)
for i in range(osn_kolvo):
    beta[i] = numpy.mod(P[i], osn[i])
print('Величина β =', beta)
#2.4 Нахождение веса mi базисов, m принадлежит Z, m1 * βi = 1(modpi)
print('4. Нахождение весов mi базисов, m принадлежит Z, m1 * βi = 1(modpi):')
m = numpy.zeros(osn_kolvo)
for i in range(osn_kolvo):
    m[i] = pow(int(beta[i]), int(-1), int(osn[i]))
print('Веса базисов m = ', m)
#2.5 Вычисление ортогональных базисов системы
print('5. Вычисление ортогональных базисов системы B, равное произведению веса базиса mi на величину Pi')
B = numpy.zeros(osn_kolvo)
for i in range(osn_kolvo):
    B[i] = m[i]*P[i]
print('Ортогональные базисы системы B = ', B)
#2.6 Нахождение числа в ПСС
print('6. Нахождение числа A в позиционной системе счисления (десятичной), с помощью суммирования всех произведений введенного числа i на ортогональный базис Bi, и затем mod полный диапазон')
A = 0
for i in range(osn_kolvo):
    if(i==0):
        print('A[', i, '] = 0 + ', int(chisl[i]), '*', int(B[i]), '=', int(chisl[i]*B[i]))
    elif(i>0):
        print('A[', i, '] = ', int(A), '+', int(chisl[i]), '*', int(B[i]), '=', int(A+chisl[i]*B[i]))
    A = int(A + chisl[i]*B[i])
print('A = ', A, 'mod(', full_diapazon, ')')
A = numpy.mod(A, full_diapazon)
print('A = ', int(A))
#2.7 Проверка числа
print('7. Проверка числа')
print('Так как A = ', int(A), 'а рабочий диапазон равен ', work_diapazon, ' то:')
if(A>work_diapazon):
    print(chisl, ' - представление числа, содержащее ошибку (ошибки)')
else:
    print(chisl, ' - число не содержит ошибки (ошибок)')

print('Вычисление ортогональных базисов на основе китайской теоремы об остатках (для проверки ошибок) завершено')
