# List Comprehension
even_numbers = [x for x in range(20) if x % 2 == 0]
squares = [x * x for x in range(10)][1:]
even_squares = [x * x for x in even_numbers][1:]

# List to Dictionaries
square_dict = {x:x*x for x in range(10)}
square_set = {x * x for x in [1, -1, 2, -2]} # mengatasi duplikasi

zeros = [0 for _ in range(10)]

pairs = [(x, y) for x in range(10) for y in range(10)]
increasing_pairs = [(x, y) for x in range(10) for y in range(x+1, 10)]

# print(increasing_pairs)
angka = [x for x in range(10)]

odd_numbers = [x for x in angka if x % 2 == 1]

print(pairs)