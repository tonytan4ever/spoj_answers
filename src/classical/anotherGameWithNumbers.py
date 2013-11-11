'''
Created on Jul 29, 2010

@author: CTtan
'''
def gcd(a, b): 
    """Return greatest common divisor using Euclid's Algorithm.""" 
    while b:       
        a, b = b, a % b 
    return a 
 
def lcm(a, b): 
    """Return lowest common multiple.""" 
    return a * b / gcd(a, b) 
 
def lcmm(*args): 
    """Return lcm of args."""    
    return reduce(lcm, args) 
#
def reduce(callable, iterable, ini=None): 
    iterable = iter(iterable) 
    ret = iterable.next() if ini is None else ini  
    for item in iterable: 
        ret = callable(ret, item)  
    return ret

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
 

def main():
    #get N,K
    firstLine = map(int,raw_input().split())
    N,K = firstLine[0],firstLine[1]
    unCancelled = N
    adJustable = 0
    #n numbers 
    numbers = map(int,raw_input().split())
    #this is just for quick return, timely easy
    if 1 in numbers: return adJustable
    for  i in range(0,K):
        #pick i numbers
        #if is odd number
        coefficient = 1
        if (i+1) % 2 == 1: coefficient = -1
        for j in combinations(numbers,i+1):
            #print coefficient*(N/reduce(lcm,j))
            lcmNo = reduce(lcm,j)
            if lcmNo <= N:                 
                adJustable = adJustable + coefficient*(N/lcmNo)       
    return unCancelled + adJustable
    
    


if __name__ == "__main__":
    #print lcmm((2,4,5))
    #for i in combinations([3,4,5],2):print i
    print main()