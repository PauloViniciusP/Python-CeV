import pygame

pygame.init()
pygame.mixer.music.load('mod_1/data/ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()