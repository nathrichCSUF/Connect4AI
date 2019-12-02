import copy
from board import Board

class AI:
    def minimax(self, board, depth, bestVal, minVal, isMaxiPlayer):
        val = 0
        r = 0
        column = 0
        validLocations = board.getValidLocations()
        is_gameTerminal = board.gameFinished()
        if depth == 0 or is_gameTerminal:
            if is_gameTerminal:
                if board.ai_check_win():
                    if board.turn is board.turn:
                        return (None, 1000)
                    elif board.turn is not board.turn:
                        return (None, -1000)
                else:
                    return (None, 0)
            else:
                return (None, board.score_position(board))
        print(validLocations)
        if isMaxiPlayer:
            # print("Entering Maxi Player Loop")
            highestVal = -1000
            # print("7th Col State: " + str(board.grid[0][6].state))
            for col in validLocations:
                r = board.obtainNextAvailRow(col)
                selfCopy = copy.copy(board)
                print("Col: " + str(col))
                selfCopy.grid[r][col].state = board.turn
                value = self.minimax(selfCopy, (depth - 1), bestVal, minVal, False)[1]

                board.grid[r][col].state = "black"
                if value > highestVal:
                    highestVal = value
                    column = col
                print("highestVal: " + str(highestVal))
                # print("col: " + str(col))
                bestVal = max(bestVal, highestVal)
                if bestVal >= minVal:
                    break
                print("Minimax Column: " + str(column))
            return column, highestVal


        else:

            print("Entering Mini Player Lopp")
            highestVal = 1000
            # placeholder = 0
            # for i in range(7):
            #     print("Available Spot: [" + str(minValueRow[i]) + "," + str(minValueCol[i]) + "]")

            for col in validLocations:
                r = board.obtainNextAvailRow(col)
                selfCopy = copy.copy(board)
                selfCopy.grid[r][col].state = board.turn
                # print("Turn: " + str(board.turn))
                value = self.minimax(selfCopy, (depth - 1), bestVal, minVal, True)[1]
                if value < highestVal:
                    highestVal = value
                    column = col
                minVal = min(highestVal, minVal)
                if bestVal >= minVal:
                    break
                board.grid[r][col].state = "black"
            return column, highestVal