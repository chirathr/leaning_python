
def mulitples_of_five():
    i = 5
    while i <= 100:
        yield i
        i += 5

for i in mulitples_of_five():
    print(i)
