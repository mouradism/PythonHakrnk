def print_formatted(number):
    # your code goes here
    for i in range(1, n+1):
        l = len(bin(number)[2:])
        print(f'{i}'.rjust(l, ' '), end=" ")
        print(f'{i:o}'.rjust(l, ' '), end=" ")
        print(f'{i:x}'.upper().rjust(l, ' '), end=" ")
        print(f'{i:b}'.rjust(l, ' '), end=" ")
        print('')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
