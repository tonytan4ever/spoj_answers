'''
Created on Jul 29, 2010

@author: CTtan
'''
def main():
    while True:
        inputNumber = int(raw_input())
        if inputNumber != 42:
            print inputNumber
        else:
            break
        
        

if __name__ == "__main__":
    main()