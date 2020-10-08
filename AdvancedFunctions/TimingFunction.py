import time, timeit


def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print("Runtime: {}".format(end-start))


def powers(limit):
    return [x**2 for x in range(limit)]


measure_runtime(lambda: powers(500000))

# current time before running the function
# start = time.time()
# running the function
# powers(5000000)
# time after running the function
# end = time.time()

# time used to run the function
# time_used = end-start

# print("Time used: {}".format(time_used))  1.0139760971069336

# timing smaller functions using 'timeit.timeit'
print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
