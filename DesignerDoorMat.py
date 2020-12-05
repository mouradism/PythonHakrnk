# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
if __name__ == '__main__':

    inp_ = input().split(' ')
    N = int(inp_[0])
    M = int(inp_[1])

    for i in range(0, N):
        out = ""
        if i < (N-1)/2:
            out += 3*(int((N-1)/2)-i)*"-"
            out += (2*i+1)*".|."
            out += 3*(int((N-1)/2)-i)*"-"
            print(out)
        elif i == (N-1)/2:
            out += int((3*N-7)/2)*"-"+"WELCOME"+int((3*N-7)/2)*"-"
            print(out)
        elif i >= (N-1)/2:
            out += 3*(i-int((N-1)/2))*"-"
            out += (2*(N-i)-1)*".|."
            out += 3*(i-int((N-1)/2))*"-"
            print(out)
