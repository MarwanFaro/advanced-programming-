products = [" LAPTOP ", "phone ", " Tablet", "CAMERA "]

cleaned_products = list(map(lambda p: p.strip().title(), products))
print(cleaned_products)




celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (9/5)*c + 32, celsius))
print(fahrenheit)





nums = [1, 2, 3, 4, 5]

transformed = list(map(lambda n: n**2 + 10, nums))
print(transformed)





words = ["python", "lambda", "programming", "map", "function"]

first_last = list(map(lambda w: (w[0], w[-1]), words))
print(first_last)
