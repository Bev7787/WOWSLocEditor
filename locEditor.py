import polib
import re
import os
dict = {}
tempList = []
location = []
terminate = False

def changefileReader(file, splitter): #Reads in the contents of changes.txt, separates based on a splitter and places the results in a dictionary.
    f = open(file, "r")
    for line in f:
        line = line.rstrip()
        tempList = line.split(splitter)
        dict[tempList[0]] = tempList[1]
        tempList = []
    f.close()
    print("Changes loaded in")
def fileReader(file): #Reads in the location of the global.mo file from filepath.txt
    f = open(file, "r")
    for line in f:
        line = line.rstrip()
        location.append(line)
    f.close()
def changeLocation(): #Add/modify global.mo file location.
    uin = str(input(f'\nInput the option below:\n1: Add a new location\n2: Update location to latest WOWS version.\n0: Return to main menu\nInput: '))
    if (uin == "1"):
        f = open("editor_files/filepath.txt", "w")
        tempList = input(f'Copy and paste the location of the global.mo file for your WOWS installation (Ensure backslashes are used). (See README for an example)\n').split("\\")
        f.write(f'{"/".join(tempList)}')
        tempList = []
        f.close()
    elif (uin == "2"):
        f = open("editor_files/filepath.txt", "r")
        line = f.readline().rstrip()
        tempList = line.split("/")
        f.close()
        newTemp = []
        for path in tempList: #checks filepath up to bin and saves.
            if (path == "bin"):
                newTemp.append(path)
                break
            newTemp.append(path)
        newAddressList = os.listdir("/".join(newTemp)) #assigns newAddressList to directory listing in /bin folder
        highest = int(newAddressList[0])
        for folder in newAddressList:
            if int(folder) > highest:
                highest = int(folder)
        newAddress = highest
        previous = ""
        for i in range (0, len(tempList)):
            if (tempList[i] == "bin"):
                previous = tempList[i+1]
                tempList[i+1] = str(newAddress)
                break
        f = open("editor_files/filepath.txt", "w")
        f.write(f'{"/".join(tempList)}')
        f.close()
        tempList = []
        print(f'Updated /bin folder to {highest}. (Previously {previous}.)')
    elif (uin == "0"):
        print("Returning to main menu.")
    else:
        print("Error: Invalid input")
def addEntry(ID, changedText, file, splitter): #Add/modify entry into changes.txt
    existingLines = []
    f = open(file, "r+")
    n = 0
    elementLoc = 0
    isWritten = False
    for line in f:
        line = line.rstrip()
        tempList = line.split(splitter)
        existingLines.append(tempList)
        if (tempList[0] == ID):
            elementLoc = n
            isWritten = True
        n+=1
        tempList = []
    f.close() #file read complete
    if (isWritten == True):
        n = 0
        if (existingLines[elementLoc][0] == ID): #checks to see if the parameter ID and the ID in the list match up
            existingLines[elementLoc][1] = changedText
            f = open(file, "w")
            while n < len(existingLines) - 1:
                f.write(f'{existingLines[n][0]}:{existingLines[n][1]}')
                f.write("\n")
                n+=1
            f.write(f'{existingLines[n][0]}:{existingLines[n][1]}') #final line does not have a newline at the end
            f.close()
        else:
            print("Error: Failed to compare ID.")
    else:
        f = open(file, "a")
        f.write("\n")
        f.write(f'{ID}:{changedText}')
        f.close()
def modifyFile(): #Modify the global.mo file based off the settings in the other files.
    fileReader("editor_files/filepath.txt")
    changefileReader("editor_files/changes.txt", ":")
    mo = polib.mofile(location[0] + '/global.mo')
    n = 0
    for entry in mo:
        if (entry.msgid in dict):
            entry.msgstr = dict[entry.msgid]
        n+=1
        print(f'\rLines scanned: {n}', end = "", flush=True)
    print(f'\nDone... Saving file...')
    mo.save(location[0] + '/global.mo')
    print("Done!")
def searchMo():
    fileReader("editor_files/filepath.txt")
    mo = polib.mofile(location[0] + '/global.mo')
    searchList = input("Enter search term. (Enter nothing to exit): ")
    while searchList:
        for entry in mo:
            check = re.search(f'(?i){searchList}', entry.msgstr)
            if (check and entry.msgid != "IDS_SSE_TEMPLATES_META"):
                print(f'{entry.msgid}:{entry.msgstr}')
                print('')
        print(f'===========================End of Search===========================\n')
        searchList = input("Enter search term. (Enter nothing to exit): ")
#main code
print(f'Welcome to the WoWs Localisation Editor tool. This tool automatically applies any modifications desired to the global.mo localisation file.\nIf you have not already, please review the README file.')
print('To navigate the interface, enter the character corresponding to the option desired.')
print(f'1: Add or modify localisation file location. (This should be done upon first use or after a game update.)\n2: Add or modify elements to be changed.\n3: Implement changes to localisation file.\n4: Search for ID by input.\nQ: Quit the Application.')
uin = str(input("Input: "))
while terminate == False:
    if uin == "1":
        changeLocation()
    elif uin == "2":
        isShip = str(input(f'\nTo return to main menu, enter 0 in the input.\nIs the item to be changed a ship? [Y/N]: ').upper())
        if (isShip == "Y"):
            id = input(f'\nEnter the ID of the ship to be modified: ').upper()
            changeText = input("Enter desired name: ")
            changeTextFull = input("Enter desired full name: ")
            addEntry(id, changeText, "editor_files/changes.txt", ":")
            addEntry(id+"_FULL", changeTextFull, "editor_files/changes.txt", ":")
        elif (isShip == "N"):
            id = input(f'\nEnter the ID of the element to be modified: ').upper()
            changeText = input("Enter desired text: ")
            addEntry(id, changeText, "editor_files/changes.txt", ":")
        elif (isShip == "0"):
            print("Returning to main menu.")
        else:
            print("Error: Invalid input")
    elif uin == "3":
        promptUser = input(f'Are you sure you want to modify the file? [Y/N]: ').upper()
        if (promptUser == "Y"):
            modifyFile()
        else:
            print("Returning to main menu.")
    elif uin == "4":
        searchMo()
    elif uin == "5":
        import antigravity
    elif uin.lower() == "q":
        terminate = True
        print("Exiting application...")
        break
    else:
        print("Error: Invalid input")
    print("==========================================================================")
    print(f'1: Add or modify localisation file location. (This should be done upon first use or after a game update.)\n2: Add or modify elements to be changed.\n3: Implement changes to localisation file.\n4: Search for ID by input.\nQ: Quit the Application.')
    uin = str(input("Input: "))


