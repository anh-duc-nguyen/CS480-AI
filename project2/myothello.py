
from othello import *

class AnhPlayer(othello_player):
    '''
    This is a Othello player AI with heuristic implemented
    This AI using a matrix to calculate the piority and 
    calculate the friendly mobilty of each piece on the board.
    @Author: Anh Nguyen
    @Version: Oct -16
    '''
    def initialize(self, boardstate, totalTime, color):
        print("Initializing", self.name)
        self.mycolor = color
        self.TLcorner = [[5,-1, 3, 2],\
                        [-1,-1, 2, 1],\
                        [3, 2, 2, 1 ],\
                        [ 2, 1, 1, 1]] 
        #This is matrix show the piority of each place on the board
        # since this board is symetric, I only initiate the top left conner
        pass;

    def calculate_utility(self, boardstate):
        d = self.mycount_difference(boardstate)
        return   d + self.priorityCal(boardstate)+ self.mobility(boardstate)

    def alphabeta_parameters(self, boardstate, remainingTime):

        return (4, None, None)
    def priorityCal (self, boardstate):
        '''
        This function using the TLcorner matrix, to calculate all the piority of
        every space on the board
        '''
        gameMap , p = boardstate.getPieces(),0
        for i in gameMap:
            if i[0] >3:
                row = 7 -i[0]
            else:
                row = i[0]

            if i[1] > 3:
                col  = 7 - i[1]
            else:
                col = i[1]
            if gameMap[i] == self.mycolor:
                p += self.TLcorner[row][col] #my turn :)
            else:
                p -= self.TLcorner[row][col] #opponent turn :(
        return p
    def mobility(self,boardstate):
        #calculate the mobility of the board
        mobi = len(boardstate.legal_moves())
        if boardstate.getPlayer() == self.mycolor:
            return mobi #positive if it is my turn
        else:
            return -mobi #negative if it opponent turn 
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))

def count_difference(boardstate):
    return (boardstate._board.count(boardstate.to_move)
            - boardstate._board.count(opponent(boardstate.to_move)))


#uncommend the following line to start the game
play_othello(Othello(), 1800, othello_player("CS480"), AnhPlayer("Anh"))