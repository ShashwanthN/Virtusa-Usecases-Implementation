
bannedWords = ["bad", "toxic", "hate", "hello"]

def mask(Text):
    result = Text
    for word in bannedWords:
        result = result.replace(word, "*********")
    return result

def hasBannedWords(Text):
    for word in bannedWords:
        if word in Text.lower():
            return True
    return False

def getAndSaveLinks(Text, linkList):
    for word in Text.split():
        if word.startswith("http"):
            linkList.append(word)
    f = open("links.txt", "w")
    for link in linkList:
        f.write(link + "\n")
    f.close()
    return linkList
posts = [
    "User1: hi im bad and i will post toxic things",
    "User2: i made a website https://html.com",
    "User3: i think someone is going to do something bad but I like this platform",
    "User4: im really really bad and im gonna do something bad",
    "User5: go to https://www.rmkec.ac.in/2023/ for addmission"
]
total = 0
cleaned=0
blocked=0

links = []
userFlag = {}
for post in posts:
    total =total+1
    username = post.split(": ")[0]
    Text = post.split(": ")[1]
    if username not in userFlag:
        userFlag[username] = 0
    cleanedText= mask(Text)
    if hasBannedWords(Text):
        userFlag[username] = userFlag[username] + 1
        blocked = blocked + 1
        print("BLOCKED: " + username + ": " + cleanedText)
    else:
        cleaned= cleaned+ 1
        print("CLEAN: " +username + ": "+ cleanedText)
    links = getAndSaveLinks(Text,links)

print("Total Posts filter: " + str(total) + " | Cleaned: " + str(cleaned) + " | Blocked: " + str(blocked))
print(userFlag)

