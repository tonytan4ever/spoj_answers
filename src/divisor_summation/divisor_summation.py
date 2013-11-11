'''
Created on Jan 12, 2011

SPOJ Problem Set (classical)
74. Divisor Summation
Problem code: DIVSUM

@author: tony
'''
def main():
    summation_list = [0]*500000
    for i in range(500000):
        p = i+1
        for j in range (2*p,500000+1,p):
            summation_list[j-1] += p
    #print summation_list
    T = int(raw_input())
    for i in range(T):
        n = int(raw_input())
        print summation_list[n-1]

if __name__ == "__main__":
    main()