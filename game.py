from players import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None #keep track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for (i,x) in enumerate(self.board) if x == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, then return
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # winner if there's 3 in a row anywhere
        # first we check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check the column next
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True
        
        # check all diagonals
        # only even numbered indices need to be checked
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diag
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diag
            if all([spot == letter for spot in diagonal2]):
                return True

        #if all of those faile
        return False

def play(game, x_player, o_player, print_game = True):
    
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterating while the game still has empty squares
    # we don't have to worry if someone has won because that will
    # break the loop

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

    #let's make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') # empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # we need to alternate the letter
            letter = 'O' if letter == 'X' else 'X'
        if print_game:
            time.sleep(.8)

    if print_game:
            print('It\'s a tie!')

if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)