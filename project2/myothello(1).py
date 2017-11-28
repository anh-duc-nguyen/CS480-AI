from othello import *
#Jerry Lin and Mussie Habtemichael
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
        #utilityval = 0
        
       # pieces = boardstate.getPieces()
        #for piece in pieces:
            
         #   if pieces[piece] == boardstate.getPlayer():
                
          #      i,j = piece
           #     utilityval += states_values[i][j]
        #return utilityval        
        
            
      
        val = self.mycount_difference(boardstate)
        return val + self.priority(boardstate) + self.mobililty(boardstate)
   
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
    def mobility(self, boardstate):
        mobile= len(boardstate.legal_moves())
        if boardstate.getPlayer() == self.mycolor:
            return mobile
        else:
            return -mobile
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))
    def priority(self, boardstate):
        '''
        we are using to tl-corner matrix. calculate priority of the space
        
        '''
        game, c = boardstate.getPieces() , 0
        for i in game:
           if i[0] >3:
                row = 7 -i[0]
           else:
                row = i[0]

           if i[1] > 3:
                col  = 7 - i[1]
           else:
                col = i[1]
           if game[i] == self.mycolor:
                c += self.TLcorner[row][col] #my turn 🙂
           else:
                c -= self.TLcorner[row][col] #opponent turn 😞
        return c   
def count_difference(boardstate):
    return (boardstate._board.count(boardstate.to_move)
            - boardstate._board.count(opponent(boardstate.to_move)))
  


play_othello(Othello(), 2000, othello_player("computer"), JM("JerryandMussie"))