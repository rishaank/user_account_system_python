Username = input ("Create a User> ")
Password = input ("Type in a secure password> ")
Verify = input ("Type in your password again> ")
if Verify != Password:
    print ("Error: you failed the password verification test")
    quit()
elif Verify == Password:
    print ("A new user was succsesfully created, going into command mode...\nCommand mode\n__________\n\nType Q to Quit (case sensitive)\nType L to Log-in (case sensitive)\n")
while 3>1:
    latest_command = input (">")
    if latest_command == "Q":
        print("Exitting...\n")
    elif latest_command == "L":
        Login = input("Type in the Username of an existing user> ")
        if Username == Login:
            Loginpass = input ("Type in the Username of an existing user's password> ")
            if Loginpass == Password:
                print ("Hello", Username)
            elif Loginpass != Password:
                print ("Error: wrong password\n")
                quit()