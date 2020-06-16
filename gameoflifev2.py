# Icons made by https://www.flaticon.com/authors/pixel-perfect

import sys
import time
import pygame
from random import randint
import numpy as np
from pygame import mixer
from matplotlib import pyplot as plt


# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
running = True  # Start rendering
pause = False  # Pause the game
frames = 10
fps = 1.0 / frames  # Frames per second
mixer.init()

# Window Settings
width = 800
height = width
rows = -1

while rows > 200 or rows <= 0:
    rows = int(input('Digite el tamanio del tablero nxn: '))  # Tamaño del tablero (Número de filas y columnas)

gap = width // rows  # Distancia de separación entre las filas y columnas

# Personalize Windows Frame
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("El juego de la vida de Conway")
icon = pygame.image.load('icon.png')
playImage = pygame.image.load('play.png')
pygame.display.set_icon(icon)

N = int(input('Digite el numero N de elementos iniciales: '))  # Cantidad de celulas vivas en la primera iteración.
m = int(input('Digite el numero m de generaciones a mostrar: '))  # Cantidad de generaciones a mostrar.

des = -1

while des != 0 and des != 1:
    des = int(input('Generar graficos 0, ejecutar animacion 1: '))

# Generate a matriz for saving the information about all cells.
map = np.zeros((rows, rows), dtype=int)  # Mapa que contiene la informacion de las celulas
aliveCells = []  # Array que alamcena las celulas y sus posiciones
deadCells = []  # Array que alamcena las celulas muertas y sus posiciones

numBorn = []
numDead = []
numAlive = []

iterBorn = []
iterDead = []
iterAlive = []


class Game:

    def draw_cell(self, pos, color):
        x, y = pos
        pygame.draw.rect(screen, color, (y * gap, x * gap, gap, gap))

    def randomCells(self, map, n, N):
        i = 0
        for i in range(0, N):
            position = (randint(0, n - 1), randint(0, n - 1))
            self.draw_cell(position, BLACK)
            map[position] = 1
            aliveCells.append(position)
            if des == 1:
                pygame.display.update()

    def neighbors_numbers(self, x, y):
        neighbors_positions = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                               (x + 0, y - 1), (x + 0, y + 1),
                               (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
        number = 0
        for x, y in neighbors_positions:
            if 0 <= x < rows and 0 <= y < rows:
                number += map[(x, y)]
        return number

    def __init__(self, n, N):
        self.randomCells(map, n, N)  # Se generan N celulas en posiciones aleatorias
        self.start = aliveCells

    def __iter__(self):
        self.actual = self.start
        return self

    def __next__(self):
        if len(self.actual) > 0:
            self.newMap = newMap
            Generation(self.actual, map, self.newMap)
            numBorn.append(len(iterBorn))
            numAlive.append(len(iterAlive))
            numDead.append(len(iterDead))
            iterAlive.clear()
            iterDead.clear()
            iterBorn.clear()
            return self.actual
        else:
            raise StopIteration


class Generation:

    def draw_cell(self, pos, color):
        x, y = pos
        pygame.draw.rect(screen, color, (y * gap, x * gap, gap, gap))

    def neighbors_numbers(self, x, y):
        neighbors_positions = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                               (x + 0, y - 1), (x + 0, y + 1),
                               (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
        number = 0
        for x, y in neighbors_positions:
            if 0 <= x < rows and 0 <= y < rows:
                number += map[(x, y)]
        return number

    def __init__(self, last, elements, newMap):
        self.actual = last
        self.elements = elements
        self.nextMap = newMap
        for x in range(rows):
            for y in range(rows):
                num = self.neighbors_numbers(x, y)
                if num == 3 and self.elements[(x, y)] == 0:
                    self.born((x, y))
                elif (num == 2 or num == 3) and self.elements[(x, y)] == 1:
                    self.alive((x, y))
                elif (num <= 1 or num >= 4) and self.elements[(x, y)] == 1:
                    self.dead((x, y))

    def alive(self, pos):
        if pos not in iterAlive:
            iterAlive.append(pos)
        self.nextMap[pos] = 1
        self.draw_cell(pos, BLACK)
        self.actual = aliveCells

    def born(self, pos):
        if pos not in aliveCells:
            aliveCells.append(pos)
        if pos not in iterBorn:
            iterBorn.append(pos)
        if pos in deadCells:
            deadCells.remove(pos)
        if pos in iterDead:
            iterDead.remove(pos)
        self.nextMap[pos] = 1
        self.draw_cell(pos, BLACK)
        self.actual = aliveCells

    def dead(self, pos):
        if pos in aliveCells:
            aliveCells.remove(pos)
        if pos in iterAlive:
            iterAlive.remove(pos)
        if pos not in deadCells:
            deadCells.append(pos)
        if pos not in iterDead:
            iterDead.append(pos)
        self.nextMap[pos] = 0
        self.draw_cell(pos, WHITE)
        self.actual = aliveCells

    def next(self):
        self.elements = self.nextMap


if __name__ == '__main__':
    screen.fill(WHITE)
    screen.blit(playImage, (width - 50, 10))
    x = [i for i in range(m)]
    if des == 1:
        pygame.display.update()
        mixer.music.load('music.mp3')
        mixer.music.play(-1)
    newMap = np.copy(map)
    numBorn.append(N)
    numAlive.append(0)
    numDead.append(0)
    frame = iter(Game(rows, N))
    h = 0
    while running:
        h += 1
        print('Ejecutando...')
        if h == m:
            if des == 0:
                pygame.quit()
                print('Imprimiendo el histograma... ')

                fig = plt.figure("Juego de la vida de Conway")
                grupo1 = fig.add_subplot(311)
                grupo2 = fig.add_subplot(312)
                grupo3 = fig.add_subplot(313)

                grupo1.bar(x, numBorn, color='g', align='center')
                grupo1.set_ylabel("Nacimientos ")
                grupo1.set_xlabel("Iteraciones")

                grupo2.bar(x, numAlive, color='c', align='center')
                grupo2.set_ylabel("Vivos")
                grupo2.set_xlabel("Iteraciones")

                grupo3.bar(x, numDead, color='m', align='center')
                grupo3.set_ylabel("Muertes")
                grupo3.set_xlabel("Iteraciones")
                plt.show()
                sys.exit(0)
            else:
                pause = True
                pygame.mixer.music.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Se ha cerrado el juego. ")
                pygame.mixer.music.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    if 749 <= mouseX <= 776 and 10 <= mouseY <= 33:
                        pause = not pause
                        pygame.mixer.music.stop() if pause else mixer.music.play(-1)
                        print('Se ha pausado el juego. ')
            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)
                if key_name == 'space':
                    pause = not pause
                    pygame.mixer.music.stop() if pause else mixer.music.play(-1)
                    print('Se ha pausado el juego. ')
        if not pause:
            try:
                next(frame)
                screen.blit(playImage, (width - 50, 10))
                map = np.copy(newMap)
                if des == 1:
                    pygame.display.update()
                time.sleep(fps)
            except StopIteration:
                print('Ya no hay celulas vivas :(')
                pause = True
                pygame.mixer.music.stop()
