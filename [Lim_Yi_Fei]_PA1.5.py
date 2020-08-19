'''
20 + 5.5

Simple and clean code. Good use of the any keyword. Minor issue with the placement of a function within a loop.
'''

import sys

while True:
    p = input("Enter password: ")

    if p == "":
        sys.exit()
        # if there is no entry, code exits

    elif 6 <= len(p) <= 16:
        # if password fulfils the length condition, code continues

        def p_check(password):
            no_spec = p.isalnum()  # password only contains alphanumerical characters
            num = any(c.isdigit() for c in p)  # has at least 1 number
            upper = any(c.isupper() for c in p)  # has at least 1 upper case
            lower = any(c.islower() for c in p)  # has at least 1 lower case
            return no_spec and num and upper and lower

        if p_check(p) is True:
            print("Valid Password")
            # if all conditions are met, it is a valid password

        else:
            print("Invalid password")
            # if password does not fulfil the above conditions, it is an invalid password
    else:
        print("Invalid password")
        # if password does not fulfil the length condition, it is an invalid password
