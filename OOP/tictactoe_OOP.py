# OOPtictactoe.py - An OOP tic-tac toe game

import copy


board_spaces = list('123456789')
X, O, BLANK = 'X', 'O', ' '

class tictactoeBoard():
    def __init__(self):
        self._board = dict() # gameBoard is represented as a Python dictionary
        self._movesTaken = list()
        for space in board_spaces:
            self._board[space] = space
            

    def displayBoard(self):
        boardStr =  f'''
                 {self._board['1']} | {self._board['2']} | {self._board['3']} 
                ---+---+---
                 {self._board['4']} | {self._board['5']} | {self._board['6']} 
                ---+---+---
                 {self._board['7']} | {self._board['8']} | {self._board['9']} 
                '''
        
        return boardStr
    
    
    def isValidmove(self, move):
        try:
            if move not in self._movesTaken and move in board_spaces:
                self._movesTaken.append(move)
                return True
            else:
                return False
        except:
            return False


    def updateBoard(self, move, mark):
        self._board[move] = mark
        

    def winningMove(self, mark):
        winning_combinations = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '4', '7'],
                    ['2','5','8'], ['3','6','9'], ['1', '5', '9'], ['3', '5', '7']]
        for win in winning_combinations:
            if self._board[win[0]] == self._board[win[1]] == self._board[win[2]] == mark:
                return True
        return False

    
    def fullBoard(self):
        for spaces in board_spaces:
            if self._board[spaces] not in ['X', 'O']:
                return False
        return True


class smallBoard(tictactoeBoard):
    def displayBoard(self):
        """Return a tiny-text representation of the board."""
        for space in board_spaces:
            if self._board[space] == BLANK:
                self._board[space] = '.'

        boardDisplay = f'''
                {self._board['1']} {self._board['2']} {self._board['3']} 
                {self._board['4']} {self._board['5']} {self._board['6']} 
                {self._board['7']} {self._board['8']} {self._board['9']} 
                '''
        
        for space in board_spaces:
            if self._board[space] == '.':
                self._board[space] = BLANK   
        return boardDisplay


              
def main():
    if input('Use mini board? Y/N: ').lower().startswith('y'):
        gameBoard = smallBoard()
    #elif input('Get Hints? Y/N: ').lower().startswith('y'):
     #   gameBoard = HintBoard()
    else:
        gameBoard = tictactoeBoard()
    print('Tic-tac-toe game in Python! Have fun!')
    currentPlayer, nextPlayer = 'X', 'O' # X goes first.

    while True:
        print(gameBoard.displayBoard())
        
        move = None
        while not gameBoard.isValidmove(move):
            print(f'What is {currentPlayer}\'s move? (1-9)')
            move = input()
        gameBoard.updateBoard(move, currentPlayer)

        if gameBoard.winningMove(currentPlayer):
            print(f'The winner is {currentPlayer}! Congratulations!')
            print(gameBoard.displayBoard())
            break
        elif gameBoard.fullBoard():
            print('It is a tie!')
            print(gameBoard.displayBoard())
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer


if __name__ == '__main__':
    main()
    
            
            
            
