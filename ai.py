import copy
from board import Board

class AI:
    def minimax(self, board, depth, bestVal, minVal, isMaxiPlayer):
        val = 0
        col = 0
        r = 0

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
        if isMaxiPlayer:
            # print("Entering Maxi Player Loop")
            highestVal = -1000
            # print("7th Col State: " + str(board.grid[0][6].state))
            for i in validLocations:
                r = board.obtainNextAvailRow(i)
                selfCopy = copy.copy(board)
                selfCopy.grid[r][i].state = board.turn
                value = self.minimax(selfCopy, (depth - 1), bestVal, minVal, False)[1]
                board.grid[r][i].state = "black"
                if value > highestVal:
                    highestVal = value
                    col = i
                bestVal = max(bestVal, highestVal)
                if bestVal >= minVal:
                    break
                return col,highestVal


        else:
            # print("Entering Mini Player Lopp")
            highestVal = 1000
            # placeholder = 0
            # for i in range(7):
            #     print("Available Spot: [" + str(minValueRow[i]) + "," + str(minValueCol[i]) + "]")

            for i in validLocations:
                r = board.obtainNextAvailRow(i)
                selfCopy = copy.copy(board)
                selfCopy.grid[r][i].state = board.turn
                # print("Turn: " + str(board.turn))
                value = self.minimax(selfCopy, (depth - 1), bestVal, minVal, True)[1]
                if value < highestVal:
                    highestVal = value
                    col = i
                minVal = min(highestVal, minVal)
                if bestVal >= minVal:
                    break
                board.grid[r][i].state = "black"
                return col, highestVal