import re

# check if we have an audio flag
audioEnabled = True
inputFile = "Fox-in-Socks.txt"

f = open(inputFile, "r")

# initialize our json object
lines = f.readlines()

title = lines[0].rstrip("\n")
fileName = title + ".JSON"
fileName = fileName.replace(" ", "-")

output = "{\"title\": \"" + title + "\","
output += "\"audio\": "
if(audioEnabled):
    output += "true"
else:
    output += "false"
output += ", \"lines\": ["

of = open(fileName, "w")
of.write(output)


# append the rest of our json object
of = open(fileName, "a")

title = title.replace(" ", "-")

for i in range(len(lines)):
    # ignore the title when adding lines
    if(i == 0):
        continue
    #ignore lines without letters
    check = re.search('[a-zA-Z]', lines[i])
    if(check == None):
        continue
    output = ""
    output += "{ "
    output += "\"text\": \""
    output += lines[i].rstrip("\n")
    output += "\""
    if(audioEnabled):
        output += ", \"audio\": \""
        output += title + str(i) + ".wav\""

    output += "}"

    if(i != len(lines)-1):
        output += ",\n"

    of.write(output)

# close our file
output = "]}"
of.write(output)