# Madlibs generator; user is asked to enter words that are then put into a story, stored in a text file, because that is more interesting and dynamic.

import string, os

# Custom punctuation set excluding ">"
custom_punctuation = set(string.punctuation) - {">"}

with open("story.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

storylist = []
previous = []
for line in lines:
    words = line.split()
    for word in words:
        # Check if the last character is punctuation (and not ">")
        if word[-1] in custom_punctuation:
            entry = [word[:-1], word[-1]]
        else:
            entry = [word, ""]

        if entry[0][0] == "<" and entry[0][len(entry[0])-1] == ">":
            done = False
            for thing in previous:
                if thing[0] == entry[0]: 
                    entry[0] = thing[1]
                    done = True
            
            if not done:
                inp = input(f"Enter a {entry[0][1:-1]}:   ")
                os.system('cls')
                previous.append([entry[0], inp])
                entry[0] = inp



        storylist.append(entry)

for i in range(0, len(storylist)):
    storylist[i] = "".join(storylist[i])

print("\n" * 3)
print(" ".join(storylist))
print("\n" * 3)


