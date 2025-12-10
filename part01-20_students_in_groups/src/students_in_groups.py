numberofstudents = int(input("How many students on the course? "))
numberofgroups = int(input("Desired group size? "))

if numberofstudents % numberofgroups == 0:
    print(f"Number of groups formed: {numberofstudents // numberofgroups}")
else:
    print(f"Number of groups formed: {numberofstudents // numberofgroups + 1}")