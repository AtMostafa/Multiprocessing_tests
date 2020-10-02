from factorial import factorial
from multiprocessing import Pool, Process
import os
from timer import timer

bigN=15

#Normal running
@timer
def normal_main():
    iterList=range(bigN)
    out=[]
    for i in iterList:
        out.append(factorial())
    
    return out

#Parallel Running
@timer
def parallel_main():
    iterList=range(bigN)

    with Pool(processes=os.cpu_count()) as pool:
        out=pool.map(factorial,iterList)
    
    return out


if __name__=="__main__":
    out=normal_main()
    print(f'{type(out)=},{len(out)=}')

    out=parallel_main()
    print(f'{type(out)=},{len(out)=}')