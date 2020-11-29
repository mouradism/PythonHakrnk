def count_substring(string, sub_string):
    count = 0
    if len(string) < len(sub_string):
        return 0
    for i in range(0, len(string)-len(sub_string)+1):
        sub = True
        for j in range(0, len(sub_string)):
            if(string[i+j] != sub_string[j]):
                sub = False
        if sub:
            count += 1
    return count


if __name__ == '__main__':
    string = "I am an Indian, by birth."
    sub_string = "Birth"

    count = count_substring(string, sub_string)
    print(count)
