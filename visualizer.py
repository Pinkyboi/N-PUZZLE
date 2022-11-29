import pygame

class NpuzzleVisualizer():

    _gameBoardPad = 20
    _pieceBorder = 10

    def __init__(self, puzzleDim, swaps,
                    puzzleStart=[1, 2, 3, 4, 5, 6, 7, 8, 0],
                    pieceBoardColor=(0, 0, 0),
                    bgColor=(255, 255, 255),
                    windowDim=720): # TODO: maybe add setters and getters
        print("p555555")
        self._windowDim = windowDim
        self._puzzleDim = puzzleDim
        self._pieceDim = self._windowDim // puzzleDim - self._gameBoardPad * 2
        self._bgColor = bgColor
        self._zeroPieceColor = (0, 0, 0)
        self._pieceBoardColor = pieceBoardColor
        self._puzzleStart = puzzleStart
        self._boardDim = self._pieceDim * self._puzzleDim - self._pieceBorder * self._puzzleDim
        self._boardStart = (self._windowDim - self._boardDim) // 2
        self._surface = pygame.display.set_mode((self._windowDim, self._windowDim))
        self._font_size = windowDim // (puzzleDim * 2) #to be calculated

    # def drawPieceBorder(self, row, column):
    #     if 
    #     boardRect = pygame.draw.rect(self._surface, self._pieceBoardColor,
    #                                         pygame.Rect(self._boardStart + self._pieceDim * column - (self._pieceBorder if column else 0) * column,
    #                                         self._boardStart + self._pieceDim * row - (self._pieceBorder if row else 0) * row,
    #                                         self._pieceDim,
    #                                         self._pieceDim), self._pieceBorder)
    #     pygame.display.update(boardRect)

    def printPieceNumber(self, row, column, value):
        
        number_font  = pygame.font.SysFont(None, self._font_size)                # Default font, Size 16
        number_image = number_font.render(str(value), True, (0, 0, 0))
        marginY =  (self._pieceDim - number_image.get_height()) // 2
        marginX = (self._pieceDim - number_image.get_width()) // 2
        self._surface.blit(number_image, (column + marginY, row + marginX))

    def drawPiece(self, row, column, value):
        columnCoor = self._boardStart + self._pieceDim * column - (self._pieceBorder if column else 0) * column
        rowCoor = self._boardStart + self._pieceDim * row - (self._pieceBorder if row else 0) * row
        if value:
            boardRect = pygame.draw.rect(self._surface, self._pieceBoardColor,
                                    pygame.Rect(columnCoor,
                                    rowCoor,
                                    self._pieceDim,
                                    self._pieceDim), self._pieceBorder)
            self.printPieceNumber(rowCoor, columnCoor, value)        
        else:
            boardRect = pygame.draw.rect(self._surface, self._zeroPieceColor,
                                    pygame.Rect(columnCoor,
                                    rowCoor,
                                    self._pieceDim,
                                    self._pieceDim))
        pygame.display.update(boardRect)

    def drawPieces(self):
        row = -1
        for piece in range(0, self._puzzleDim * self._puzzleDim):
            column = piece % self._puzzleDim
            if column == 0:
                row += 1
            print((row, column))
            self.drawPiece(row, column, self._puzzleStart[piece])

    def startVisualization(self):
        quit = False
        pygame.init()
        self._surface.fill(self._bgColor)
        pygame.display.flip()
        print("p55555555555")
        self.drawPieces()
        print("p55555555555")
        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = False
            



if __name__ == "__main__":
        vs = NpuzzleVisualizer(3, 720)
        vs.startVisualization()
