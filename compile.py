#Files that need to be in the directory named "lists" (removed .txt suffix):
# abuse
# ads
# adservers
# CoinMiner
# crypto
# domainlist
# drugs
# fraud
# hosts
# justdomains
# list
# list_browser
# list_optional
# malware
# nrop (p*rn)
# phishing
# piracy
# ransomware
# redirect
# scam
# tracking
# UKCommBlocks


#Basic coding convention notes from the coder.
# inp: inp is a variable that i use in menus. either yes/no menus or a list 1/2/3/4... menu
# item: item is a variable in for arrays that I use to get items from an array. i dont use this in for range loops.
# line: refer to item

#######START CODE#######
#######START CODE#######
#######START CODE#######
print("Installing dependencies. Give us a minute.")
import os
os.system("pip install tqdm math")
from tqdm import tqdm

def roundDecimalUp(number:float, decimals:int=0): #this will be used for the smart file formatting
    import math
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.ceil(number)

    factor = 10 ** decimals
    return math.ceil(number * factor) / factor

files = ["lists/abuse", "lists/ads", "lists/adservers", "lists/CoinMiner", "lists/crypto", "lists/domainlist", "lists/drugs", "lists/fraud", "lists/hosts", "lists/justdomains", 
        "lists/list", "lists/list_browser", "lists/list_optional", "lists/malware", "lists/nrop", "lists/phishing", "lists/piracy", "lists/ransomware", "lists/redirect", 
        "lists/scam", "lists/tracking", "lists/UKCommBlocks"] #array of file names. to be used on the loop to get file contents

contents = ""

print("Would you like to add any files to the current\narray? The current array consists of:")
for item in files:
    print(item, end= ",")
    if item == "list_browser":
        print()
inp = input("y/N> ")
if inp.lower() == "y" or inp.lower == "yes":
    looping = True
    while looping:
        inp = input("What is the name of the file (without .txt) that you\nwould like to add to the array? Type e to exit this menu.\n> ")
        if inp == "e":
            looping = False
        else:
            files.append(inp)
else:
    print("Alright, sticking to the current file array.")

for item in files:
    fileName = item + ".txt"
    print("Opened: ", fileName)
    f = open(fileName, "r")
    contents = contents + f.read()
    print("Written", fileName, "to the memory array. Do not exit yet, we still need to get the other entries and save!")
    f.close()
    contents = contents + "\n"

#Asking for user pref. Keep or remove # lines.

listOfContents = contents.split("\n")


print("\n\n\nWe have managed to gather domains. However, there is a possibility that some lines\nare comment lines. This means that the line contains\neither a # to comment out an entry, or to note that an entry was added.\n\nWould you like to see these entries to decide wether\nyou would like to keep or remove them?")
inp = input("y/N> ")
if inp.lower() == "y" or inp.lower() == "yes":
    autoNo = False
    callThis = True
    print("Ok, let me do some magic work behind the scenes to get this set up for you.")
    lenList = len(listOfContents)

    rememberRemove = []
    for i in tqdm (range (lenList-2), desc="Searching..."):
        line = listOfContents[i]
        if "#" in list(line):
            if autoNo == True:
                callThis = False
                rememberRemove.append(line)
            if callThis == True:
                print("Keep this line:\n" + line)
                inp = input("Y/n/an(auto-no) >")
                if inp.lower() == "n" or inp.lower() == "no":
                    print("Ok, removing this line from your array.")
                    rememberRemove.append(line)
                elif inp.lower() == "an" or inp.lower() == "auto no" or inp.lower() == "auto-no" or inp.lower() == "autono":
                    autoNo = True
                    print("Automatically removing all comment lines.")
                    rememberRemove.append(line)
                else:
                    print("Ok, keeping this line.")

    lenRemember = len(rememberRemove)
    
    for i in tqdm (range (lenRemember), desc="Removing..."):
        item=rememberRemove[i]
        listOfContents.remove(item)

print("As well as comment lines, there may be invalid lines\nInvalid lines may look like this:\nwww.example.com Issue 69\n\nThis line could either cause a crash in your pi-hole or other DNS\nfilter, or could simply just not be recognised and wouldn't work\nYou have 3 choices per each line. You can either:\n1) Change\n2) Keep\n3) Edit\nThe search function looks for lines with spaces in.\nWould you like to view these lines that may possibly cause errors?")
inp = input("y/N")

if inp.lower() == "y" or inp.lower() == "yes":
    print("Ok, let me do some magic work behind the scenes to get this set up for you.")
    lenList = len(listOfContents)

    rememberRemove = []
    for i in tqdm (range (lenList-2), desc="Searching..."):
        line = listOfContents[i]
        if " " in list(line):
            print("Keep this line:\n" + line)
            inp = input("y/n/E >")
            if inp.lower() == "n" or inp.lower() == "no":
                print("Ok, removing this line from your array.")
                rememberRemove.append(line)
            elif inp.lower() == "y" or inp.lower() == "yes":
                print("Ok, keeping this line.")
            else:
                whatToHave = input("Modify\n> ")
                listOfContents[i] = whatToHave

    lenRemember = len(rememberRemove)
    
    for i in tqdm (range (lenRemember), desc="Removing..."):
        item=rememberRemove[i]
        listOfContents.remove(item)

print("Your list may be all over the place. Do you want us to\nsort the list for you?")
inp = input("Y/n> ")
if inp.lower() == "n" or inp.lower() == "no":
    print("Alright, we wont sort your list. :)")
else:
    print("Sorting list now. :)")
    listOfContents = sorted(listOfContents)
    print("Sorted list!")

print("\n\n\n\n\n\n\n\n\nNow comes the fun part! Saving your file. Here are\nsome statistics while you wait:\nDomains gathered: ", len(listOfContents),"\nTotal domains in the world: ~359800000\nTotal TLD(Top Level Domain) extentions available: 1517\nNumber of .com domains: 1300000")
contents = ""
print("Starting file formatting.  Give us a minute.")

lenList = len(listOfContents)

#Save into multiple files, then merge those files. Saves memory and speeds up code. We see a throttle start
#at roughly 200k domains, so we will split per 200k domains and then save those into seperate files, then merge
#them together

totalToSplit = lenList / 200000
if totalToSplit < 1:
    print("Your list is under 200k. This means you should be able to\nsave the list straight to the file.")
    for i in tqdm (range( lenList), desc="Formatting..."):        
        contents = contents + listOfContents[i] + "\n"   
    
    print("Formatted list into string.")

    #Basic Code:
    print("Domains gathered. Length:", len(contents.split("\n")))
    print("Saving to file. Please wait.")
    f = open("!blocklist.txt", "w")
    f.write(contents)
    print("Written content to file '!blocklist.txt'.")
    f.close()
    print("Closed file. You can now use this file in your blocklist.")
else:
    totalToSplit = roundDecimalUp(totalToSplit)

    print("The way we will save the file is as follows:\n1) Split your large list into lists of 200k\n2) Save these small lists of 200k\n3) Merge these small lists into a large list.")
    splitCurrent = 0
    currentFile = 1
    filesOpened = []
    for i in tqdm (range (lenList), desc="Formatting..."):
        splitCurrent += 1
        contents = contents + listOfContents[i] + "\n"
        if splitCurrent >= 200000:
            print("\nSaving the current list to file", currentFile)
            fileNameCurrent = "file" + str(currentFile) + ".txt"
            f = open(fileNameCurrent, "w")
            f.write(contents)
            f.close()
            splitCurrent = 0
            contents = ""
            currentFile += 1
            print("Opened, written, and closed file:", fileNameCurrent)
            filesOpened.append(fileNameCurrent)
    
    print("Finished formatting and saving to mini lists.\n\nNow we will start to save the small lists to a large list.")
    for file in filesOpened:
        fil = open(file, "r")
        contents = contents + fil.read()
        fil.close()
        print("Opened mini list:", file)
    
    f = open("blocklist.txt", "w")
    f.write(contents)
    f.close()