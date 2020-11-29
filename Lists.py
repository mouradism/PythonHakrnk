'''
if __name__ == '__main__':
    N = int(input())
    # print(N)
    done = False
    list_ = []
    while(~done):
        inputRaw = input()
        print(inputRaw)
        input_ = inputRaw.split(' ')
        print(input_[0])
        if input_:
            print(input_[0])
            if input_[0] == 'insert':
                list_.insert(int(input_[1]), int(input_[2]))
            elif input_[0] == 'print':
                print(list_)
            elif input_[0] == 'remove':
                list_.remove(int(input_[1]))
            elif input_[0] == 'append':
                list_.append(int(input_[2]))
            elif input_[0] == 'sort':
                list_.sort()
            elif input_[0] == 'pop':
                list_.pop()
            elif input_[0] == 'reverse':
                list_.reverse()

        else:
            done = True
'''
if __name__ == '__main__':
    N = int(input())

    list_ = []
    for i in range(0, N):
        input_ = input().split()

        if input_[0] == 'insert':
            list_.insert(int(input_[1]), int(input_[2]))
        elif input_[0] == 'print':
            print(list_)
        elif input_[0] == 'remove':
            list_.remove(int(input_[1]))
        elif input_[0] == 'append':
            list_.append(int(input_[1]))
        elif input_[0] == 'sort':
            list_.sort()
        elif input_[0] == 'pop':
            list_.pop()
        elif input_[0] == 'reverse':
            list_.reverse()
