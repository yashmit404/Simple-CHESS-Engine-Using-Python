
class GameState:

    def __init__(self):
        
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["0" , "0" , "0" , "0" , "0" , "0" , "0" , "0" ],
            ["0" , "0" , "0" , "0" , "0" , "0" , "0" , "0" ],
            ["0" , "0" , "0" , "0" , "0" , "0" , "0" , "0" ],
            ["0" , "0" , "0" , "0" , "0" , "0" , "0" , "0" ],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.white_to_move = True
        self.move_log = []
    def make_move(self, start_sq, end_sq):

        start_row, start_col = start_sq
        end_row, end_col = end_sq

        piece_moved = self.board[start_row][start_col]

        self.board[end_row][end_col] = piece_moved

        self.board[start_row][start_col] = 0

        self.white_to_move = not self.white_to_move

    