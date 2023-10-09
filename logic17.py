def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a%100000<((a//10000)%10<(a//1000)%10<(a//100)%10<a%10)
    return x
print(main(75421))