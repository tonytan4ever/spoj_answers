'''
Created on Jan 12nd, 2011

SPOJ Problem Set (classical)
11. Factorial
Problem code: FCTRL

note: finding trailing zeros for factorials. 
point: find how many 5 factor can this factorial provide.
algorithm: divide by 5 until result is 0 

see http://www.purplemath.com/modules/factzero.htm

@author: tony
'''
def main():
    T = int(raw_input())
    for i in range(T):
        factorial_number = int(raw_input())
        number_trailing_zero = 0
        quotient = factorial_number / 5
        while quotient > 0:
            number_trailing_zero += quotient
            quotient /= 5
        print number_trailing_zero
    

if __name__ == "__main__":
    main()