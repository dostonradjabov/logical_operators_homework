def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    x = a>10000 and a<100000
    return x
print(main(15234))
print(main(763))