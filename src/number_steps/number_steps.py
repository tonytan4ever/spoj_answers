'''
Created on Jan 13, 2011

SPOJ Problem Set (classical)
1112. Number Steps
Problem code: NSTEPS

@author: tony
'''
def main():
    T = int(raw_input())
    for i in range(T):
        x,y = map(int, raw_input().split())
        if y != x and y != x-2:
            print "No Number"
        elif y == x:
            if x % 2:
                print 2*x-1
            else:
                print 2*x
        else:
            if x % 2:
                print 2*(x-2) + 1
            else:
                print 2*(x-2) + 2

if __name__ == "__main__":
    main()
            
                
            