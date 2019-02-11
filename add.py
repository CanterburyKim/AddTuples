def add_little_endian(a,b,carry=0):
    """
    assumes both a and b are tuples of equal length, little endian.
    Recursive approach: add the leftmost digit and then add the remaining
    n-1 length tuples.
    """
    length = len(a)

    # Base case.  If a and b are empty, just return the carry number
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


print( add_little_endian((4,7), (5,9)) )
print( add_little_endian((4,7,3,9,5,4), (5,9,6,3,7,1)) )
