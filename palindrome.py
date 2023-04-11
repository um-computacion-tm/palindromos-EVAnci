def check_palindrome(s):
    # Ignore spaces in the string 
    s = s.lower()
    s_no_spaces = ''
    for i in s:
        if i != ' ':
            s_no_spaces += i

    # if the string len is 1 or 0 will be a palindrome
    if len(s) == 1 or len(s) == 0:
        return True
    else:
        # So if the string first char is equal to the last char, this will be
        # calling the function check_palindrome for the string without the 
        # first and the last character.
        # If the first char and the last char are different then return false. 
        if s[0] != s[-1]:
            return False
        else:
            return check_palindrome(s[1:-1])