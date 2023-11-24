# import webbrowser
# webbrowser.open('C:\\Users\\Lucas\\Music\\mario.mp3')
# import winsound
# filename = 'C:\\Users\\Lucas\\PycharmProjects\\Pythonexercicios\\mario.mp3'
# winsound.PlaySound(filename, winsound.SND_FILENAME)
import pygame
pygame.mixer.init()
pygame.mixer.music.load("mario.mp3")
pygame.mixer.music.play()
pygame.event.wait()
