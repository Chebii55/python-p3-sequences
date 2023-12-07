#!/usr/bin/env python3

def print_fibonacci(length):
    x = [0, 1]

    while len(x) < length:
        a = x[-1] + x[-2]
        x.append(a)

    print(x[:length])

    
    
