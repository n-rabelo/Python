import pygame

pygame.init()
pygame.mixer_music.load('ex020.mp3')
pygame.mixer.music.play()
pygame.event.wait()
