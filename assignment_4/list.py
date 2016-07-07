import os

dbFilename = "task_database_python.txt"
dbPath = os.path.join( os.getenv("HOME"), dbFilename )
with open(dbPath, "r") as myfile:
    dbContents = myfile.read()
    print(trimmedContents) = dbContents.rstrip()
parsedTask = parseArguments(sys.argv)

