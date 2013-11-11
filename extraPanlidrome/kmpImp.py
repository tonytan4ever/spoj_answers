'''
Created on Aug 8, 2010

@author: tony
'''
def compute_prefix_function(p):
    m = len(p)
    pi = [0]*m
    k = 0
    for q in range(1,m):
        while k > 0 and p[k] != p[q]:
            k = pi[k-1]
        if p[k] == p[q]:
            k = k+1
        pi[q] = k
    return pi

if __name__ == "__main__":
    print compute_prefix_function("abaabaaab")