import math
from timer import timer

# @timer
def factorial(*arg,**kwarg):
    i=math.factorial(10e5)
    return i


if __name__=="__main__":
    i=factorial()
    # print(f'output is {i}')