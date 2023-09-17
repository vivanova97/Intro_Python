from random import randint, sample

__all__ = ['chess_board_game', 'return_four_true_games']

def _gen_chess_board() -> list[tuple]:
    """"
    Generates and returns eight random placements for the eight queens.
    """
    spaces_on_board = [(i,j) for i in range(0,8) for j in range(0,8)]
    eight_random_places = sample(spaces_on_board,8)
    
    return eight_random_places

def chess_board_game() -> bool:
    """
    Checks if any of the eight queens, randomly placed, beat each other.  If they do, returns False, if they don't 
    returns True and prints the board.
    """
    chess_board = [[0,0,0,0,0,0,0,0], 
                   [0,0,0,0,0,0,0,0], 
                   [0,0,0,0,0,0,0,0], 
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0], 
                   [0,0,0,0,0,0,0,0], 
                   [0,0,0,0,0,0,0,0], 
                   [0,0,0,0,0,0,0,0]]
    
    eight_random_places = _gen_chess_board()

    for horizontal, diagonal in eight_random_places:
        chess_board[horizontal][diagonal] = 1
    
    # print(*chess_board, sep='\n') 
    # Добавьте код сверху обратно если хочется посмотреть на расстановку которая возвращает False

    for index_row, row in enumerate(chess_board):
        if row.count(1) > 1: #Checks if two queens are in the same row
            return False
        
        for index_column, item in enumerate(row):
            if item == 1:
                if list(filter(lambda x: x == 1, (chess_board[i][index_column] for i in range(0,8)))).count(1) > 1: 
                    #Checks if two queens are in one column
                    return False
                if index_row + index_column <= 7:
                    if list(filter(lambda x: x == 1, (chess_board[index_row+index_column-i][0+i] for i in range(index_row+index_column+1)))).count(1) > 1: 
                        #Checks if two queens are in left top diagonal half 
                        return False
                if index_row + index_column > 7:
                    if list(filter(lambda x: x == 1, (chess_board[7-i][index_row+index_column-7+i] for i in range(abs(index_row+index_column-7-8))))).count(1) > 1: 
                        #Checks if two queens are in right bottom diagonal half 
                        return False
                if index_row - index_column >= 0:
                    if list(filter(lambda x: x == 1, (chess_board[index_row-index_column+i][0+i] for i in range(abs(index_row-8))))).count(1) > 1: 
                        #Checks if two queens are in left bottom diagonal half 
                        return False
                if index_row - index_column < 0:
                    if list(filter(lambda x: x == 1, (chess_board[0+i][index_column-index_row] for i in range(abs(index_column-8))))).count(1) > 1: 
                        #Checks if two queens are in top right diagonal half 
                        return False
    
    print(*chess_board, sep='\n')
    
    return True


def return_four_true_games():

    """Returns four games where the queens don't beat each other. 
    This can take around 3-5 minutes to finish running."""

    four_games_where_queens_do_not_beat = 0

    while four_games_where_queens_do_not_beat < 4:
        returned_true = chess_board_game()
        if returned_true == True:
            print('\n')
            four_games_where_queens_do_not_beat+=1

return_four_true_games()

if __name__ == '__main__':
    chess_board_game()
    return_four_true_games()