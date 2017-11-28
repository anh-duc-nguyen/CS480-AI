
from othello import *

class JM(othello_player):
    #  This will be called once at the beginning of the game, after
    #  a few random moves have been made.  Boardstate is the initial
    #  boardstate for the game, totalTime is the total amount of time
    #  (in seconds) in the range 60-1800 that your player will get for
    #  the game.  For our tournament, I will generally set this to 300.
    #  color is one of Black or White (which are just constants defined
    #  in the othello.py file) saying what color the player will be
    #  playing.
    def initialize(self, boardstate, totalTime, color):
        print("Initializing", self.name)
        self.mycolor = color
        pass;
    # This should return the utility of the given boardstate.
    # It can access (but not modify) the to_move and _board fields.
    # expanding this code-10/16/17
    def calculate_utility(self, boardstate):
        states_values=[[10000, -3000,10000, 800, 1000, -3000,10,000],[-3000,-5000,-450, -500,-450, -5000,-3000],
                    [1000,-450,30,10,10,30,-450,1000],[800,-500,10,50,50,10,-500,800],
                    [800,-500,10,50,50,10,-500,800],
                    [1000,-450,30,10,10,30,-450,1000],[-3000,-5000,-450,-500,-500,-450,-5000,-3000],
                    [10000,-3000,1000,800,300,1000,-3000,10000]]
        utilityval = 0
        
        pieces = boardstate.getPieces()
        for piece in pieces:
            
            if pieces[piece] == boardstate.getPlayer():
                
                i,j = piece
                utilityval += states_values[i][j]
        return utilityval        
        
            
      
        return self.mycount_difference(boardstate)
   
    def alphabeta_parameters(self, boardstate, remainingTime):
        # This should return a tuple of (cutoffDepth, cutoffTest, evalFn)
        # where any (or all) of the values can be None, in which case the
        # default values are used:
        #        cutoffDepth default is 4
        #        cutoffTest default is None, which just uses cutoffDepth to
        #            determine whether to cutoff search
        #        evalFn default is None, which uses your boardstate_utility_fn
        #            to evaluate the utility of board states.
        
        return (4, None, None)
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))

def count_difference(boardstate):
    return (boardstate._board.count(boardstate.to_move)
            - boardstate._board.count(opponent(boardstate.to_move)))
  


play_othello(Othello(), 1800, othello_player("CS480"), JM("Anh"))
