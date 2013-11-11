'''
Created on Jan 19, 2011

SPOJ Problem Set (classical)
12. The Game of Master-Mind
Problem code: MMIND

@author: tony
'''
def main():
    T = int(raw_input())
    for i in range(T):
        P,C,M = map(int, raw_input().split())
        for j in range(2*M):
            guess = map(int, raw_input().split())
            B,W = map(int,raw_input().split())


if __name__ == "__main__":
    pass