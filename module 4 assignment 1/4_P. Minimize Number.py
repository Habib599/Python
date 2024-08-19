def even(arr):
    for num in arr:
        if num % 2 != 0:
            return False
    return True

n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])

operation = 0
while even(arr):
    for i in range(n):
        arr[i] //= 2
    operation += 1

print(operation)
