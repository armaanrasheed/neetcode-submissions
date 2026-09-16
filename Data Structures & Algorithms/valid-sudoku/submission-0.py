class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
                
        #row validity check
        for row in range(9):
            rowSet = set()
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in rowSet):
                    return False
                else:
                    rowSet.add(board[row][col])
        
        #col validity check

        #i would need someway to validate if im checking the correct quadrant of col using //3
        for col in range(9):
            colSet = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if (board[row][col] in colSet):
                    return False
                else:
                    colSet.add(board[row][col])
        

        # 3x3 validity
        # for this one, i need to just have a set where i can insert
        # all the numbers of the 3x3 from 1-9 into the set and
        # ensure validity

        for square in range(9):
            squareSet = set()
            for row in range(3):
                for col in range(3):
                    rowSquare = (square//3) * 3 + row
                    colSquare = (square % 3) * 3 + col
                    if board[rowSquare][colSquare] == ".":
                        continue
                    if board[rowSquare][colSquare] in squareSet:
                        return False
                    else:
                        squareSet.add(board[rowSquare][colSquare])

        return True