import textwrap


def wrap(string, max_width):
    i = 1
    outString = ""
    for q in string:
        outString += q
        if i == max_width:
            outString += "\n"
            i = 0
        i += 1
    return outString


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
