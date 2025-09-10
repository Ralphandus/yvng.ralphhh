import re

while True:
    username = input("Please eter your username: ")
    pattern = r"^[a-zA-Z0-9]*_[0_9]*#"
    if re.match(pattern, username):
        while True
            password = input("Please enter your password: ")
            pattern2 = r"^[a-zA-Z0-9@#$%^&+=._]"
            if re.match(pattern2, password): and len(password) >= 8:
                print("Username and password are valid.")
            break
        else:
            print("Invalid password format. Please try again.")
    break
else:
    print("Invalid username format. Please try again.")
    
 
           
            
                