password = input("Password: ")

while True: #while true loop to repeat until break
    repeat = input("Repeat password: ")
    if repeat == password:
        print("User account created!")
        break
    else:
        print("They do not match!")
