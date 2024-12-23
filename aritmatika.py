# Versi Iteratif
def aritmatika_iteratif(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Versi Rekursif
def aritmatika_rekursif(n):
    if n == 1:
        return 1
    return n + aritmatika_rekursif(n - 1)
