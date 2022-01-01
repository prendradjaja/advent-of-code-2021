import multiprocessing

def square(n):
    return n * n

if __name__ == '__main__':
    # try:
    #     cpus = multiprocessing.cpu_count()
    # except NotImplementedError:
    #     cpus = 2   # arbitrary default
    cpus = 2


    pool = multiprocessing.Pool(cpus)
    print(pool.map(square, range(10)))
