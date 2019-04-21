import io

profileDirectory = None
logtxtDirectory = None
firefoxDriver = None
windowHandle1 = None
windowHande2 = None
logInFile = None


def initialize():
    global profileDirectory
    global logInFile
    global logtxtDirectory

    profileDirectory = "H:\Mozilla_Firefox_Profile\PL"

    # Tracer Initialization
    logtxtDirectory = "log.txt"
    logInFile = True
    temp = io.open(logtxtDirectory, "w")
    temp.close()
