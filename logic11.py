def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x=a>100 and a<1000
    return x
print(main(12))
print(main(3))