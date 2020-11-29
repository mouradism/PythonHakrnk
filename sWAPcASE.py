def swap_case(s):
    s_out = ""
    for s_ in s:
        if s_.islower():
            s_ = s_.upper()
        else:
            s_ = s_.lower()
        s_out += s_

    return s_out


if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)
