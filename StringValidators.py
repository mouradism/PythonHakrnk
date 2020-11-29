if __name__ == '__main__':
    s = "qA2"
    result_ = [False, False, False, False, False]
    for q in s:
        result_[0] = result_[0] or q.isalnum()
        result_[1] = result_[1] or q.isalpha()
        result_[2] = result_[2] or q.isdigit()
        result_[3] = result_[3] or q.islower()
        result_[4] = result_[4] or q.isupper()
    for r in result_:
        print(r)
