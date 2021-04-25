import numpy as np
# # Zad 1
# # Za pomocą funkcji arange stwórz tablicę numpy składającą się z 15 kolejnych wielokrotności liczby 3.
# a = np.arange(3, 46, +3)
# print(a)

# # Zad 2
# # Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64
# b = np.arange(0, 1, +0.1) #, dtype = 'int64'
# print(b)
# print(b.dtype)
# a = b.astype('int64')
# print(a.dtype)

# # Zad 3
# # Napisz funkcję, która będzie:
# # * Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# # * Zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1
# n = 3
# c = np.arange(1,int(n)**2)
# print(c)

# # Zad 4
# # Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji
# # potęgowania oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj
# # tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]
# d = 2
# IlePoteg = 4
# liczby = np.logspace(d,d**IlePoteg,IlePoteg)
# print(liczby)

# Zad 5
# Napisz funkcję, która:
# * Na wejściu przyjmuje jeden parametr określający długość wektora
# * Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# * Generuj macierz diagonalną z w/w wektorem jako przekątną
DlugoscWektora = 4

# a = np.array(b for b in range(5))
# print(a)



