import random
import os
import sys

FileNameLength = 100
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[];,./!@#$%^&*(){}|_+<>?'
charList = list(char)

def secureErase(file, passes, securityLevel):
    #Check if the file exists
    if not os.path.exists(file):
        sys.exit(str(file) + " does not exist")

    #Run the amount of passes
    for i in range(0, passes):
        print("SecureErasing " + str(file) + " [Pass:" + str(i) + "]", end="\r")
        #Open file
        with open(file, 'r', encoding="utf8", errors='ignore') as f:
            fileData = f.read().splitlines()
    
        #Wipe current data in file
        with open(file, 'w') as f:
            f.write('')
    
        #Getdata and prepare to write to the file
        for line in fileData:
            writeString = ''
            #Get length of line and create a string with that length
            for write in range(0, len(line) * securityLevel):
                writeString += str(charList[random.randint(0,len(charList)-1)])
      
            #Write string to file
            try:
                with open(file, 'a') as f:
                    f.write(str(writeString) + '\n')
            except:
                pass
    #Set filename to random chars
    char2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    charList2 = list(char2)
    #Gen random name
    writeString = ''
    for write in range(0, FileNameLength):
        writeString += str(charList[random.randint(0,len(charList2)-1)])
    
    #Get the file extention
    splitText = file.split('.')
    newFileName = writeString + "." + splitText[-1]

    #Rename file
    os.rename(file, newFileName)

    #Done
    print("SecureErasing " + str(file) + " [Pass:Done]")

    #Remove scrambled file
    os.remove(newFileName)