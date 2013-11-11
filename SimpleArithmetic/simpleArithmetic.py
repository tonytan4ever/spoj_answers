'''
Created on January 7th, 2011

@author: tony
'''
def main():
    T = int(raw_input())
    for i in range(T):
        expression = raw_input()
        first, second, operator = None, None, None
        for i in range(0, len(expression)):
            if expression[i] == "+" or expression[i] == "-" \
                     or expression[i] == "*":
                     first, second, operator = int(expression[:i]), int(expression[i+1:]), expression[i]
        if operator == "+" or operator == "-":
            result = first + second if operator == "+" else first - second
            longest = max(len(str(first)),  len(str(second)) + 1, len(str(result)))
            horizontal_len = max(len(str(second)) + 1, len(str(result)))
            first,second = "".join([" " * (longest - len(str(first))),str(first)]), "".join([" " * (longest - len(str(second)) - 1),operator,str(second)])
            result = "".join([" " * (longest - len(str(result))), str(result)])
            print first
            print second
            print "".join([" " * (longest - horizontal_len), "-" * horizontal_len])
            print result
        elif operator == "*":
            result = first * second
            digits = len(str(second))
            tempfirst, tempsecond = first,second
            rightmost_prod = first * int(str(second)[digits - 1])
            leftmost_prod = first * int(str(second)[0])
            longest = max(len(str(first)), len(str(second)) + 1, len(str(result)))
            horizontal_len_1 = max(digits + 1, len(str(rightmost_prod)))
            horizontal_len_2 = max(len(str(leftmost_prod)) + digits - 1 , len(str(result)))
            first,second = "".join([" " * (longest - len(str(first))),str(first)]), "".join([" " * (longest - len(str(second)) - 1),operator,str(second)])
            result = "".join([" " * (longest - len(str(result))), str(result)])
            print first
            print second
            print "".join([" " * (longest - horizontal_len_1), "-" * horizontal_len_1])      
            if digits > 1:
                for i in range(0, digits):
                    multiplier = int((str(tempsecond))[digits - 1 - i])
                    tempresult = tempfirst * multiplier
                    tempresult = "".join([" " * (longest - i - len(str(tempresult))), str(tempresult)])
                    print tempresult
                print "".join([" " * (longest - horizontal_len_2), "-" * horizontal_len_2])
            print result
            
                           

if __name__ == "__main__":
    main()           