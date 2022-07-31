import re

def register():
    file=open("C:/Users/shajjath/Desktop/Phython Course/Email Login example.txt","r")
    user_name = input("create usename :")
    user_name_condition = r'^[a-zA-z]+[\._]?[a-zA-Z 0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(user_name_condition, user_name):
        print('username validation success')
    else:
        print('username validation failed')
        register()

    def passwordreg():
        file = open("C:/Users/shajjath/Desktop/Phython Course/Email Login example.txt", "r")
        password = input("create password:")
        password_condition = r'^(?=.*?[A-z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,16}$'
        if re.search(password_condition, password):
             print('password validation success')
             file = open("C:/Users/shajjath/Desktop/Phython Course/Email Login example.txt", "a")
             file.write(user_name+" "+password+"\n")

        else:
             print('password validation failed')
             passwordreg()

    passwordreg()

def forgetpassword():
    user_name = input("Please enter your username: ")
    file= open("C:/Users/shajjath/Desktop/Phython Course/Email Login example.txt","r")
    lines=file.read()
    if user_name not in lines:
        register()
    else:
        k=[]
        v=[]
        file = open("C:/Users/shajjath/Desktop/Phython Course/Email Login example.txt", "r")
        for x in file:
            a,b=x.split()
            b=b.strip()
            k.append(a)
            v.append(b)
        data=dict(zip(k,v))
        print(data[user_name])

def home():

    option=input("Choose between Login or Registration or Forget Password: ")
    if option == "Registration":
        register()
    elif option == "Login":
        user_name = input("Please enter your username: ")
        password = input("Please enter your password: ")
        file = open("C:/Users/shajjath/Desktop/Phython Course/Email Login example.txt", "r")
        for x in file.readlines():
            login_details = x.split()
            if user_name == login_details[0] and password == login_details[1]:
                print('user login credentials already exists')
                return True
        else:
            print('user credentials not exists')
            option=input("Choose between Registration or Forget Password: ")
            if option == "Registration":
                register()
            else:
                forgetpassword()

    elif option == "Forget Password":
        forgetpassword()
    else:
        home()

home()



