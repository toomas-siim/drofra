import importlib

class Script:
    coreHandle = None

    def init(self, coreHandle):
        self.coreHandle = coreHandle

    def loadScript(self, scriptPath):
        importlib.import_module(scriptPath)