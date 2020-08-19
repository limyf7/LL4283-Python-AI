'''
10 + 5.5

Good attempt at using try-except to perform entry validation. Use of zip is commendable, although the result can be more directly stored as a nested list instead of having to zip the outputs.
Script was well commented. Split (and rsplit) come with "maxsplit" keyword arguments, which allow controlling how many times a string is split.
The use of sys is technically superfluous, since simple Python scripts will automatically exit, but no credit nor demerit was given for this.

'''

import sys

email_list = []

# components of an email address user@server.tld
user = []
server = []
tld = []

output = []

while True:
    email = input("Enter email address: ")

    if email != "Quit":
        try:
            email_list.append(email)

            # extract user from email address
            user.append(email.split("@")[0])

            domain = email.split("@")[1]
            # extract server from email address
            server.append(".".join(domain.split(".")[:-1]))

            # extract top-level domain from email address
            tld.append(domain.split(".")[-1])

        except IndexError:
            # loop continues if entry does not satisfy email address format
            continue

    else:
        # when Quit is entered, combine and print analysis result for each email, then quit code
        output = list(zip(email_list, user, server, tld))

        for r in output:
            print("{}, {}, {}, {}".format(*r))

        sys.exit()

'''
Explaining name: isolate characters before "@" in a list called "user"
    email.split("@")[0]   splits email by @, and takes the first element
    adds the result to the list "user"

Explaining server: isolate characters after "@" and before the last "." in a list called "server"
    email.split("@")[1]   splits email by @, and takes the second element
    .split(".")[:-1]      splits the second element by ".", and takes all the elements except the last element
    ".".join()            joins the elements with ".", if there is more than one element
    adds the result to the list "server"

Explaining tld: isolate the characters after the last "." in a list called "tld"
    email.split("@")[1]   splits email by @, and takes the second element
    .split(".")[-1]       splits the second element by ".", and takes the last element
    adds the result to the list "tld"

'''

# Prof's method

'''
emailDB = []

while True: 
  emailAddress = input("Enter email address:")

  if emailAddress != "Quit":
    atPos = emailAddress.find("a")
    dotPos = emailAddress.rfind(".")

    username = emailAddress[:atPos]
    server = emailAddress[atPos+1:dotPos]
    tld = emailAddress[dotPos+1:]

    emailDB.append([emailAddress, username, server, tld])

  else:
    for emailEntry in emailDB:
      print("{}, {}, {}, {}".format(*emailEntry))
    break
'''