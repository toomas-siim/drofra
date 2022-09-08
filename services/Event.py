import json

class Event:
    listeners = []

    def addListener(eventKey, callback):
        Event.listeners.push({"key": eventKey,"callback": callback})

    def callEvents(calledEvent):
        for event in Event.listeners:
            if event.key is calledEvent.key:
                event.callback(calledEvent)