import json

class Event:
    listeners = []

    def addListener(eventKey, callback):
        Event.listeners.push({"key": eventKey,"callback": callback})

    def callEvents(calledEvent, eventData):
        for event in Event.listeners:
            if event.key == calledEvent.key:
                eventData.key = event.key
                event.callback(eventData)