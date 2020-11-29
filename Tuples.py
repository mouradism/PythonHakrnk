if __name__ == '__main__':
    '''
    n = int(input())
    integer_list = map(int, input().split())
    '''
    t = (1, 2)

    integer_list = map(int, t)
    print(hash(tuple(integer_list)))
