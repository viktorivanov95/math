import numpy as np
import time
number = int(input('Введите число '))
double_number_sqrt = int((2*number)**(0.5))
print('Rвадратный корень из двойного введенного числа (', 2*number, ') равен ', double_number_sqrt)
start_time = time.time()

def main(number):
    b = 0
    c = 0
    f = -1
    quantity = 0
    for a in range(0, number+1):
        e = 1
        g = 1
        h = 1
        b = number-a
        c = number+a
        f = f+1;
        if(b!=c and b>double_number_sqrt):
            for d in range(2, double_number_sqrt+1):
                if(b%d==0 or c%d==0):
                    print(b, '/', d, '= 0 или ', c, '/', d, '=0, поэтому break, d = ', d, ' e =', e)  
                    break
                elif(b%d!=0 and c%d!=0):
                    e = e+1;
                    print(b, '/', d, '!= 0 и ', c, '/', d, '!=0, поэтому идем дальше, d = ', d, ' e =', e) 
                else: break
                if(e==double_number_sqrt):            
                    quantity = quantity + 1
                    print('все d посмотрели, следовательно ', b, ' и ', c, ' - простые числа!, quantity = ', quantity)
        if(b>=2 and b<=double_number_sqrt):
            for d in range(2, double_number_sqrt+1):
                if(b>d and b%d==0):
                    print(b, '!=', d, ' и ', b, '/', d, '=', 0, ' поэтому break, d = ', d, ' g =', g)
                    break
                elif(b>d and c%d==0):
                    print(b, '!=', d, ' и ', c, '/', d, '=', 0, ' поэтому break, d = ', d, ' h =', h)
                    break
                if(b>d and b%d!=0):
                    g = g+1
                    print(b, '!=', d, ' и ', b, '/', d, '!=', 0, ' поэтому идем дальше, d = ', d, ' g =', g)
                if(b>d and c%d!=0):
                    h = h+1
                    print(b, '!=', d, ' и ', c, '/', d, '!=', 0, ' поэтому идем дальше, d = ', d, ' h =', h) 
                if(b<=d and c%d==0):
                    print(b, '<=', d, ' и ', c, '/', d, '=', 0, ' поэтому break, d = ', d, ' h =', h)
                    break
                if(b<=d and c%d!=0):
                    h = h+1
                    print(b, '<=', d, ' и ', c, '/', d, '!=', 0, ' поэтому идем дальше, d = ', d, ' h =', h)
                if(g == b-1 and h == double_number_sqrt):
                    quantity = quantity + 1
                    print(b, ' и ', c, ' - простые числа!, quantity = ', quantity, 'g = ', g, ' h = ', h)
    return quantity

print(main(number))
print("--- %s seconds ---" % (time.time() - start_time))
print('Программа завершена')
input('Press ENTER to exit')
