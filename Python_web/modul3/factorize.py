from time import time


def factorize(*numbers):
    list_result = ''
    for number in numbers:
        list_division = []
        i = 1
        while i <= number:
            if not number % i:
                list_division.append(i)
            i += 1
        list_result += f'for {number} is {list_division}\n'
    return list_result


if __name__ == "__main__":
    time_start = time()
    print(factorize(128, 255, 99999, 10651060))
    time_delta = time()-time_start
    print(round(time_delta, 4))
