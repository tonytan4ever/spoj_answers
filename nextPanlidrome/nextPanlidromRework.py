#!/usr/bin/env python2.7
#--coding:utf-8--
 
"""
http://www.spoj.com/problems/PALIN/
"""
 
 
 
__author__="Tony Tan"
__date__="April 11, 2014"
__version__="0.1"
__email__="tonytan198211@gmail.com"
 
 
def nextPalindrome(K):
    if all(digit == '9' for digit in K):
        return int(K) + 2
    L = len(K)
    left = K[:L/2]
    center = L % 2 and K[L/2] or ""
    right = left[::-1]
    P = ''.join([left, center, right])
    if P > K:
        return P
    if center and center != '9':
        center = chr(ord(center) + 1)
        return ''.join([left, center, right])
    elif center:
        center = '0'
    left = list(left)
    digits_left = len(left)
    while digits_left:
        idx = digits_left - 1
        if left[idx] == '9':
            left[idx] = '0'
            digits_left = digits_left - 1
        else:
            left[idx] = chr(ord(left[idx]) + 1)
            break
    left = "".join(left)
    right = left[::-1]
    return ''.join([left, center, right])
 
 
def main():
    T = int(raw_input())
    for i in range(T):
        number = raw_input()
        print nextPalindrome(number) 
 
 
 
if __name__ == '__main__':
    main()