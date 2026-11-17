from time import perf_counter


def benchmark(operation, repeats=100):
    start = perf_counter()
    for _ in range(repeats):
        operation()
    return perf_counter() - start
