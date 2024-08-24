def even_or_odd(num):
    if isinstance(num, (int, float)):
        if num % 2 == 0:
            return "Even"
        return "Odd"
    return "Must be numbers"


print(even_or_odd(10))
print(even_or_odd(23))
print(even_or_odd("Hello"))
