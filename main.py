def main():
    total = 0

    ## Lab 4-4
    
    numbers = [0] * 5
    for i in range(len(numbers)):
        numbers[i] = int(input('Enter a value: '))

    print(numbers)
    for v in numbers:
        total += v
    
    print(total)

    return total, numbers


if __name__ == '__main__':
    main()
