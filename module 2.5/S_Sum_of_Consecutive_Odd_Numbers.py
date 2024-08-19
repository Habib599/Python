def sum_of_odd_numbers_between(X, Y):
    
    total_sum = 0
    
    if X > Y:
        X, Y = Y, X
    
    # Iterate through numbers from X+1 to Y-1
    for num in range(X + 1, Y):
        # Check if the number is odd
        if num % 2 != 0:
            total_sum += num
    
    return total_sum

# Input the number of test cases
T = int(input())


for _ in range(T):
    X, Y = input().split()
    X, Y = int(X), int(Y)
    result = sum_of_odd_numbers_between(X, Y)
    print(result)
