for i in range(3):
    username = "atif"
    password = "1234"
    usr = input("Enter your username: ")
    pwd = input("Enter your password: ")
    if usr == username and pwd == password:
        print ("Login Successfull!")
        break
    elif usr == username and pwd != password:
        print("Invlalid Password!!")
        print("Attempts Remaining: ", 3-(i+1))
    else:
        print("Invalid Credentials")
        print("Attempts Remaining: ", 3-(i+1))

    