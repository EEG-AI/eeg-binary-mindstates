import pygame
import random
import time


pygame.init()

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
width, height = screen.get_size()

white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.SysFont("None", 200)  #we can make this bigger later

start_time = time.time()
total_time = 300 # 5 mins = 300 seconds

#protocol steps

#blank screen for 1 minute

#display on for 3.5 seconds
display_text("ON")
time.sleep(3.5)

#break for 3.5 seconds
screen.fill(WHITE)
time.sleep (3.5)
#random on/off for 3.5 for the 300 seconds (5 mins)
while time.time() -start_time < total_time:
    word = random.choice(["ON", "OFF"])