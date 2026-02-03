def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)
num = int(input("Enter a number: "))
if num == 0:
    print(1)
else:
    print(count_digits(abs(num)))
