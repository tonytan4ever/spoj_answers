'''
Created on Aug 8, 2010

@author: tony
'''
from sys import stdin,stdout
def main():
    while True:
        stringList = stdin.readline()[:-1]
        length = len(stringList)
        if length == 0:
            break
        reversed = -1
        match = False
        for index in range(length):
            tempIndex = index
            while stringList[tempIndex] == stringList[reversed]:
                tempIndex += 1
                reversed -= 1
                if tempIndex == length:        
                    match = True
                    break
            else:
                reversed = -1
                continue
            if match:
                break
        extend = stringList[:reversed+1][::-1]    
        stdout.write(stringList)
        stdout.write(extend)
        stdout.write("\n")
        
if __name__== "__main__":
    main()
            
            
