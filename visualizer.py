import pygame
import time
class NpuzzleVisualizer():

    _gameBoardPad = 20
    _pieceBorder = 10

    _fontColor = (255, 254, 252)
    _bgColor=(49, 49, 49)
    _evenPieceColor=(93, 93, 93)
    _oddPieceColor=(136, 0, 0)
    _pieceBorderColor=(0, 0, 0)
    _zeroPieceColor=(0, 0, 0)

    def __init__(self, puzzleDim, puzzleStates, windowDim=720):
        self._puzzleDim = puzzleDim
        self._windowDim = windowDim
        self._pieceDim = self._windowDim // puzzleDim - self._gameBoardPad * 2
        self._puzzleStates = puzzleStates
        self._boardDim = self._pieceDim * self._puzzleDim - self._pieceBorder * self._puzzleDim
        self._boardStart = (self._windowDim - self._boardDim) // 2
        self._fontSize = self._pieceDim // 3
        self._numbers = {}
        pygame.init()
        self._surface = pygame.display.set_mode((self._windowDim, self._windowDim))

    def printPieceNumber(self, row, column, value):
        if value not in self._numbers.keys():
            numberFont  = pygame.font.Font("Roboto-Black.ttf", self._fontSize)
            numberImage = numberFont.render(str(value), True, self._fontColor)
            self._numbers[value] = numberImage
        textRect = self._numbers[value].get_rect(center=(column + (self._pieceDim // 2), row + (self._pieceDim//2)))
        self._surface.blit(self._numbers[value], textRect)

    def drawPiece(self, row, column, value):
        columnCoor = self._boardStart + self._pieceDim * column - (self._pieceBorder if column else 0) * column
        rowCoor = self._boardStart + self._pieceDim * row - (self._pieceBorder if row else 0) * row
        if value:
            pieceColor = self._oddPieceColor if value % 2 else self._evenPieceColor
            piece = pygame.draw.rect(self._surface, pieceColor,
                                    pygame.Rect(columnCoor,
                                    rowCoor,
                                    self._pieceDim,
                                    self._pieceDim))
            pieceBorder = pygame.draw.rect(self._surface, self._pieceBorderColor,
                                    pygame.Rect(columnCoor,
                                    rowCoor,
                                    self._pieceDim,
                                    self._pieceDim), self._pieceBorder)
            self.printPieceNumber(rowCoor, columnCoor, value)       
            pygame.display.update(piece)
            pygame.display.update(pieceBorder)
        else:
            zeroPiece = pygame.draw.rect(self._surface, self._zeroPieceColor,
                                    pygame.Rect(columnCoor,
                                    rowCoor,
                                    self._pieceDim,
                                    self._pieceDim))
            pygame.display.update(zeroPiece)

    def drawPieces(self, puzzleState):
        row = -1
        for piece in range(self._puzzleDim * self._puzzleDim):
            column = piece % self._puzzleDim
            if column == 0:
                row += 1
            self.drawPiece(row, column, puzzleState[piece])

    def startVisualization(self):
        quit = False
        self._surface.fill(self._bgColor)
        pygame.display.flip()
        i = 0
        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    i -= 1
                if event.key == pygame.K_RIGHT:
                    i += 1
            if (i == len(self._puzzleStates)):
                time.sleep(5)
                exit()
            self.drawPieces(self._puzzleStates[i])
            time.sleep(1)
            i += 1

if __name__ == "__main__":
        vs = NpuzzleVisualizer(3)
        vs.startVisualization()
