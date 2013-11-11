'''
Created on Jan 13, 2011

SPOJ Problem Set (classical)
25. Pouring water
Problem code: POUR1

@author: tony
'''
def gcd(a,b):
    return a if not b else gcd(b,a%b)

def check(a,b,c):
    """
    fill in a first, then pour it in b
    """
    ret,ca,cb = 0,0,0
    while True:
        if ca == c or cb == c:
            #print ret
            return ret
        #if b is full, empty b
        if cb == b : cb = 0
        #if a is empty, fill in a
        elif ca == 0 : ca = a
        else:
            dt = min(b-cb,ca)
            #print "set_trace:"
            #print "ca:",ca,"cb:",cb,"dt:",dt
            ca -= dt; cb += dt
            #print "ca:",ca,"cb:",cb
        ret += 1

def main():
    T = int(raw_input())
    for i in range(T):
        a = int(raw_input())
        b = int(raw_input())
        c = int(raw_input())
        d = gcd(a,b)
        if c%d or (c>a and c>b): print -1
        else: print min(check(a,b,c), check(b,a,c))

if __name__ == "__main__":
    main()