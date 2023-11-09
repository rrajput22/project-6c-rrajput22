# Author: Rajvi Rajput
# GitHub username: rrajput22
# Date: 11/08/2023
# Description: Recursive function named is_subsequence that takes two string parameters and returns
# True if the first string is a subsequence of the second string, but returns False otherwise.


def is_subsequence(str1, str2):
    """
    Recursive function to check if str1 is a subsequence of str2.
    """
    # Base case to check if the first string is empty, it is always a subsequence
    if not str1:
        return True
    # Base case to check if the second string is empty and the first is not, it's not a subsequence
    elif not str2:
        return False
    else:
        # Checks if the first character of str1 matches the first character of str2
        if str1[0] == str2[0]:
            # Continue with the rest of str1 and str2
            return is_subsequence(str1[1:], str2[1:])
        else:
            # Continue with the rest of str2
            return is_subsequence(str1, str2[1:])
