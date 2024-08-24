def sum_numbers(a, b=None):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    return "Must be numbers"


print(sum_numbers(10, 20))
print(sum_numbers("Hello", 20))
print(sum_numbers(10))
