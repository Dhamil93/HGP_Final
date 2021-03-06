from piece import Piece



class Stone:
    Piece = Piece.NoPiece
    liberties = 0
    x = -1
    y = -1

    def __init__(self, Piece, x, y):  # a contstuctor initialising variables
        self.Piece = Piece
        self.liberties = 0
        self.x = x
        self.y = y

    def getPiece(self):  # a methoad to return Piece
        return self.Piece

    def getLiberties(self):  # a method to return Liberties
        return self.liberties

    def setLiberties(self, liberties):  # a method to set Liberties
        self.liberties = liberties

    def getup(self, boardArray):
        if self.y == 0:
            return None
        else:
            return boardArray[self.y - 1][self.x]  # move y coordinate upwards

    def getright(self, boardArray):
        if self.x == 6:
            return None
        else:
            return boardArray[self.y][self.x + 1]  # move x coordinate to the right

    def getleft(self, boardArray):
        if self.x == 0:
            return None
        else:
            return boardArray[self.y][self.x - 1]  # move x coordinate to the left

    def getdown(self, boardArray):
        if self.y == 6:
            return None
        else:
            return boardArray[self.y + 1][self.x]  # move y coordinate to downwards


class GameLogic():

    print("Game Logic Object Created")
    # TODO add code here to manage the logic of your game
    turn = Piece.White
    Xpos = 0
    Ypos = 0
    boardArray = 0
    whiteprisoners = 0
    blackprisoners = 0
    whiteterritories = 0
    blackterritories = 0


    def updateparams(self,boardArray,xpos,ypos):
        # update current variables
        self.Xpos = xpos
        self.Ypos = ypos
        self.boardArray=boardArray


    def checklogic(self,boardArray,xpos,ypos):
        # update current variables
        self.Xpos = xpos
        self.Ypos = ypos
        self.boardArray=boardArray


    def checkvacant(self):
        # check if the position is vacant or not
        if self.boardArray[self.Ypos][self.Xpos].Piece==Piece.NoPiece :
            return True
        else :
            return False


    def changeturn(self):
        # function to swap turns
        print("turn changed")
        if self.turn == Piece.Black:
            self.turn = Piece.White
        else:
            self.turn = Piece.Black


    def placestone(self):
        # function to place the stone on the board
        if self.turn == Piece.Black:
            self.boardArray[self.Ypos][self.Xpos].Piece = Piece.Black
        else:
            self.boardArray[self.Ypos][self.Xpos].Piece = Piece.White

        print("Liberties = " + str(self.boardArray[self.Ypos][self.Xpos].liberties) + "x pos = " + str(
            self.boardArray[self.Ypos][self.Xpos].x) + "y pos = " + str(self.boardArray[self.Ypos][self.Xpos].y))


    def updateLiberties(self):
        # update the liberties of all the available stones
        count = 0
        for row in self.boardArray :
            for cell in row :
                count=0
                if cell.Piece != Piece.NoPiece :
                    Stonecolor=cell.Piece

                    if cell.getup(self.boardArray) != None and (cell.getup(self.boardArray).Piece == Stonecolor or cell.getup(self.boardArray).Piece == Piece.NoPiece) :
                        count=count+1
                    if cell.getright(self.boardArray) != None and (cell.getright(self.boardArray).Piece == Stonecolor or cell.getright(self.boardArray).Piece == Piece.NoPiece) :
                        count=count+1
                    if cell.getleft(self.boardArray) != None and (cell.getleft(self.boardArray).Piece == Stonecolor or cell.getleft(self.boardArray).Piece == Piece.NoPiece) :
                        count=count+1
                    if cell.getdown(self.boardArray) != None and (cell.getdown(self.boardArray).Piece == Stonecolor or cell.getdown(self.boardArray).Piece == Piece.NoPiece) :
                        count=count+1
                    cell.setLiberties(count)


    def updatecaptures(self):
        # update captures of entire board, i.e. remove all stone who have 0 liberties left
        for row in self.boardArray :
            for cell in row :
                if(cell.liberties==0 and cell.Piece != Piece.NoPiece):
                    if(cell.Piece== Piece.Black):
                        self.whiteprisoners=self.whiteprisoners+1
                        self.boardArray[cell.y][cell.x]=Stone(Piece.NoPiece,cell.x,cell.y)
                        print("Black Stone Captured at x: "+str(cell.x) + ", y: "+str(cell.y))
                        return "Black Stone Captured at x: "+str(cell.x) + ", y: "+str(cell.y)
                    elif(cell.Piece== Piece.White):
                        self.blackprisoners=self.blackprisoners+1
                        self.boardArray[cell.y][cell.x] = Stone(Piece.NoPiece, cell.x, cell.y)
                        print("White Stone Captured at x: " + str(cell.x) + ", y: " + str(cell.y))
                        return "White Stone Captured at x: " + str(cell.x) + ", y: " + str(cell.y)


    def updatecaptures2(self):
        # function to check if any of the neighbouring stones of the current placement has 0 liberties left , if yes then capture them
        if self.boardArray[self.Ypos][self.Xpos].getup(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getup(self.boardArray).liberties == 0 and self.boardArray[self.Ypos][
                self.Xpos].getup(self.boardArray).Piece != Piece.NoPiece :

            return self.capturePiece(self.Xpos,self.Ypos-1)
        elif  self.boardArray[self.Ypos][self.Xpos].getright(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getright(self.boardArray).liberties == 0 and self.boardArray[self.Ypos][
                self.Xpos].getright(self.boardArray).Piece != Piece.NoPiece :
            return self.capturePiece(self.Xpos+1, self.Ypos)
        elif  self.boardArray[self.Ypos][self.Xpos].getleft(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getleft(self.boardArray).liberties == 0 and self.boardArray[self.Ypos][
                self.Xpos].getleft(self.boardArray).Piece != Piece.NoPiece :
            return self.capturePiece(self.Xpos-1, self.Ypos)
        elif  self.boardArray[self.Ypos][self.Xpos].getdown(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getdown(self.boardArray).liberties == 0 and self.boardArray[self.Ypos][
                self.Xpos].getdown(self.boardArray).Piece != Piece.NoPiece :
            return self.capturePiece(self.Xpos, self.Ypos+1)


    def capturePiece(self,xpos,ypos):
        # captures a piece at the given position
        if self.boardArray[ypos][xpos].Piece == 1:  # if the piece is white
            self.blackprisoners = self.blackprisoners + 1
            self.boardArray[ypos][xpos] = Stone(Piece.NoPiece, xpos, ypos)
            return "White Stone Captured at x: " + str(xpos) + ", y: " + str(ypos)

        else:  # if the piece is black
            self.whiteprisoners = self.whiteprisoners + 1
            self.boardArray[ypos][xpos] = Stone(Piece.NoPiece, xpos, ypos)
            return "Black Stone Captured at x: " + str(xpos) + ", y: " + str(ypos)


    def checkforSuicide(self):
        oppositeplayer=Piece.NoPiece
        if self.turn==Piece.Black :
            oppositeplayer=Piece.White
        else :
            oppositeplayer =Piece.Black
        count=0
        # counts the neighbouring positions for opposite stones or nulls(end of board)
        if self.boardArray[self.Ypos][self.Xpos].getup(self.boardArray) == None or self.boardArray[self.Ypos][self.Xpos].getup(self.boardArray).Piece == oppositeplayer :
            count=count+1
        if self.boardArray[self.Ypos][self.Xpos].getleft(self.boardArray) == None or self.boardArray[self.Ypos][self.Xpos].getleft(self.boardArray).Piece == oppositeplayer :
            count = count + 1
        if self.boardArray[self.Ypos][self.Xpos].getright(self.boardArray) == None or self.boardArray[self.Ypos][self.Xpos].getright(self.boardArray).Piece == oppositeplayer :
            count = count + 1
        if self.boardArray[self.Ypos][self.Xpos].getdown(self.boardArray) == None or self.boardArray[self.Ypos][self.Xpos].getdown(self.boardArray).Piece == oppositeplayer :
            count = count + 1

        if(count==4) : # this means all side are of opposite color or end of board
            # now checking if any of the neighbours have a single liberty, if they do then by placing this stone, their liberties would turn to zero so it wont be suicide
            if self.boardArray[self.Ypos][self.Xpos].getup(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getup(self.boardArray).liberties == 1:
                return False
            if self.boardArray[self.Ypos][self.Xpos].getleft(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getleft(self.boardArray).liberties == 1:
                return False
            if self.boardArray[self.Ypos][self.Xpos].getright(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getright(self.boardArray).liberties == 1:
                return False
            if self.boardArray[self.Ypos][self.Xpos].getdown(self.boardArray) != None and self.boardArray[self.Ypos][
                self.Xpos].getdown(self.boardArray).liberties == 1:
                return False
            return True
        else :
            return False


    def getBlackPrisoner(self):
        return str(self.blackprisoners)


    def getWhitePrisoner(self):
        return str(self.whiteprisoners)


    def getBlackTerritories(self):
        return str(self.blackterritories)


    def getWhiteTerritories(self):
        return str(self.whiteterritories)


    def updateTeritories(self):
        # update the current positions occupied by each player
        countb = 0
        countw = 0
        for row in self.boardArray:
            for cell in row:
                if cell.Piece == Piece.Black:
                    countb = countb + 1
                elif cell.Piece == Piece.White:
                    countw=countw+1
        self.whiteterritories=countw
        self.blackterritories=countb


    def getScore(self,Piece):
        if Piece==2:
            return self.blackterritories+self.blackprisoners
        else:
            return self.whiteterritories+ self.whiteprisoners









