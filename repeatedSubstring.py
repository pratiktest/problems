def bruteforce():
    input = 'ababab'

    halfLength = int(len(input) / 2)
    fullLength = int(len(input))
    print(str(halfLength))
    """
        just iterate halflength+1.. string with more than halflength cannot be multiplied to whole string
        halflength+1 since we are 0 indexed so we need to go 1 more
    """
    for i in range(1, halfLength + 1):
        """ only then we can multiply and construct the whole string 5%1 ==0 but 5%2 != 0 so we cannot construct
            length of string 5 with length of subsrtring 2"""
        if fullLength % i == 0:
            """ 
                first we start just first char i=1..substr[0:1] is just character a
                for this character the length we need to repeat to get entire string is 6/1 = 6
                aaaaaa != ababab
                so we move on

                then i=2
                substr[0:2] is ab and we will need to do length/2(6/2) 3 times times to get the whole string
                ababab..we get the string return true

                WE NEED TO MULTIPLY SUBSTR len(SUBSTR)/i times
                eg a*8
                eg ab*4
                eg abab*2
                6 + 3 + 2
                11
            """
            substr = input[0:i]
            timesToMultiply = int(fullLength / i)
            s = ""
            for j in range(0, timesToMultiply):
                s = s + substr
            print(s)
            if s == input:
                print(True)

def ordern():
    input = "ababab"
    """
        valid input is ababab
        input + input = abababababab
        if we consider input + input without first char bababababab...ababab is a substring of this 
        so the idea is
        
        STRING IS MADE OF REPEATED STRINGS ONLY IF IT IS A NON TRIVIAL ROTATION OF ITSELF
        
        A is rotation of B if A is substring of BB
        paci rotate by 2 ->  cipa
        pacipaci  if you see cipa is in between as paci and cipa are rotations
        
        abcd abcd 
        abcdabcd abcdabcd
        ofcourse abcd abcd will be a substring
        but even if we remove a
        bcdabcd abcdabcd
        
        as string is rotation of itself we will get this string in between
        think of this as removing a and putting it at the end
        
        If there is no repetition then 
        pqrbc
        
        pqrbcpqrbc + rotate by 1 -> qrbcpqrbcp
        pqrbc is a substr but starts from the other end and is not in middle or before len(pqrbc)
    
        
        
        
    """
    index = (input+input).find(input,1)
    print (index != len(input))




if __name__ == '__main__':
    bruteforce()
    ordern()


