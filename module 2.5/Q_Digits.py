def print_digits_reverse(n):
    digits = []
    
    while n > 0:
        digit = n % 10
        digits.append(digit)
        n //= 10
    
    print(*digits[::1])

T = int(input())

for _ in range(T):
    N = int(input())
    print_digits_reverse(N)
