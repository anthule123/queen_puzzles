
#biểu diễn board ở matplot lib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pygame as pg
import sys
import time
import random
import math

from queen import Queen
class ChessBoardDrawing():
    def __init__(self, width, height, imageName):
        self.width = width
        self.height = height
        pg.init()
        self.screen = pg.display.set_mode((width*100, height*100))
        self.imageName = imageName
        pg.display.set_caption("Chess Board")
        clock = pg.time.Clock()
#dùng pygame để vẽ bàn cờ
    
    #vẽ bàn cờ
    def drawBoard(self):
        for i in range(self.width):
            for j in range(self.height):
                if (i + j) % 2 == 0:
                    pg.draw.rect(self.screen, (255, 255, 255), (i*100, j*100, 100, 100))
                else:
                    pg.draw.rect(self.screen, (0, 0, 0), (i*100, j*100, 100, 100))
    def drawQueen(self, queens):
        #tạo list 3 quân hậu
    
        for queen in queens:
            #vẽ queen từ queen.jpg
            queenImg = pg.image.load(
                #lấy đường dẫn của file queen.jpg
                'queen.jpg'
            )
            #chỉnh lại kích cỡ hậu
            queenImg = pg.transform.scale(queenImg, (100, 100))
            self.screen.blit(queenImg, (queen.col*100, queen.row*100))
    
    def run(self, queens):
        screen = self.screen
        clock = pg.time.Clock()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            screen.fill((0, 0, 0))
            self.drawBoard()
            self.drawQueen(queens=queens)
            pg.image.save(self.screen, self.imageName)

            pg.display.flip()
            clock.tick(1)
            #chạy 0.1s rồi dừng lại
            time.sleep(0.01)
            break

    #dừng chương trình  


