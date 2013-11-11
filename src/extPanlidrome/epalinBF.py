'''
Created on Aug 8, 2010

@author: tony
'''
def main():
    T = int(raw_input())
    for i in range(T):
        stringList = list(raw_input())
        length = len(stringList)
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
            if match:
                break
            else:
                reversed = -1
        exList = []
        while index > 0:
            exList.append(stringList[reversed])
            reversed -= 1
            index -= 1
        stringList.extend(exList)
        print "".join(stringList)
        
if __name__== "__main__":
    main()
            
            
