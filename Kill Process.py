import psutil


processName = input('Name> ')
def checkIfProcessRunning(processName):

    for proc in psutil.process_iter():
        try:

            if processName.lower() in proc.name().lower():#idk why this works
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False; #3 hours to figure out why this didnt work

def star(processName):#true or false
    if checkIfProcessRunning(processName) == True:
        print("Found the Process")
        input("KILL [ENTER]")#holds script for user interaction
        killer(processName)
    elif checkIfProcessRunning(processName) == False:
        print("Nothing Similar Running")


def killer(processName):
    try:
        for proc in psutil.process_iter():#initiate process_iter
            proc.name = processName
            if proc.name == processName:#if equal to corresponding name
                p = psutil.Process(proc.pid)
                p.kill()
    except:
        print("cannot kill process")

star(processName)
