'''
Created on Jan 12, 2011

SPOJ Problem Set (classical)
302. Count on Cantor
Problem code: CANTON

algorithm: http://galaas.blogbus.com/logs/73106344.html

@author: tony
'''
def main():
    T = int(raw_input())
    for i in range(T):
        term_no = int(raw_input())
        import math
        #possible: where pth line where term_no'th number will reside
        possible = int(math.sqrt(2.0*term_no))
        while possible*(possible+1) >= 2*term_no:
            possible -= 1
        sum = possible*(possible+1)/2
        # depending possible's odd/even, have to calculate
        # up/down differently
        # rationale: different directions. 
        if possible % 2:
            up = term_no - sum;
            down = possible + 2 - up
        else:
            down = term_no-sum;
            up = possible + 2 - down
        print "TERM %d IS %d/%d" % (term_no, up, down)
            
            
        


if __name__ == "__main__":
    main()
