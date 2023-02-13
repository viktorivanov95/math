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
print('Поиск рабочего R и полного P диапазонов: ')
work_diapazon = numpy.prod(osn_inform) 
print('Рабочий диапазон R (произведение информационных оснований) = ', work_diapazon)
full_diapazon = numpy.prod(osn)
print('Полный диапазон P (произведение всех оснований) = ', full_diapazon)
#3. Перевод числа из СОК в ОПСС (обобщенную позиционную систему счисления)
#   (для проверки наличия ошибок)
print('Перевод числа из СОК в ОПСС (обобщенную позиционную систему счисления) для проверки наличия ошибок')
#3.1 Поиск констант с ij, являющихся мультипликативными обратными величинами
# для pi по модулю pj (c ij * pi = 1(mod pj))
print('1. Поиск констант с ij, являющихся мультипликативными обратными величинами для pi по модулю pj (c ij * pi = 1(mod pj))')
c_kolvo = 0
c = numpy.zeros((osn_kolvo-1, osn_kolvo))
for i in range(int(osn_kolvo-1)):
    for j in range(int(osn_kolvo-1)):
        try:
            c[j][i] = pow(int(osn[i]), int(-1), int(osn[j+1]))
            print('c[', j, '][', i, '] = ', c[j][i])
        except ValueError:
            continue
print('Матрица констант c ij: ')
print(c[:,:osn_kolvo-1])
#3.2 Обнуление лишних констант в матрице констант c ij
print('2. Обнуление лишних констант в матрице констант c ij')
for i in range(int(osn_kolvo-2)):
    c[i][i+1:] = 0
print('Матрица констант c ij с обнуленными лишними константами: ')
print(c[:,:osn_kolvo-1])
#3.3 Расчет числа в ОПСС
print('3. Расчет числа в ОПСС')
opss = numpy.zeros(osn_kolvo)
opss[0] = numpy.mod(chisl[0], osn[0])
print('opss[0] = ', chisl[0], '(mod', osn[0], ')', '=', opss[0])
opss[1] = numpy.mod(((chisl[1] - opss[0])*(c[0][0])), osn[1])
print('opss[1] = ', ((chisl[1] - opss[0])*(c[0][0])), '(mod', osn[1], ') = ', numpy.mod(((chisl[1] - opss[0])*(c[0][0])), osn[1]))
for i in range(2, int(osn_kolvo)):
    opss[i] = (chisl[i] - opss[0])*c[i-1][0]
    print('opss[', i, '] = (', chisl[i], '-', opss[0], ')*', c[i-1][0], '=', opss[i])
for i in range(2, int(osn_kolvo)):
    for j in range(2, int(osn_kolvo)):
        if(c[i-1][j] == 0):
            print('opss[', i, '] = (', opss[i], '-', opss[i-1], ')*', c[i-1][j-1], '(mod', osn[i], ') =', numpy.mod(((opss[i] - opss[i-1])*(c[i-1][j-1])), osn[i]))
            opss[i] = numpy.mod(((opss[i] - opss[i-1])*(c[i-1][j-1])), osn[i])
            print('opss[', i, '] = ', opss[i])
            break
        elif(c[i-1][j] != 0):
            print('opss[', i, '] = (', opss[i], '-', opss[j-1], ')*', c[i-1][j-1], '=', (opss[i] - opss[j-1])*c[i-1][j-1])
            opss[i] = (opss[i] - opss[j-1])*c[i-1][j-1]
            print('opss[', i, '] = ', opss[i])
print('Число в ОПСС равно: ', opss)
#3.4 Проверка числа на наличие ошибок
print('4. Проверка числа на наличие ошибок')
check = 0
for i in range(osn_inform_kolvo, osn_kolvo):
    if(opss[i] != 0):
        print(chisl, ' - представление числа, содержащее ошибку (ошибки), т.к. число в ОПСС по хотя бы одному контрольному основанию не равно нулю')
        break;
    elif(opss[i] == 0):
        check = check + 1
    if(check == osn_kontrol_kolvo):
        print(chisl, ' - число не содержит ошибку (ошибок), т.к. число в ОПСС по всем контрольным основаниям равно нулю')
print('Перевод числа из СОК в ОПСС (для проверки ошибок) завершен')
#3.5 Дополнительная проверка (переведем число в позиционную систему счисления методом ортогональных базисов
#а также переводом в позиционную систему из ОПСС, и сравним их)
print('5. Дополнительная проверка (переведем число в позиционную систему счисления методом ортогональных базисов, а также переводом в позиционную систему из ОПСС, и сравним их)')
print('Вычисление ортогональных базисов на основе китайской теоремы об остатках (для проверки на наличие ошибок в числе):')
#3.5.1 Поиск величины P/pi = Pi для каждого основания
print('5.1 Поиск величины P/pi = Pi для каждого сонования, где P - полный диапазон, pi - i-ое основание:') 
P = numpy.zeros(osn_kolvo)
for i in range(osn_kolvo):
    P[i] = full_diapazon/osn[i]
print('Величина P = ', P)
#3.5.2 Поиск величины βi = Pi(modpi)
print('5.2 Поиск величины βi = Pi(modpi):')
beta = numpy.zeros(osn_kolvo)
for i in range(osn_kolvo):
    beta[i] = numpy.mod(P[i], osn[i])
print('Величина β =', beta)
#3.5.3 Нахождение веса mi базисов, m принадлежит Z, m1 * βi = 1(modpi)
print('5.3 Нахождение весов mi базисов, m принадлежит Z, m1 * βi = 1(modpi):')
m = numpy.zeros(osn_kolvo)
for i in range(osn_kolvo):
    m[i] = pow(int(beta[i]), int(-1), int(osn[i]))
print('Веса базисов m = ', m)
#3.5.4 Вычисление ортогональных базисов системы
print('5.4 Вычисление ортогональных базисов системы B, равное произведению веса базиса mi на величину Pi')
B = numpy.zeros(osn_kolvo)
for i in range(osn_kolvo):
    B[i] = m[i]*P[i]
print('Ортогональные базисы системы B = ', B)
#3.5.5 Нахождение числа в ПСС
print('5.5 Нахождение числа A в позиционной системе счисления (десятичной), с помощью суммирования всех произведений введенного числа i на ортогональный базис Bi, и затем mod полный диапазон')
A = 0
for i in range(osn_kolvo):
    if(i==0):
        print('A[', i, '] = 0 + ', int(chisl[i]), '*', int(B[i]), '=', int(chisl[i]*B[i]))
    elif(i>0):
        print('A[', i, '] = ', int(A), '+', int(chisl[i]), '*', int(B[i]), '=', int(A+chisl[i]*B[i]))
    A = int(A + chisl[i]*B[i])
print('A = ', A, 'mod(', full_diapazon, ')')
A = numpy.mod(A, full_diapazon)
print('Число А (переведенное с помощью метода ортогональных базисов = ', int(A))
#3.5.6 Проверка числа, переведенного в ОПСС, на правильность, переводом в позиционную систему
opss_check = 0
for i in range(osn_kolvo):
    print(opss_check, '+', opss[i], '*', numpy.prod(osn[0:i]), '=', opss_check + opss[i]*numpy.prod(osn[0:i]))
    opss_check = opss_check + opss[i]*numpy.prod(osn[0:i])
print('Число А (переведенное в позиционную систему счисления из СОК = ', opss_check)
if(int(opss_check) == int(A)):
    print(int(opss_check), '=', int(A))
    print('Число в ОПСС переведено правильно')
else:
    print(int(opss_check), '!=', int(A))
    print('Число в ОПСС переведено неправильно, есть ошибка')
