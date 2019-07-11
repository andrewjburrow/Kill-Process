import psutil



processName = input('Name> ')
def checkIfProcessRunning(processName):

    for proc in psutil.process_iter():
        try:

            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def star(processName):#true or false
    if checkIfProcessRunning(processName) == True:
        print("Found the Process")

        #holds script for user interaction
        pid_find(processName)
    elif checkIfProcessRunning(processName) == False:
        print("Nothing Similar Running")


def pid_find(processName):
    pid = []
    for proc in psutil.process_iter():
        try:
            if proc.name() == processName+'.exe':
                pid.append(proc.pid)
        except psutil.AccessDenied:
            pass
    try:
        process = pid[0]
    except IndexError:
        print("no pid")
        quit()
     #print process id
    killer(processName, process)

def killer(processName, process):# Need to use psutil instead of os library
    counterP = []
    counterC = []
    parent_pid = process
    parent = psutil.Process(process)
    for child in parent.children(recursive=True):
        counterC.append(child)
        child.kill()
    counterP.append(parent)
    parent.kill()
    if checkIfProcessRunning(processName) == True:
        star(processName)
    elif checkIfProcessRunning(processName) == False:
        print('{Child Process}')
        print('-'*25)
        for x in counterC:
            print(x)
        print('-'*25)
        print('{Parent Process}')
        for x in counterP:
            print(x)
        print('-'*25)



star(processName)
