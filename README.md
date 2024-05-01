# smart-blinds

## Evan Hall ehall9@nd.edu and Derek Pepple dpepple@nd.edu

Due to the packages required to run the flask server with Alexa, python must be 3.10 or less

Abstract: Blinds can be in inconvenient places and users might want to control them or set them automatically. Using a D/C motor, users are able to drive the bead chain of their blinds. Then, using a photoresistor and an Amazon Alexa, users can control the blinds from anywhere in the room, or set it to open and close depending on light levels.

Main.py - runs the light sensor and web server threads
lightControl.py - runs the photoresistor and motor code
flaskSkill.py - runs the web server that the alexa skill accesses
