'''
Created on Aug 7, 2010

@author: tony
'''
def main():
    T = int(raw_input())
    for i in range(T):
        numberList = list(raw_input())
        length = len(numberList)
        middle = (length >> 1)
        changePair = [middle,middle]
        checkPair = changePair[:]
        #mirror
        extending = numberList[:middle]
        extending.reverse()
        if length & 1 == 0:
            changePair[0] -= 1 
            checkPair[0] -= 1
        else:
            extending.insert(0,numberList[middle])
        while checkPair[0] >=0:
            if numberList[checkPair[0]] > numberList[checkPair[1]]:
                needIncre = False
                break
            elif numberList[checkPair[0]] < numberList[checkPair[1]]:
                needIncre = True
                break
            else:
                checkPair[0] -= 1
                checkPair[1] += 1
                continue
        else:
            needIncre = True    
        #attach mirrored part
        numberList = numberList[:middle]
        numberList.extend(extending)
        #increase changePair's number, if necessary
        if (needIncre):
            if numberList[changePair[0]] != "9":
                char = numberList[changePair[0]]
                numberList[changePair[0]] = chr(ord(char)+1)
                numberList[changePair[1]] = chr(ord(char)+1)
            else:
                while (numberList[changePair[0]] == "9"):
                    numberList[changePair[0]] = "0"
                    numberList[changePair[1]] = "0"
                    changePair[0] -= 1
                    changePair[1] += 1
                    if changePair[0] == -1:
                        numberList.append("0")
                        changePair[0] = 0
                        changePair[1] = -1
                char = numberList[changePair[0]]
                numberList[changePair[0]] = chr(ord(char)+1)
                numberList[changePair[1]] = chr(ord(char)+1)
        print "".join(numberList)
                    
                
            
                
            
        
                
                
            
        
            
if __name__ == "__main__":
    main()
        