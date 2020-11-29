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
# gambling
# youtube


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

def runCompile():

    files = ["lists/abuse", "lists/ads", "lists/adservers", "lists/CoinMiner", "lists/crypto", "lists/domainlist", "lists/drugs", "lists/fraud", "lists/hosts", "lists/justdomains", 
            "lists/list", "lists/list_browser", "lists/list_optional", "lists/malware", "lists/nrop", "lists/phishing", "lists/piracy", "lists/ransomware", "lists/redirect", 
            "lists/scam", "lists/tracking", "lists/UKCommBlocks", "lists/gambling", "lists/youtube"] #array of file names. to be used on the loop to get file contents

    contents = ""

    print("Would you like to add any files to the current\narray? The current array consists of:")
    for item in files:
        print(item, end= ",")
        if item == "lists/redirect" or item == "lists/justdomains":
            print()
    inp = input("y/N> ")
    if inp.lower() == "y" or inp.lower == "yes":
        looping = True
        while looping:
            inp = input("What is the name of the file (without .txt) that you\nwould like to add to the array?\nRemember to include directory structure.\nE.g lists/malware\n Type e to exit this menu.\n> ")
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

    print("Congratulations! Your new blocklist has been made! Now we will check it, to see if it\npasses the test. If it doesn't you may wish to\nre-run the test OR re-run the actual blocklist\ncompiler if you think it may have an affect on your\nblocker.\n")
    checkLists()

def contentToCheck(i, contentsLen, blockLen):
    import random

    if i >= 0 and i <= 4:    
        return random.randint(0,contentsLen-1)
    elif i >= 5 and i <= 9:
        return random.randint(0,blockLen-1)
    else:
        exit("ERROR.")

def checkLists():
    check1 = False
    check2 = False
    check3 = False
    print("We will now check the lists to try and determine if the edits worked.")
    import time
    print("PLEASE NOTE: ALL CHECKS RUN IN MEMORY. NO CHANGES WILL BE MADE TO YOUR RAW\nLISTS OR YOUR COMPILED BLOCKLIST.")
    print("The functionality of the check tool is very hit or miss. Please remember that\nwhen creating your blocklist you may have removed or changed lines\nsuch as comment or invalid lines.\n\nThis tool is only to be used as a basis.\nTo have a blocklist be marked as valid it MUST pass the first test with a maximum\nrange rate of 2000\nand it MUST pass the last test with a minimum finding of 80%")

    files = ["lists/abuse", "lists/ads", "lists/adservers", "lists/CoinMiner", "lists/crypto", "lists/domainlist", "lists/drugs", "lists/fraud", "lists/hosts", "lists/justdomains", 
            "lists/list", "lists/list_browser", "lists/list_optional", "lists/malware", "lists/nrop", "lists/phishing", "lists/piracy", "lists/ransomware", "lists/redirect", 
            "lists/scam", "lists/tracking", "lists/UKCommBlocks"] #array of file names. to be used on the loop to get file contents
    print("Would you like to add any files to the current\narray? The current array consists of:")
    for item in files:
        print(item, end= ",")
        if item == "lists/redirect" or item == "lists/justdomains":
            print()
    inp = input("y/N> ")
    if inp.lower() == "y" or inp.lower == "yes":
        looping = True
        while looping:
            inp = input("What is the name of the file (without .txt) that you\nwould like to add to the array?\nRemember to include directory structure.\nE.g lists/malware\n Type e to exit this menu.\n> ")
            if inp == "e":
                looping = False
            else:
                files.append(inp)
    else:
        print("Alright, sticking to the current file array.")
    contents = ""


    #These lines are indeed the same line of code from the code to compile the list.
    print("Check 1.\nCheck 1 runs and gets the data from all the raw files and checks against the file blocklist.txt. It checks against the LENGTH.")

    time.sleep(3)
    for item in files:
        fileName = item + ".txt"
        print("Opened: ", fileName)
        f = open(fileName, "r")
        contents = contents + f.read()
        print("Written", fileName, "to the memory array.")
        f.close()
        contents = contents + "\n"

    time.sleep(2)
    print("\n\n\nWe have got all the entries, great! Now lets get the length of the list.")
    print("Length of the array:", len(contents.split("\n")))
    print("Now we will find the length of the compiled blocklist.")
    f = open("blocklist.txt", "r")
    block = f.read()
    f.close()
    print("Your blocklist length:", len(block.split("\n")))
    print("\n\nTo compare:\n")
    print("Your blocklist:",len(block.split("\n")),"\nList of blocklists", len(contents.split("\n")))
    print("Please remember that there may be hundreds/thousands of lines of difference, however this is good! It means we got rid of unneccesarry lines.")

    contents = contents.split("\n")
    block = block.split("\n")
    contentsLen = len(contents)
    blockLen = len(block)

    if contentsLen-blockLen <=-2001 or contentsLen-blockLen >=2001:
        print("FAILED Check 1.")
        print("Your blocklist had a difference of:", str(contentsLen-blockLen))
        check1 = False
    else:
        print("PASSED Check 1.")
        check1 = True

    print("Check 2.\nCheck 2 checks against the LAST item of the sorted arrays. This means we will sort the array, then check the LAST item.")
    time.sleep(3)


    print("File contents are being sorted now.")
    contents = sorted(contents)
    print("Sorted contents file.\nSorting blocklist file.")
    block = sorted(block)

    print("The last item of the contents files is:", contents[contentsLen-1])
    print("The last item of the blocklist file is:", block[blockLen-1])

    print("Remember, you might have deleted an entry in one of the formatting/fixing sections.")

    if contents[contentsLen-1] == block[blockLen-1]:
        print("PASSED Check 2")
        check2 = True
    else:
        print("FAILED Check 2.")
        check2 = False

    print("Final Check/Check 3.\nTake 5 random items in the list and check if it is in the blocklist and vice versa.")


    found = False
    successRate = 0

    for i in tqdm (range (10), desc="Searching and Checking..."):
        contentsIndex = contents[contentToCheck(i, contentsLen=contentsLen, blockLen=blockLen)]
        blockIndex = contents[contentToCheck(i, contentsLen=contentsLen, blockLen=blockLen)]

        if i <= 4:
            for item in block:
                if item == contentsIndex and found == False:
                    print("\nFound", contentsIndex, "in both files.")
                    found = True
                    successRate += 1
        if i >= 5:
            for item in contents:
                if item == blockIndex and found == False:
                    print("\nFound", blockIndex, "in both files.")
                    found = True
                    successRate += 1

        if found == False:
            print("\n", contentsIndex, "was NOT found in both lists.")
        found = False

        print()

    print("Calculating success rate.")
    #Percent rate calculation: (successRate * 1000) / 100 OR successRate * 10
    successCalc = (successRate * 1000) / 100
    print("Success rate:", str(successCalc) + "%")

    if successCalc < 80:
        print("FAILED Check 3")
        check3 = False
    else:
        print("PASSED Check 3")
        check3 = True

    time.sleep(2)

    check1 = "Pass" if check1 == True else "Fail" #if check1 == True: check1 = "Pass" else: check1 = "Fail"
    check2 = "Pass" if check2 == True else "Fail"
    check3 = "Pass" if check3 == True else "Fail"
    print("\n\n\n\n\nFinal results:\nCheck 1:", check1,"\nCheck 2:", check2, "\nCheck 3:", check3)

    totalCheck = "Pass" if check1 == "Pass" and check3 == "Pass" else "Fail"
    print("\n\nFinal results:", totalCheck)





inp = input("===TheEverythingBlocklist===\nWhat would you like to do?\n1) Make a blocklist\n2) Check a blocklist\n3) Exit\n> ")
if inp == "1":
    runCompile()
elif inp == "2":
    checkLists()
else:
    exit("Thanks for using ===TheEverythingBlocklist===")