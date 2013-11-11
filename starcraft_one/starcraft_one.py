'''
Created on January 11, 2011

SPOJ Problem Set (classical)
2643. Starcraft I
Problem code: SC1

@author: tony
'''
def ceil(a,b):
    """quick ceiling function for
       dividend: a
       divisor:  b
    """
    return a/b if not a % b else a/b + 1
    
    

def main():
    T = int(raw_input())
    for i in range(T):
        n, x, y, z, A, B = map(int, raw_input().split())
        # get the possible minimum ST time assuming no new
        # probes were built
        min_no_new_probe = ceil(A,x*n) + ceil(B,y*n)  #time for all mineral first, then gas
        for i in range(1, n):
            # i (0<=i<=n) probes for mineral,
            # n-i for gas
            mineral_time = ceil(A, x*i)
            gas_time = ceil(B,x*(n-i))
            if mineral_time > gas_time:
                temp_min_time = gas_time + ceil((A-gas_time*x*i),n)
            elif mineral_time < gas_time:
                temp_min_time = mineral_time + ceil((B-mineral_time*y*(n-i)),n)
            else:
                temp_min_time = gas_time
            if temp_min_time < min_no_new_probe:
                min_no_new_probe = temp_min_time 
        #largest number of possible new probe
        fractional_part = ceil(ceil(A % (x*n), x) + ceil(B % (y*n),y), n)
        print fractional_part
        min_serial_time = A/(x*n) + B/(y*n) + fractional_part 
        print "minimum:",min_no_new_probe 
        print "serial:", min_serial_time 
        return

if __name__ == "__main__": 
    main()
                