'''
Created on January 11th, 2011

SPOJ 8 - Complete the Sequence![CMPLS]
solved by n-1'th degree differences
see: http://rchardx.is-programmer.com/posts/16142.html

@author: tony
'''
def main():
    T = int(raw_input())
    for i in range(T):
        n,m = map(int, raw_input().split())
        array = []
        array.append(map(int,raw_input().split()))
        #compute n-1't difference
        for i in range(1,n):
            array.append([])
            for j in range(0, n-i):
                array[i].append(array[i-1][j+1]-array[i-1][j])
        #add m last difference to the last row of difference
        #rationale: we need compute next m numbers in the sequence
        for i in range(1,m+1):
            array[n-1].append(array[n-1][0])
        #fill each difference row with m more values
        #rationale: same as last one
        for i in range(n-2,-1,-1):
            for j in range(0,m):
                array[i].append(array[i][n-i+j-1]+array[i+1][n-i+j-1])
        for i in range(0, m-1):
            print array[0][n+i],
        print array[0][n+m-1]
        
if __name__ == "__main__":
    main()
        