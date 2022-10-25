# Zadanie 1

# n = 30
# for i in range(1, n + 1,):
#     print(i, "Listopada")


# Zadanie 2

# print("Wprowadź ilość potrzebnych liczb")
# k = int(input())
# n = 1
# for i in range(n, k, 2):
#     print(i * i)



# Dodatkowe pierdoły

# import math
# p_inf = math.inf
# n_inf = -math.inf

# print("Nieskończoność dodatnia = ",p_inf)
# print(math.isinf(p_inf))



# n = 1
# for i in range(n, p_inf, 2):
#     print(i * i)


# Zadanie 3

# a = 1000
# for i in range(a, 9999, 1):
#     if (i % 379 == 0):
#         print(i)


# Zadanie 4
# Nie jestem pewny czy dobrze zrozumiałem polecenie dlatego 2 wersje.


# Wersja 1

# a = 100
# b = 1000
# for i in range(a, b, 1):
#     if (i % 5 == 0) or (i % 6 == 0) or (i % 11 == 0):
#         print(i)


# Wersja 2

# a = 100
# b = 999
# for i in range(a, b, 1):
#     if ((i % 5 == 0) and (i % 6 == 0)) or (i % 11 == 0):
#         print(i)


# Zadanie 5

# suma = 0
# n = int(input())
# for i in range(0, n):
#     suma += int(input())
# print(suma)


# Zadanie 6

# k = int(input())
# suma = 0
# for i in range(0, k * 2, 2):
#   suma += (i)
# print(suma)


# Zadanie 7

# m = int(input())
# suma = 0
# for i in range(11, (m * 2) + 11, 2):
#   suma += i
# print(suma)


# Zadanie 8

# print("Wpisz kwotę")
# W0 = int(input())
# print("Wpisz czas")
# L = int(input())
#
# zarobek = W0
# for i in range(0, (2 * L), 1):
#   for j in range(6):
#     zarobek = zarobek * 1.005
# print(zarobek)


# Zadanie 9

# n = int(input())
# suma = 0
# for i in range(21, (n * 100) + 21, 100):
#   suma += i
# print(suma)

# Zadanie 10

# a = 1
# b = 32
# for i in range(a, b , 1):
#     c = (i * i)
#     if (i < 10):
#         while c > 10:
#             c -= 10
#     else:
#         while c >= 100:
#             c -= 100
#     if i == c:
#         print(i * i)