name1 = input("Please type in your name: ")

listofnephewsDonalds = ["Huey", "Dewey", "Louie"]
listofnephewsMouse = ["Morty", "Ferdie"]

if name1 in listofnephewsDonalds:
    print("I think you might be one of Donald Duck's nephews.")
elif name1 in listofnephewsMouse:
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")