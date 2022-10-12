from os import listdir
from os.path import isfile, join, basename
import importlib
from system.Sensor import Sensor

class Script:
    coreHandle = None
    scripts = []
    activeScript = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle

    def handleScripts():
        for script in Script.scripts:
            if Script.activeScript == script.name:
                script.handle()

    def importAllScripts(coreHandle):
        scripts = Script.getScriptsFromFolder("./scripts/")
        for script in scripts:
            Script.loadScript(script, coreHandle)

    def processRequirements(scriptName, requirements, coreHandle):
        for requirement in requirements:
            if requirement["system"] == "sensor":
                if requirement["required"] == True:
                    if Sensor.getSensorHandleByPurpose(requirement["requirement"]["purpose"]) == None:
                        coreHandle.shutdown = True
                        coreHandle.writeLog("Failed loading script: " + scriptName)
                        coreHandle.writeLog("--> Missing requirement: " + requirement["requirement"]["purpose"] + " sensor.")
                        return False

    def getScriptsFromFolder(folder):
        return [f for f in listdir(folder) if isfile(join(folder, f))]

    def getBasename(path):
        return basename(path).split(".")[0]

    def loadScript(scriptPath, coreHandle):
        className = basename(scriptPath).split(".")[0]
        module = importlib.import_module("scripts." + className)
        my_class = getattr(module, className)
        my_instance = my_class()
        try:
            my_instance.init(coreHandle)
            Script.processRequirements(className, my_instance.REQUIREMENTS, coreHandle)
        except BaseException as err:
            coreHandle.writeLog("Unable to start script: " + basename(scriptPath).split(".")[0])
            coreHandle.writeLog("Failure message: " + str(err))
        Script.scripts.append(my_instance)