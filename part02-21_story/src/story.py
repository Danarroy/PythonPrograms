#  words = []

# while True: #while true loop to repeat until break
#     repeat = input("Please type in a word: ")
#     if repeat == "end":
#         break
#     words.append(repeat)
# print(" ".join(words))

words = []
last_word = ""

while True:
    repeat = input("Please type in a word: ")
    
    if repeat == "end":
        break
    
    if repeat == last_word:
        break
    
    words.append(repeat)
    last_word = repeat

print(" ".join(words))
