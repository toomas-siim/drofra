import time

class Time:
    startTime = None
    timedFunctions = []

    def init(self, coreHandle):
        self.startTime = time.time()
        self.coreHandle = coreHandle

    def addTimedFunction(self, intervalMs, callback):
        self.timedFunctions.append({"lastTrigger": (time.time() * 1000), "intervalMs": intervalMs, "trigger": callback})

    def getRunTime(self):
        if self.startTime == None:
            return 0
        return time.time() - self.startTime

    def handle(self):
        for timedFunction in self.timedFunctions:
            if (time.time() * 1000) - timedFunction["lastTrigger"] > timedFunction["intervalMs"]:
                timedFunction["lastTrigger"] = time.time() * 1000
                timedFunction.trigger(self.coreHandle)