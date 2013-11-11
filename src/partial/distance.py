"""
#Consider a sequence D consisting of an infinite number of hexadecimal digits 
#made by concatenating all the positive integers 1, 2, 3, 4,..., N,...
#The sequence D begins with:

#123456789ABCDEF101112131415161718191A1B1C1D1E1F202122...

#We may see D as an infinite string of hexadecimal digits. 
#Let S be an arbitrary string consisting only of hexadecimal digits. 
#The number of occurrences of S in D as a substring is infinite. The distance between two nonoverlapping 
#occurrence of S is the number of digits between these two occurrences. 
#For instance, if S='21', the distance between the first two occurrences of S is 27 (as illustrated above). 
#Task You are given a string S of at most 30 characters long. 
#Write a program that determines the distance between the first two occurrences of S in D.
#Input
#The input contains the string S in a single line. 

#Output
#The output contains the distance between the first two occurrences of S in D in a single line. 

#Example
#Input
#21
#Output
#27

#Input
#A
#Output
#26

Created on Jul 29, 2010
@author: CTtan
"""

def distanceFind(inputString):
    infiniteHex = ""
    hexNumber = 1
    #a flag for find first appearance 
    findFirst = False
    while True:
        infiniteHex = "".join([infiniteHex,("%x"%hexNumber).upper()])
        if infiniteHex.find(inputString) != -1: 
            if not findFirst:
                findFirst = True
                #clear previous string, for saving memory
                infiniteHex = ""
            #find the secondA appeareance
            else:
                return len(infiniteHex)-1
        #yield infiniteHex
        hexNumber += 1
        
        

if __name__ == "__main__":
    inputString = raw_input()
    print distanceFind(inputString)
        