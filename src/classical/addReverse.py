'''
Created on Jul 29, 2010

@author: CTtan
'''
def main():
    iterationNo = int(raw_input())
    for i in range(iterationNo):
        numbers = map(lambda x:int("".join(reversed(x))),raw_input().split())
        print int("".join(reversed(str(numbers[0]+numbers[1]))))
        
        
        
        
if __name__ == "__main__":
    main()