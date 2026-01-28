numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)