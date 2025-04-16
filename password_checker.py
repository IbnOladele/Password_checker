password = input("insert password: ")

#length checker
def password_length(password):
    if len(password) < 8:
        print("password is too short, try again!")
password_length(password)

def has_uppercase(password):
    if not any(char.isupper() for char in password):
        print("password is weak, must contain at least one uppercase letter")
has_uppercase(password)

def has_digit(password):
    if not any(char in "!@#$%^&*()-_+=<>?{}[]|:;\"'`~" for char in password):
        print("password is weak, must contain at least one special character")
    if not any(char.isdigit() for char in password):
        print("password is weak, must contain at least one number")
has_digit(password)
print(password)