def mutate_string(string, position, character):
    outList = [string[i:i+1] for i in range(0, len(string), 1)]
    outList[position]=character
    return "".join(outList)


if __name__ == '__main__':
    s = "abracadabra"
    i, c = "5 k".split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
