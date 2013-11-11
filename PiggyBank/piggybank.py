'''
Created on June 9th, 2011

Problem: piggy bank
SPOJ link: https://www.spoj.pl/problems/PIGBANK/

@author: tony
'''
# this is just for index purposes
VALUE,WEIGHT = 0,1

def main():
    T = int(raw_input())
    for i in range(T):
        empty,filled = map(int,raw_input().split())
        weight = filled - empty
        coin_kind = int(raw_input())
        coin_list = []
        for i in range(coin_kind):
            value,weight = map(int,raw_input().split())
            vwratio = float(value) / weight
            coin_list.append((value,weight,vwratio))
        coin_list = sorted(coin_list, key=lambda coin: coin[2])
        
            
    
if __name__ == "__main__":
    main()