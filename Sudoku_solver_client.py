from Sudoku_Board import *
if __name__ == '__main__':
    board = SudokuBoard([ \
        [UnitCell(5), UnitCell(''), UnitCell(7), UnitCell(8), UnitCell(4), UnitCell(''), UnitCell(''), UnitCell(''),UnitCell('')], \
        [UnitCell(''), UnitCell(''), UnitCell(2), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(7),
         UnitCell('')], \
        [UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(7), UnitCell(''), UnitCell(5), UnitCell(3), UnitCell(''),
         UnitCell('')], \
        [UnitCell(''), UnitCell(1), UnitCell(4), UnitCell(''), UnitCell(2), UnitCell(''), UnitCell(7), UnitCell(''),
         UnitCell('')], \
        [UnitCell(2), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''),
         UnitCell(8)], \
        [UnitCell(''), UnitCell(''), UnitCell(8), UnitCell(''), UnitCell(5), UnitCell(''), UnitCell(1), UnitCell(4),
         UnitCell('')], \
        [UnitCell(''), UnitCell(''), UnitCell(3), UnitCell(5), UnitCell(''), UnitCell(7), UnitCell(''), UnitCell(''),
         UnitCell('')], \
        [UnitCell(''), UnitCell(6), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(5), UnitCell(''),
         UnitCell('')], \
        [UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(9), UnitCell(6), UnitCell(2), UnitCell(''),
         UnitCell(7)] \
 \
        ])
    Continue = 'Y'

    while not board.is_solved() and Continue == 'Y':
        print(board)
        board.row_checker()
        board.col_checker()
        board.block_checker()
        board.clear_board()
        board.row_checker()
        board.col_checker()
        board.block_checker()
        board.clear_board2()

        print(board)
        if board.is_solved():
            print('Solved!!')
            break
        Continue = input("Continue solving?")
        if Continue != 'Y':
            print(board.return_posibilities())