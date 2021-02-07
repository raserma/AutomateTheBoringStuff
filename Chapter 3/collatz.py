def collatz(collatz_n):
    if collatz_n % 2 == 0:
        return collatz_n//2
    else:
        return 3*collatz_n+1


if __name__ == '__main__':
    collatz_series = []
    try:
        number = int(input('Introduce a number: '))
        while number != 1:
            number = collatz(number)
            collatz_series.append(number)
    except ValueError:
        print('Please, use a valid integer.')

    print('Your collatz series is ', {str(collatz_series)})


