import datetime
import io

import Model.settings


def log(message):

    print(datetime.datetime.now().ctime() + "   " + message)
    if Model.settings.logInFile:
        file = io.open(Model.settings.logtxtDirectory, "a")
        file.write(datetime.datetime.now().ctime() + " " + message + "\n")
        file.close()
