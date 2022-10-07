from os import listdir
from os.path import isfile, join, basename
import importlib

class Script:
    coreHandle = None
    scripts = []

    def init(self, coreHandle):
        self.coreHandle = coreHandle

    def handleScripts():
        for script in Script.scripts:
            script.handle()

    def importAllScripts(coreHandle):
        scripts = Script.getScriptsFromFolder("./scripts/")
        for script in scripts:
            Script.loadScript(script, coreHandle)

    def getScriptsFromFolder(folder):
        return [f for f in listdir(folder) if isfile(join(folder, f))]

    def loadScript(scriptPath, coreHandle):
        module = importlib.import_module("scripts." + basename(scriptPath).split(".")[0])
        my_class = getattr(module, basename(scriptPath).split(".")[0])
        my_instance = my_class()
        try:
            my_instance.init(coreHandle)
        except BaseException as err:
            coreHandle.writeLog("Unable to start script: " + basename(scriptPath).split(".")[0])
            coreHandle.writeLog("Failure message: " + str(err))
        Script.scripts.append(my_instance)