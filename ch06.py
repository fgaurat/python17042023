import fibo as fb
import sys

# from fibo import fib as the_fib
# from fibo import *

if __name__=="__main__":
    print("module ch06",__name__)
    print(sys.argv)
    if len(sys.argv)>1:
        value = int(sys.argv[1])
        fb.fib(value)
        a = fb.fib2(value)
    else:
        print("Hoooooooo ! ")

