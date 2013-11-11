'''
Created on Aug 7, 2010

@author: tony
'''
def main():
    T = int(raw_input())
    for i in range(T):
        number = int(raw_input())
        #print "Here"
        possiblePanlidrome = number + 1
        while True:
            possiblePanlidrome = possiblePanlidrome + 1
            #print possiblePanlidrome
            reverse = str(possiblePanlidrome)[::-1]
            if  reverse == str(possiblePanlidrome):
                print reverse 
                break
            
if __name__ == "__main__":
    main()
            