def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    len(s)==5
    if '*'==s[3] or '*'==s[2] or '*'==s[0] or '*'==s[1] or '*'==s[4] :
        return 1
    else :
        return False

print(main('aakmkj*'))