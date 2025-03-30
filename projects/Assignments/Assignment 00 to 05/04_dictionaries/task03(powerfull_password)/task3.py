import hashlib

print("03 Powerfull Password")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

store_logins:dict={
    "abc123@gmail.com":hash_password("123asd@#$"),
    "youtube123@gmail.com":hash_password("43ahdsd@#$"),
    "malik123@gmail.com":hash_password("6253asd@#$"),
}

def login(email,password):
    if email in store_logins:
        return store_logins[email] == hash_password(password)
    return False

def main():
    email:str=input("Enter your email: ")
    password:str=input("Enter your password: ")

    if login(email,password):
        print("Login Successful! ")
    else:
        print("Invalid email or password. ")

if __name__ == "__main__":
    main()
        