correctpassword = 4321
attempts = 0

while True:
    enterpassword = int(input("PIN: "))
    attempts += 1
    if enterpassword == correctpassword:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
        else:
            print("Correct! It took you " + str(attempts) + " attempts")
        break
    else:
        print("Wrong")

#everyting uner while true will repeat until break is reached
#attempts += 1 adds one to attempts each time the loop repeats
# if enterpassword == correctpassword checks if the entered password is correct
# if attempts == 1 checks if it took only one attempt
