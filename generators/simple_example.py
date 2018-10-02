
def mulitples_of_five():
    i = 5
    while True:
        yield i
        i += 5


numbers = mulitples_of_five()

for i in range(10):
    print(next(numbers))
