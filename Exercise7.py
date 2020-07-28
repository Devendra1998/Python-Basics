# Healthy Programmer

# 9am - 5pm
# water-water.mp3 (3.5 litres) - he typed Drank -
# log we will created
# Eyes - eyes.mp3 -every 30min -EyDone -log
# Physical activity - physical.mp3 every -45min -ExDone -log
#
# Rules
# Pygane module to play audio

import time
import pygame
w=open("water log.txt","a")
e=open("Eye exercise.txt","a")
p=open("Physical exercise.txt","a")
a=time.localtime()
print(a)