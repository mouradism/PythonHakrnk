def average(array):
    # your code goes here
    st = (set(array))
    return sum(st)/len(st)


if __name__ == '__main__':
    #n = int(input())
    arr = list(map(int, "161 182 161 154 176 170 167 171 170 174".split()))
    result = average(arr)
    print(result)
