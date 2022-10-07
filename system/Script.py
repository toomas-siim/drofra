from os import listdir
from os.path import isfile, join

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
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        instance = class_()
        instance.init(coreHandle)
        Script.scripts.push(instance)