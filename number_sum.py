
def positional_sum(num):
    total = 0
    for char in str(num):
        total += int(char)

    return total

def positional_sum2(num):
    total = 0
    while num > 0:
        remainder = num % 10
        total += remainder
        num = int(num / 10)

    return total

print(positional_sum(3456))