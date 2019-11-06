
"""
take temp = 1
lets say no is 101 i.e 5

we need to xor 101 with 111 that we we will do a compliment
after the most biggest 1 which is most leftmost 1 temp > no
This is when we will end the process of creating this no which has all 1's

but lets say no is 4 100
first we create 111
then do 100 ^ 111 = 011

"""
def compliment(no):
    temp = 1
    while temp < no:
        temp = temp << 1
        temp = temp+1
    return no ^ temp

if __name__ == '__main__':
    no = 4
    c = compliment(no)
    print(c)