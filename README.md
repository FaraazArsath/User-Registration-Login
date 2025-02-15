# User Authentication System in Python
A simple Python program for user registration, login, and password recovery, utilizing regular expressions for input validation.

## 🚀 Features
User Registration: Allows users to create a username and password, ensuring they meet predefined validation criteria.

User Login: Enables existing users to log in securely using stored credentials.

Password Recovery: Provides users with an option to recover their password by verifying their username.
## 🔧 Functions
register() → Creates a new user account. Validates the username using a regular expression to ensure an email-like format.

passwd() → Prompts users to set a password, enforcing strong password rules (uppercase, lowercase, digit, and special character).

forgetpassword() → Initiates the password recovery process by verifying the provided username.
## 🛠 Regular Expressions
Username Validation:

r'^[a-zA-Z]+[._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

Password Validation:

r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#])"

## 📂 Note
User data is securely stored in a file named database.txt.
