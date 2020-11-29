def split_and_join(line):
    # write your code here
    split_line = line.split(" ")
    outLine = split_line[0]
    for i in range(1, len(split_line)):
        outLine = outLine+"-"+split_line[i]
    return outLine


if __name__ == '__main__':
    line = 'this is a string'
    result = split_and_join(line)
    print(result)
