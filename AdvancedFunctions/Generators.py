# Generator functions return a generator object. This generator objects are used by either calling
# the 'next() method' on the generator object of using the generator object in a 'for loop'.
def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1


g = hundred_numbers()

print(next(g))  # 0
print(next(g))  # 1

double_g = next(g)
print(double_g ** 2)  # 2

print(list(g))  # 3-99
