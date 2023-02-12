import numpy
osn_inform_kolvo = int(input('Введите количество информационных оснований '))
osn_kontrol_kolvo = int(input('Введение количество контрольных оснований '))
osn_inform = numpy.zeros((osn_inform_kolvo), dtype=int)
osn_kontrol = numpy.zeros((osn_kontrol_kolvo), dtype=int)
osn_kolvo = osn_inform_kolvo + osn_kontrol_kolvo
for i in range(osn_inform_kolvo):
    osn_inform[i] = int(input(f'Введите {i+1} информационное основание '))
for i in range(osn_kontrol_kolvo):
    osn_kontrol[i] = int(input(f'Введите {i+1} контрольное основание '))
print('osn_inform = ', osn_inform)
print('osn_kontrol = ', osn_kontrol)
osn = numpy.concatenate((osn_inform, osn_kontrol))
print('osn = ', osn)
work_diapazon = numpy.prod(osn_inform) 
print('work_diapazon = ', work_diapazon)
full_diapazon = numpy.prod(osn)
print('full diapazon = ', full_diapazon)
for i in range(full_diapazon):
    if(i==work_diapazon):
        print('=============================')
    a = numpy.mod(i, osn)
    print('i = ', i, 'a = ', a)

