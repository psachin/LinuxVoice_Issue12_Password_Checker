import easygui as eg

def pword():
    global password
    global lower
    global upper
    global integer
    password = eg.passwordbox(msg="Please enter your password")
    length = len(password)
    print(length)
    lower = sum([int(c.islower()) for c in password])
    print(lower)
    upper = sum([int(c.isupper()) for c in password])
    print(upper)
    integer = sum([int(c.isdigit()) for c in password])
    print(integer)


def length():
    global password
    if len(password) < 6:
        eg.msgbox(msg="Your password is too short, please try again")
    elif len(password) > 12:
        eg.msgbox(msg="Your password is too long, please try again")

def strength():
    global lower
    global upper
    global integer
    if (lower) < 1:
        eg.msgbox(msg="Please use a mixed case password with lower case letters")
    elif (upper) < 1:
        eg.msgbox(msg="Please use a mixed case password with UPPER case letters")
    elif (integer) < 1:
        eg.msgbox(msg="Please try adding a number")
    else:
        eg.msgbox(msg="Strength Assessed - Your password is ok")

while True:
    pword()
    length()
    strength()
    answer = eg.ynbox(title="Try again?",
                      msg="Would you like to try again?")
    if answer is False:
        break


