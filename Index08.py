def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    len(s)==5
    x=s.find('*')
    if x!=-1:
        x=s.index("*")
        return x
    else :
        x=False
        return x

print(main('aakm*'))