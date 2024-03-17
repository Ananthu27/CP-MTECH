# if number & (2**k-1) = 0 then the number is divisible by 2**k
def odd(num):
    return (num & 1)

def bitwise_not(num):
    return -num-1

def power_of_two(num):
    return not (num & (num-1))

def int_to_binary(num):
    for i in range(16,0-1,-1):
        if (1<<i)&num : print('1',end='')
        else : print('0',end='')
    print()

def application(num,k):

    # set the k'th bit
    temp = num | (1<<k)
    int_to_binary(num)
    int_to_binary(temp)
    print()

    # unset the k'th bit
    temp = num & ~(1<<k)
    int_to_binary(num)
    int_to_binary(temp)
    print()

    # invert the k'th bit
    temp = num ^ (1<<k)
    int_to_binary(num)
    int_to_binary(temp)
    print()

    #############
    
    # unset the first set bit from right to 1
    temp = num & (num-1)
    int_to_binary(num)
    int_to_binary(temp)
    print()
    
    # unset all the set bits except first set bit from right
    temp = num & -num
    int_to_binary(num)
    int_to_binary(temp)
    print()
    
    # make the bits to the left of first set bit from right to 1
    temp = num | (num-1)
    int_to_binary(num)
    int_to_binary(temp)
    print()

application(2**10+2**3,3)