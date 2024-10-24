from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        results = pool.map(square, range(10))
        
    print(results)