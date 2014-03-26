'''
Created on March 26th, 2014

SPOJ Problem Set (arrays)
17104. Fun with Sequences (Act 3)
Problem code: SMPSEQ5

@author: tony
'''
import sys

def main():
    s_length = int(raw_input())
    s = map(int, raw_input().split())
    q_length = int(raw_input())
    q = map(int, raw_input().split())
    index_range = s_length if s_length <= q_length else q_length
    first = True
    for i in xrange(index_range):
        if s[i] == q[i]:
            if first:
                sys.stdout.write(str(i+1))
                first = False
            else:
                sys.stdout.write(" "+str(i+1))
        

if __name__ == "__main__":
    main()