file="Current.txt"
oldfile="old.txt"
def cleanFile(file,oldfile):
    with open(file,"r+" ) as writeFile:
        with open(oldfile,"a+") as appendFile:

            #moving the cursor to start of the file
            writeFile.seek(0)

            # Reading the lines in the file and storing in members as a List
            members=writeFile.readlines()

            # 0th index is header and it is removed to get the data
            header=members[0]
            members.pop(0)

            inactive=[]
            for member in members:
                if "no" in member:
                    inactive.append(member)

            writeFile.seek(0)
            writeFile.write(header)
            appendFile.write(header)
            for member in members:
                if member in inactive:
                    appendFile.write(member)
                else:
                    writeFile.write(member)
            writeFile.truncate()

cleanFile(file,oldfile)



