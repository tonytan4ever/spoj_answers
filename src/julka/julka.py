'''
Created on Jan 12, 2011

SPOJ Problem Set (classical)
54. Julka
Problem code: JULKA

@author: tony
'''
def main():
    T = 10
    for i in range(T):
        total,diff = int(raw_input()), int(raw_input())
        natalia = (total-diff) / 2
        klaudia = natalia + diff
        print klaudia
        print natalia
    
if __name__ == "__main__":
    main()
        
