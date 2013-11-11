'''
Created on Aug 9, 2010

@author: CTtan
'''
def next(Tstring):
    m = len(Tstring)
    pi = [0] * m
    k = 0; j = 1
    while j <= m-1:
        while k > 0 and Tstring[k] != Tstring[j]:
            k = pi[k - 1]
        if Tstring[k] == Tstring[j]:
            k = k + 1
        pi[j] = k
        j += 1
    return pi


while True:
    Sstring = raw_input()
    if Sstring == "":
        break
    #here, using KMP algorithm to match
    Tstring = Sstring[::-1]
    length = len(Sstring)
    i = 0; j = 0; 
    nextT = next(Tstring)
    while i <= length -1:
        while j > 0 and Tstring[j] != Sstring[i]:
            j = nextT[j-1]    
        if Tstring[j] == Sstring[i]:
            j += 1
        i += 1 
    print "after, j=>",j        
    print "".join([Sstring,Tstring[j:]])
        
