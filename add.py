def add_little_endian(a,b,carry=0):
    """
    assumes both a and b are tuples of equal length, little endian.
    Recursive approach: add the leftmost digit and then add the digits in
    the remaining n-1 length tuples.
    """
    length = len(a)

    # Base case.  If a and b are empty, just return the carry number
    # use a list here so that it can be unpacked into the tuple
    if length == 0 :
        return [] if carry == 0 else [carry]

    # add the leftmost digits and the carry value.
    # split the digit from the carry
    digit_sum = a[0] + b[0] + carry
    digit = digit_sum % 10
    digit_carry = digit_sum // 10

    # recursive step : create a tuple with the digit and the
    # the rest of the digits added together (w/carry)
    # note the use of the unpack operator (unary *)
    return( digit, *add_little_endian( a[1:], b[1:], digit_carry ) )



def main():
    first_tuple = (4,7)
    second_tuple = (5,9)
    result = add_little_endian( first_tuple, second_tuple)
    print(f'  {first_tuple}\n+ {second_tuple}\n= {result}')

    print('\n---\n')
    first_tuple = (4,7,3,9,5,4)
    second_tuple = (5,9,6,3,7,1)
    result = add_little_endian( first_tuple, second_tuple)
    print(f'  {first_tuple}\n+ {second_tuple}\n= {result}')

if __name__ == '__main__':
    main()
