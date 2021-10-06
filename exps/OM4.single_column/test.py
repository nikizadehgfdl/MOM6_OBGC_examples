#!/bin/env python
#Initially copied from https://github.com/wangsl/python-embedding
import sys
from math import sin
#import torch
#import numpy  #This gives all kinds of library errors at runtime

def my_test0(x, y) :
    print(' From Python test: {}'.format(x.size))
    for i in range(x.size) :
        x[i] += 1.0

    a = torch.from_numpy(x)
    print(a)

    b = torch.from_numpy(x.astype(numpy.float32))
    print(b)

    if torch.cuda.is_available() :
        b_dev = b.cuda()
        print(b_dev)

    for i in range(y.size) :
        y[i] = 2*numpy.float64(b[i]) + 0.1

    print(y)

    sys.stdout.flush()
    
def my_test(x) :
    print(' **** From my_test1 ****',x)
    sys.stdout.flush()
    a=sum(x)
    return a

def my_test2(x,y) :
    print(' **** From my_test2 ****',x,y)
    sys.stdout.flush()
    a=sum(x)
    b=sum(y)
    return a,b

if __name__ == '__main__' :
    import numpy as np

    x = np.arange(10, dtype=numpy.float64)
    print(x)

    y = np.arange(10, dtype=numpy.float64)
    print(y)
    my_test(x, y)

    print(x)


