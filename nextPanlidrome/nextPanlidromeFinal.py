'''
Created on Aug 8, 2010

@author: tony
'''
def toDigits(n, b=10):
    # Yeah, I could just use str() to get them, but I'm sure someone will bitch
    # that I had to use actual math
    digits = []
    while n > 0:
        digits.append(n % b)
        # Integer division in Python 3 (actually >= 2.5)
        n //= b
    # Actually returns digits in reversed order so index in array corresponds
    # to base power
    return digits
       
def fromDigits(digits, b=10):
    return sum(b**i * ai for i, ai in enumerate(digits))

       
def nextPalindrome(n, b=10):
    digits = toDigits(n, b)
    nd = len(digits)
    half = nd//2
    A = digits[nd-half:]
    B = list(reversed(A))
    C = digits[:half]
    nA, nB, nC = map(lambda x: fromDigits(x, b), (A, B, C))
    print nA, nB, nC
    if nB > nC:
        # Not >= because if given a palindrome, we want the next one
        digits[:half] = B
    else:
        if nd % 2 == 0:
            nA += 1
        elif digits[half] == b-1:            
            digits[half] = 0
            nA += 1
        else:
            digits[half] += 1
        A = toDigits(nA)
        B = list(reversed(A))
        digits[nd-half:] = A
        digits[:half] = B
    return fromDigits(digits, b)


def main():
    T = int(raw_input())
    for i in range(T):
        number = int(raw_input())
        print nextPalindrome(number) 


if __name__ == "__main__":
    main()


