import sys
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time

class NpuzzleVisualizer():

    _pieceBorder = 10
    _fontColor = (255, 254, 252)
    _bgColor=(49, 49, 49)
    _evenPieceColor=(93, 93, 93)
    _oddPieceColor=(136, 0, 0)
    _pieceBorderColor=(0, 0, 0)
    _zeroPieceColor=(0, 0, 0)
    _timeBetweenStates = 0.8
    _puzzleIndex = 0
    _fontStyle = "Roboto-Black.ttf"

    def __init__(self, puzzleDim, puzzleStates, windowDim=720):
        pygame.init()
        self._puzzleDim = puzzleDim
        self._windowDim = windowDim
        self._pieceDim = self._windowDim // (puzzleDim + 1)
        self._pieceBorder = self._pieceDim // 30
        self._puzzleStates = puzzleStates
        self._boardDim = self._pieceDim * self._puzzleDim - (self._pieceBorder * (self._puzzleDim - 1))
        self._boardStart = (self._windowDim - self._boardDim) // 2
        self._fontSize = self._pieceDim // 2
        self._numbers = {}
        self._surface = pygame.display.set_mode((self._windowDim, self._windowDim))

    def create_font(self, text, font, size, color=(255,255,255), bold=False, italic=False):
        font = pygame.font.SysFont(font, size, bold=bold, italic=italic)
        text = font.render(text, True, color)
        return text

    def printPieceNumber(self, row, column, value):
        if value not in self._numbers.keys():
            self._numbers[value] = self.create_font(str(value), self._fontStyle, self._fontSize, self._fontColor)
        textRect = self._numbers[value].get_rect(center=(column + (self._pieceDim // 2), row + (self._pieceDim//2)))
        self._surface.blit(self._numbers[value], textRect)

    def drawPiece(self, row, column, value):
        columnCoor = self._boardStart + self._pieceDim * column - (self._pieceBorder if column else 0) * column
        rowCoor = self._boardStart + self._pieceDim * row - (self._pieceBorder if row else 0) * row
        if value:
            pieceColor = self._oddPieceColor if value % 2 else self._evenPieceColor
            pygame.draw.rect(self._surface, pieceColor,
                                    pygame.Rect(columnCoor,
                                    rowCoor,
                                    self._pieceDim,
                                    self._pieceDim))
            pygame.draw.rect(self._surface, self._pieceBorderColor,
                                    pygame.Rect(columnCoor,
                                    rowCoor,
                                    self._pieceDim,
                                    self._pieceDim), self._pieceBorder)
            self.printPieceNumber(rowCoor, columnCoor, value)
        else:
            pygame.draw.rect(self._surface, self._zeroPieceColor,
                                    pygame.Rect(columnCoor,
                                    rowCoor,
                                    self._pieceDim,
                                    self._pieceDim))

    def mySleep(self, seconds):
        start = time.time()
        while time.time() - start < seconds:
            if self.eventHandler():
                break
            pygame.time.wait(10)

    def drawPieces(self, puzzleState):
        row = -1
        for piece in range(self._puzzleDim * self._puzzleDim):
            self.eventHandler()
            column = piece % self._puzzleDim
            if column == 0:
                row += 1
            self.drawPiece(row, column, puzzleState[piece])
        pygame.display.flip()
        self.mySleep(self._timeBetweenStates)

    def pause(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self._puzzleIndex = self._puzzleIndex + 1 if event.key == pygame.K_RIGHT else self._puzzleIndex - 1
                        self._puzzleIndex = min(max(self._puzzleIndex, 0), len(self._puzzleStates) - 1)
                        self.drawPieces(self._puzzleStates[self._puzzleIndex])
                    if event.key == pygame.K_p:
                        return

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self._puzzleIndex = self._puzzleIndex + 1 if event.key == pygame.K_RIGHT else self._puzzleIndex - 1
                    self._puzzleIndex = min(max(self._puzzleIndex, 0), len(self._puzzleStates) - 1)
                    self.drawPieces(self._puzzleStates[self._puzzleIndex])
                    return False
                if event.key == pygame.K_p:
                    self.pause()
                    return True
        return False

    def startVisualization(self):
        self._surface.fill(self._bgColor)
        pygame.display.flip()
        while True:
            self.eventHandler()
            self._puzzleIndex = min(max(self._puzzleIndex, 0), len(self._puzzleStates) - 1)
            self.drawPieces(self._puzzleStates[self._puzzleIndex])
            self._puzzleIndex += 1

if __name__ == "__main__":
        vs = NpuzzleVisualizer(3)
        vs.startVisualization()
