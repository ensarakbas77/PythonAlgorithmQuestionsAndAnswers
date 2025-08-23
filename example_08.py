# [1, 1 ,1, 3, 5, 9, 17, 31, 57, ...] 
# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

def tribonacci(signature: list[int], n: int) -> list[int]:
    # n=0 için boş liste
    if n == 0:
        return []
    # n<3 için signature'ın kırpılmış hali
    if n <= 3:
        return signature[:n]
    
    seq = signature[:]  # kopya al
    # n uzunluğa ulaşana kadar son 3 elemanın toplamını ekle
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2] + seq[-3])
    return seq

# Örnekler
print(tribonacci([1, 1, 1], 10))  # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
print(tribonacci([0, 0, 1], 10))  # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
print(tribonacci([1, 2, 3], 0))   # []
print(tribonacci([1, 2, 3], 2))   # [1, 2]


# Fibonacci (Recursive)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
print("********** Fibonacci **********")

def fibonacci(n):
    # Base cases
    if n==0:
        return 0

    elif n==1:
        return 1

    else:
        # Recursive case
        return fibonacci(n-2) + fibonacci(n-1)

num=6
for i in range(0,num):
    print(fibonacci(i))
