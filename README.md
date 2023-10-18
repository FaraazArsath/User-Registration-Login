GUVI - Assignment 1                                                       

# User Login Python Program
A simple Python program that allows users to register, login, and recover forgotten passwords using regular expressions for input validation.

## Features
User Registration: Allows users to create a username and password. Validates username and password based on specified criteria.

User Login: Allows existing users to log in with their username and password.

Password Recovery: Enables users to recover their password by providing their username.

## Functions
register()
Allows users to create a username. Validates the username using a regular expression for email-like formats.

passwd()
Prompts the user to create a password. Enforces criteria like at least one lowercase, one uppercase, one digit, and one special character.

forgetpassword()
Initiates the password recovery process. Prompts for a username and checks if it exists in the database.

## Regular Expressions

Username: r'^[a-zA-Z]+[\._]?[a-zA-z 0-9]+[@]\w+[.]\w{2,3}$'
Password: r"^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[!@#])"

## Note
User data is stored in a file named database.txt.










