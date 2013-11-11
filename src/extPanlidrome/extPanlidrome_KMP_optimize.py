'''
Created on Aug 9, 2010

@author: CTtan
'''
def nextTable(Tstring):
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
    length = len(Sstring)
    i = 0; j = -1;
    #this, definitely need optimize 
    nextT = nextTable(Sstring[::-1])
    #*******************************
    #nextT = {}
    #
    #*******************************
    while i <= length -1:
        while j < -1  and Sstring[j] != Sstring[i]:
            j = -(nextT[-(j+2)])-1    
        if Sstring[j] == Sstring[i]:
            j -= 1
        i += 1
    print "after, j=> ",j         
    print "".join([Sstring,Sstring[j::-1]])
        
