# echomaster-server
Server for echomaster - control PC's sound volume with simple gestures.

## What??
This program is a server designed to work on a Raspberry Pi 3 (or other RPi-compatible hardware) .
RPi must have an ultrasonic distance sensor connected via GPIO.
By moving hand closer or further from ultrasonic sensor you can change sound volume on all clients(Windows only) connected to that echomaster server.

## Where is the client?
Here: https://github.com/AndrewRocky/echomaster-client

## How to run:
`python3 server.py`

## Trivia:
Project was created as a final project for 'Internet of Things' course of Kumoh National Institute of Technology.
