import random

def sortowanie(lista,n):
    for i in range(n):
        for j in range(1,n):
            if lista[j-1] > lista[j]:
                temp = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = temp
    return lista

lista = []
n = input('Podaj dlugosc listy: ')
n = int(n)
for x in range(n):
    x = random.randint(0,100) #zakres liczb
    lista.append(x)

print('Lista nie posortowana: ')
print(lista)

print('======================')

print('Lista posortowana')
print(sortowanie(lista,n))