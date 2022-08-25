# Firefly
## General
Coded in python, the firefly drone isn't as much of a drone, more of a framework for drones.<br>
You have a drone.ini file in the root folder, where you can configure it according to the technical specs you have set.<br>

Supports a number of sensors and systems like GPS, Motors, Servos, Gyro, Compass, Camera, Radio Comms etc...<br>
This supports different types of drones as well, like quadcopters, planes and helicopters.

## Planned features
### Gyro stabilized gimbal camera control
For those advanced UAV drones that want to focus on a single point while flying.
### AI Image Analysis
For various purposes: <br>
* High altitude distance sensing<br>
* Target acquisition<br>
* Null Signal Navigation<br>
### Null Signal Navigation (NSN)
This is a rather complex feature, expecting lots of trial and error. <br>
Basically the most dangerous thing for an UAV is using radio signals (incl GPS), hence using AI imaging analysis and path recognition<br>
it should be possible to remember and fly back where you came from based on stored images during the flight.<br>
This avoids using any sorts of radio signals until it's near where it came from, accuracy doesn't have to be 100%, just enough for it to come back to friendly lines.<br>
### Optical Camoflauge
During the day time, it's rather easy to spot a drone, especially if there's little cloud cover. <br>
Even if the drone is able to avoid RADAR there is always the risk of optical detection.<br>
So a camoflauge is needed, this consists of an LED cover under the drone which emits low intensity RGB light.<br>
The RGB values are set by a top directed photon sensor. This will effectively mimic the color of the sky (be it clouds or blue) and should avoid detection.<br>
Light intensity should depend on the environment lighting, during the dark no light should be emitted.
