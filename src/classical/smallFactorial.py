'''
Created on Jul 30, 2010

@author: CTtan
'''
def factorial(n):
    if n == 1:return 1
    else: return n*factorial(n-1)

def main():
    iterationNo = int(raw_input())
    for i in range(iterationNo):
        number = int(raw_input())
        print factorial(number) 
    
    
    
if __name__ == "__main__":
     main() 