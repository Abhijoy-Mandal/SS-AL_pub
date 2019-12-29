from typing import List, Union, Tuple, Any


class UnitCell:
    """

    """
    def __init__(self, element: Any) -> None:
        if element == '':
            self.element = element
            self._possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.element = element
            self._possibilities = None

    def __str__(self):
        return '{self.element}'.format(self=self)

    def remove_possibilities(self, value: int) -> None:
        if self._possibilities is not None and value in self._possibilities:
            self._possibilities.remove(value)

    def get_possibilities(self) -> List[int]:
        return self._possibilities

    def set_possibilities(self) -> None:
        self._possibilities = None


class SudokuBoard:
    """
    A class representing a 9x9 sudoku board
    It is stored as a List of Lists

    Every blank space is represented by ''
    and other spaces by integers between [0-9]
    Attributes
    """
    def __init__(self, board: List[List[UnitCell]]) -> None:
        self.board = []
        for row in board:
            self.board.append(row[:])

    def __str__(self):
        """
        >>> Sudoku = SudokuBoard([\
                                 [UnitCell(''), UnitCell(6), UnitCell(5), UnitCell(1), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(9), UnitCell(7)],\
                                 [UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(5), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell('')],\
                                 [UnitCell(9), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell('')],\
                                 [UnitCell(''), UnitCell(''), UnitCell(8), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell('')],\
                                 [UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(9), UnitCell(6), UnitCell(''), UnitCell(''), UnitCell('')],\
                                 [UnitCell(6), UnitCell(''), UnitCell(''), UnitCell(8), UnitCell(1), UnitCell(''), UnitCell(5), UnitCell(4), UnitCell('')],\
                                 [UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(7), UnitCell(8), UnitCell(2), UnitCell(''), UnitCell(''), UnitCell(5)],\
                                 [UnitCell(''), UnitCell(4), UnitCell(2), UnitCell(''), UnitCell(''), UnitCell(9), UnitCell(8), UnitCell(6), UnitCell('')],\
                                 [UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell(''), UnitCell('')]\
                                    ])
        >>> print(Sudoku)
        |___|_6_|_5_|_1_|___|___|___|_9_|_7_|
        |___|___|___|___|_5_|___|___|___|___|
        |_9_|___|___|___|___|___|___|___|___|
        |___|___|_8_|___|___|___|___|___|___|
        |___|___|___|___|_9_|_6_|___|___|___|
        |_6_|___|___|_8_|_1_|___|_5_|_4_|___|
        |___|___|___|_7_|_8_|_2_|___|___|_5_|
        |___|_4_|_2_|___|___|_9_|_8_|_6_|___|
        |___|___|___|___|___|___|___|___|___|
        <BLANKLINE>
        """
        str = ""
        #i = 0
        for row in self.board:
            str += '|'
            #j = 0
            for element in row:
                if element.element == '':
                    str += '___|'
                    # if j % 3 == 2:
                    #     str += '___||'
                    # else:
                    #     str += '___|'
                else:
                    str += f'_{element.element}_|'
                    # if j % 3 == 2:
                    #     str += f'_{element.element}_||'
                    # else:
                    #     str += f'_{element.element}_|'
                #j += 1
            str += f'\n'
        return str

    def is_solved(self) -> Any:
        for row in self.board:
            for element in row:
                if element.element == '':
                    return False
        return True

    def return_posibilities(self) -> str:
        s = ''
        for i in range(9):
            for j in range(9):
                if self.board[i][j].get_possibilities() is None:
                    s += f'element at {i}x{j} := [] \n'
                else:
                    s += f'element at {i}x{j} := {self.board[i][j].get_possibilities()}\n'
        return s

    def col_checker(self) -> None:
        cols = BoardAsCol(self)
        for col in cols.Columns:
            col.remove_possibilities([])

    def row_checker(self) -> None:
        for row in self.board:
            num_list = []
            for element in row:
                if isinstance(element.element, int):
                    num_list.append(element.element)
            for element in row:
                if element.element == '':
                    for val in num_list:
                        element.remove_possibilities(val)

    def block_checker(self) -> None:
        blocks = BoardAsBlock(self)
        for block in blocks.blocks:
            block.remove_possibilities([])

    def clear_board(self) -> None:
        for row in self.board:
            for element in row:
                if element.element == '' and len(element.get_possibilities()) == 1:
                    element.element = element.get_possibilities()[0]
                    element.set_possibilities()

    def clear_board2(self) -> None:
        blocks = BoardAsBlock(self)
        cols = BoardAsCol(self)
        for col in cols.Columns:
            col.cells_possibility_sorted()
        self.col_checker()
        self.block_checker()
        self.row_checker()
        for block in blocks.blocks:
            block.cells_possibility_sorted()
        self.col_checker()
        self.block_checker()
        self.row_checker()
        ret_lst = []
        for val in range(9):
            temp_lst = []
            for row in self.board:
                for element in row:
                    if element.element == '' and (val+1) in element.get_possibilities():
                        temp_lst.append(element)
            ret_lst.append(temp_lst[:])
        for i in range(9):
            if len(ret_lst[i]) == 1:
                ret_lst[i][0].element = i + 1
                ret_lst[i][0].set_possibilities()

    def get_row_col(self, cell: UnitCell) -> Tuple:
        for i in range(9):
            for j in range(9):
                if self.board[i][j] is cell:
                    return (i, j)
class BoardAsCol:
    """
    represents the entire board as a set of columns
    Attributes

    Columns: List
    """
    def __init__(self, board: SudokuBoard) -> None:
        self.Columns = [[], [], [], [], [], [], [], [], []]
        for col in range(9):
            temp_col = []
            for row in range(9):
                temp_col.append(board.board[row][col])
            self.Columns[col] = Column(temp_col)


class Column:
    """
    class representing a single column
    """
    def __init__(self, col: List[UnitCell]) -> None:
        self.column = col[:]

    def remove_possibilities(self, values: List[int]) -> None:
        values = self.values_in_col()
        for element in self.column:
            if element.element == '':
                for value in values:
                    element.remove_possibilities(value)

    def values_in_col(self) -> List[int]:
        ret_lst = []
        for element in self.column:
            if isinstance(element.element, int):
                ret_lst.append(element.element)
        return ret_lst

    def cells_possibility_sorted(self) -> None:
        ret_lst = []
        for val in range(9):
            temp_lst = []
            for element in self.column:
                if element.element == '' and (val+1) in element.get_possibilities():
                    temp_lst.append(element)
            ret_lst.append(temp_lst[:])
        for i in range(9):
            if len(ret_lst[i]) == 1:
                ret_lst[i][0].element = i+1
                ret_lst[i][0].set_possibilities()


class BoardAsBlock:
    """
    represents the entire board as 9 blocks.

    Attributes
    Blocks: List[Block]
    """
    def __init__(self, board: SudokuBoard) -> None:
        self.blocks = board_to_block(board)


class Block:
    """
    class represening a block of the board 3x3

    """
    def __init__(self, cells: List[UnitCell], board: SudokuBoard) -> None:
        self.board = board
        self.block = []
        self.block.append([cells[0], cells[1], cells[2]])
        self.block.append([cells[3], cells[4], cells[5]])
        self.block.append([cells[6], cells[7], cells[8]])

    def remove_possibilities(self, values: List[int]) -> None:
        values = self.values_in_block()
        for row in self.block:
            for element in row:
                if element.element == '':
                    for value in values:
                        element.remove_possibilities(value)

    def values_in_block(self) -> List[int]:
        ret_lst = []
        for row in self.block:
            for element in row:
                if isinstance(element.element, int):
                    ret_lst.append(element.element)
        return ret_lst

    def cells_possibility_sorted(self) -> None:
        ret_lst = []
        for val in range(9):
            temp_lst = []
            for row in self.block:
                for element in row:
                    if element.element == '' and (val+1) in element.get_possibilities():
                        temp_lst.append(element)
            ret_lst.append(temp_lst[:])
        for i in range(9):
            if len(ret_lst[i]) == 1:
                ret_lst[i][0].element = i+1
                ret_lst[i][0].set_possibilities()
                self.board.col_checker()
                self.board.block_checker()
                self.board.row_checker()
            elif len(ret_lst[i]) == 2:
                tup1 = self.board.get_row_col(ret_lst[i][0])
                tup2 = self.board.get_row_col(ret_lst[i][1])
                if tup1[0] == tup2[0]:
                    row = self.board.board[tup1[0]]
                    for element in row:
                        if element is not ret_lst[i][0] and element is not ret_lst[i][1]:
                            element.remove_possibilities(i+1)
                    self.board.clear_board()
                    self.board.col_checker()
                    self.board.block_checker()
                    self.board.row_checker()
                elif tup1[1] == tup2[1]:
                    cols = BoardAsCol(self.board)
                    col = cols.Columns[tup1[1]]
                    for element in col.column:
                        if element is not ret_lst[i][0] and element is not ret_lst[i][1]:
                            element.remove_possibilities(i+1)
                    self.board.clear_board()
                    self.board.col_checker()
                    self.board.block_checker()
                    self.board.row_checker()
            elif len(ret_lst[i]) == 3:
                tup1 = self.board.get_row_col(ret_lst[i][0])
                tup2 = self.board.get_row_col(ret_lst[i][1])
                tup3 = self.board.get_row_col(ret_lst[i][2])
                if tup1[0] == tup2[0] == tup3[0]:
                    row = self.board.board[tup1[0]]
                    for element in row:
                        if element is not ret_lst[i][0] and element is not ret_lst[i][1] and element is not ret_lst[i][2]:
                            element.remove_possibilities(i+1)
                    self.board.clear_board()
                    self.board.col_checker()
                    self.board.block_checker()
                    self.board.row_checker()
                elif tup1[1] == tup2[1] == tup3[1]:
                    cols = BoardAsCol(self.board)
                    col = cols.Columns[tup1[1]]
                    for element in col.column:
                        if element is not ret_lst[i][0] and element is not ret_lst[i][1] and element is not ret_lst[i][2]:
                            element.remove_possibilities(i+1)
                    self.board.clear_board()
                    self.board.col_checker()
                    self.board.block_checker()
                    self.board.row_checker()


def board_to_block(board : SudokuBoard) -> List[Block]:
    block_List = [[], [], [], [], [], [], [], [], []]
    block_List[0] = Block([board.board[0][0], board.board[0][1], board.board[0][2], board.board[1][0], board.board[1][1], \
                    board.board[1][2], board.board[2][0], board.board[2][1], board.board[2][2]
                    ], board)
    block_List[1] = Block([board.board[0][3], board.board[0][4], board.board[0][5], board.board[1][3], board.board[1][4], \
                     board.board[1][5], board.board[2][3], board.board[2][4], board.board[2][5]
                     ], board)
    block_List[2] = Block([board.board[0][6], board.board[0][7], board.board[0][8], board.board[1][6], board.board[1][7], \
                     board.board[1][8], board.board[2][6], board.board[2][7], board.board[2][8]
                     ], board)
    block_List[3] = Block([board.board[3][0], board.board[3][1], board.board[3][2], board.board[4][0], board.board[4][1], \
                     board.board[4][2], board.board[5][0], board.board[5][1], board.board[5][2]
                     ], board)
    block_List[4] = Block([board.board[3][3], board.board[3][4], board.board[3][5], board.board[4][3], board.board[4][4], \
                     board.board[4][5], board.board[5][3], board.board[5][4], board.board[5][5]
                     ], board)
    block_List[5] = Block([board.board[3][6], board.board[3][7], board.board[3][8], board.board[4][6], board.board[4][7], \
                     board.board[4][8], board.board[5][6], board.board[5][7], board.board[5][8]
                     ], board)
    block_List[6] = Block([board.board[6][0], board.board[6][1], board.board[6][2], board.board[7][0], board.board[7][1], \
                     board.board[7][2], board.board[8][0], board.board[8][1], board.board[8][2]
                     ], board)
    block_List[7] = Block([board.board[6][3], board.board[6][4], board.board[6][5], board.board[7][3], board.board[7][4], \
                     board.board[7][5], board.board[8][3], board.board[8][4], board.board[8][5]
                     ], board)
    block_List[8] = Block([board.board[6][6], board.board[6][7], board.board[6][8], board.board[7][6], board.board[7][7], \
                     board.board[7][8], board.board[8][6], board.board[8][7], board.board[8][8]
                     ], board)
    return block_List
