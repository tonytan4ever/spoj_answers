'''
Created on Jan 12, 2011

SPOJ Problem Set (classical)
4. Transform the Expression
Problem code: ONP

@author: tony
'''
def main():
    T = int(raw_input())
    operator = dict(zip(('+','-','*','/','^','('),
                            (1,2,3,4,5,6)))
    for i in range(T):
        exp = raw_input()
        # here, add an extra '(' to the stack acting as '$'
        stack = ['(']
        result = []
        priority = 6
        for ch in exp:
            if ch.isalpha():
                result.append(ch)
                continue
            if ch == '(':
                stack.append(ch)
                priority = 6
                continue
            if ch in operator.keys():
                if operator[ch] > priority:
                    result.append(ch)
                else:
                    stack.append(ch)
                    priority = operator[ch]
                continue
            if ch == ')':
                retr = stack.pop()
                while retr != '(':
                    result.append(retr)
                    retr = stack.pop()
                priority = operator[stack[-1]]
        print "".join(result)
            
if __name__ == "__main__":
    main()