def fib(n):
    result = []
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b^2,a+b
    return result

import fibtest
import os
os.getcwd()
from fibtest import fib
fib(200)

