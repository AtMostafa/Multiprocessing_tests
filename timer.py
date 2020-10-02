import time

def timer (func):
    def wrapper(*arg,**kwarg):
        t0=time.perf_counter()
        out=func(*arg,**kwarg)
        dt=time.perf_counter()-t0
        print(f'elapsed time is {dt=:.3f}s')
        return out
    return wrapper
