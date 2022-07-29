import re
file = open("filename.txt")
record = file.read()
login = input("Enter the username to login : ")
if(login in record):
    print("User Credentials exits")
else:
    print("Entered user credentials does not exists ")
    ask_user=int(input("choose 1 to go for 'Registration' or 2 for 'Forgotpassword': "))
    
    if (ask_user==1):
        user_name = input('enter the username to register: ')
        user_name_condition = r'^[a-zA-z]+[\._]?[a-zA-Z 0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(user_name_condition, user_name):
            print('username validation success')
            file=open("filename.txt","a")
            file.write(user_name)
            file.close()
        else:
            print('username validation failed')
    elif (ask_user==2):
        password = input('enter the password to validate: ')
        password_condition = r'^(?=.*?[A-z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,16}$'
        if re.search(password_condition, password):
            print('password validation success')
            file=open("filename.txt","a")
            file.write(password)
            file.close()
        else:
            print('password validation failed')

    else:
          print




