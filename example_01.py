def deneme(arr):
    res1 = arr[0][0] + arr[1][1] + arr[2][2]
    res2 = arr[0][2] + arr[1][1] + arr[2][0]
    return abs(res1 - res2)

def diagonalDifference(arr):
    n = len(arr) # 3
    primary_diagonal = 0
    secondary_diagonal = 0

    for i in range(n):
        primary_diagonal += arr[i][i]
        secondary_diagonal += arr[i][n - 1 - i]

    return abs(primary_diagonal - secondary_diagonal)

arr = [[11, 2, 4], 
       [4, 5, 6], 
       [10, 8, -12]]
sonuc = deneme(arr)
result = diagonalDifference(arr)

print(result)
# print(sonuc)

# 11 + 5 + -12 = 4
# 4 + 5 + 10 = 19
# result = 15

