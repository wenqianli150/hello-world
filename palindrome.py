"""
  Name: Wenqian Li
  UWNetId: wli6
  TimeComplexity = O(n)
"""
"""
       Evaluates a given string and determines whether or not it is a palindrome.
       :param the_string: The string to evaluate.
       :returns: True when the string is a palindrome, False otherwise.
"""

def is_palindrome(the_string):
    # Run loop from 0 to len/2
    the_string = the_string.replace(' ', "")
    for i in range(0, int(len(the_string) / 2)):
        if the_string[i].lower() != the_string[len(the_string) - i - 1].lower():
            return False
    return True


# main function
while True:
    s = input('Your string is: ')
    if s == 'quit':
        break
    answer = is_palindrome(s)

    if answer:
        print("Ture")
    else:
        print("False")
