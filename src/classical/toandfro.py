'''
Created on Jul 29, 2010

@author: CTtan
'''
def main():
    import sys
    colNo = int(raw_input())
    while colNo:
        message = raw_input()
        adjustedMessage = ""
        for row in range(len(message)/colNo):
            #print message[row*colNo:(row+1)*colNo]
            if row %2 == 0:
                adjustedMessage = "".join([adjustedMessage,message[row*colNo:(row+1)*colNo]])
            else:
                adjustedMessage = "".join([adjustedMessage,"".join(reversed(message[row*colNo:(row+1)*colNo]))])
        for i in range(0,colNo):
            for offset in range(len(message)/colNo):
                #print offset*colNo
                sys.stdout.write(adjustedMessage[i+offset*colNo])
        sys.stdout.write("\n")
        colNo = int(raw_input())        


if __name__ == "__main__":
    main()