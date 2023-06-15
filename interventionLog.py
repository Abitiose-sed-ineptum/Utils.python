import time, os
from datetime import date

def scanDirectory(filename, dirpath):
    print("Scanning " + str(dirpath) + " for " + str(filename) + "...",end="")
    logFound = False
    logs = os.listdir(dirpath)
    for log in logs:
        if log == filename:
            logFound = True
            print("scan completed with 1 log found.")
            break
        else:
            print("scan completed. No active logs found.")
    if len(logs) == 0:
        print("scan completed. Directory is empty.")
    return logFound

def logInterventions(filename, knownIssues, dirpath):
    logExists = scanDirectory(logName, dirpath)
    filename_full = os.path.join(dirpath, filename)

    try:
        if logExists:
            # open in append mode if file exists
            f = open(filename_full, "a")
            print("Logging session is now active in append mode\n")
        else:
            # open in write mode if file does not exist
            f = open(filename_full, "w")
            print("Logging session is now active in write mode\n")
            f.write('Date: ' + str(time.asctime()) + '\n')
            f.write("Log Type: " + logType + "\n\n")
    except:
        FileNotFoundError
        print("That file does not exist")
        exit(0)

    while (True):
        try:
            robot = input("Enter Robot Identifier: ")
            t = time.asctime()
            displayMenuOptionText(knownIssues)
            problem = input("Make a selection from the list or free type a custom description: ")

            #converting a numeric selection into text
            if problem.isnumeric():
                selection = int(problem)
                problem = knownIssues[selection]
            f.write(str(robot) + "\n")
            f.write(str(problem) + "\n")
            f.write(str(t) + "\n\n")

        except:
            print("\nClosing log...",end="")
            f.close()
            print("done")
            exit(0)

def displayMenuOptionText(knownIssues):
    ## CAUTION: indexing from 1, not zero
    # header is 62 characters across
    print("+------------------------ Options ---------------------------+")
    for i in range(0, len(knownIssues)):
        print("[{0}]\t\t\t\t{1}".format(i+1, knownIssues[i]))

    print("[CTRL+C]                           Quit Logging Interventions ")
    print("+------------------------------------------------------------+")

def retrieveKnownIssues():
    print("Populating list of known issues...",end="")
    filename = "knownIssues.txt"
    f = open(filename, "r")
    knownIssues = []
    for line in f:
        knownIssues.append(line)

    f.close()
    print("done")
    return knownIssues

if __name__ == '__main__':
    # scan all files in directory
    # if no log exists for today, create the log
    # if the log exists, append to the log

    dirpath = "./Production_Logs/"
    logType = "Production"
    today = date.today()
    logName = logType + "_" + str(today) + ".txt"

    # retrieve list of known issues, can modify in text file
    knownIssues = retrieveKnownIssues()
    logInterventions(logName, knownIssues, dirpath)
