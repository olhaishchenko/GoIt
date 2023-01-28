from time import time
from multiprocessing import Pool, cpu_count


def factorize(number):
    list_division = []
    i = 1
    while i <= number:
        if not number % i:
            list_division.append(i)
        i += 1
    return list_division

def callback(result):
    print(f"Result: {result}")


if __name__ == "__main__":
    time_start = time()
    with Pool(cpu_count()) as p:
        p.map_async(
           factorize,
            [128, 255, 99999, 10651060],
            callback=callback,
        )
        p.close()  # перестати виділяти процеси в пулл
        p.join()  # дочекатися закінчення всіх процесів
    time_delta = time() - time_start
    print(round(time_delta, 4))

# a, b, c, d  = factorize(128, 255, 99999, 10651060)
#
# assert a == [1, 2, 4, 8, 16, 32, 64, 128]
# assert b == [1, 3, 5, 15, 17, 51, 85, 255]
# assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
