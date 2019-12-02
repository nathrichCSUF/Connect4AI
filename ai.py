import copy
from board import Board
class AI:
    def minimax(self, board, depth, bestVal, minVal, isMaxiPlayer):
        val = 0
        col = 0
        r = 0
        # score = self.evalFunction()
        # print("Depth: " + str(depth))
        # print("Score: " + str(score))
        # if score == 1000:
        #     print("My turn to win!")
        #     return self.optMoveRow
        # elif score == -1000:
        #     print("Player Winning Move is being Blocked by AI")
        #     return self.optMoveRow
        #
        # placeholder = 0
        validLocations = board.getValidLocations()
        is_gameTerminal = board.gameFinished()
        if depth == 0 or is_gameTerminal:
            if is_gameTerminal:
                if board.check_win():
                    if board.turn is self.board.turn:
                        return (None, 10000000)
                else:
                    return (None, 0)
            else:
                return (None, board.score_position(board))

        # for i in range(6):
        #     for j in range(7):
        #         if self.grid[i][j].state is "black":
        #             minValueRow[placeholder] = i
        #             minValueCol[placeholder] = j
        #             placeholder = placeholder + 1
        #             break
        # print("\nRecursive\n")
        if isMaxiPlayer:
            print("Entering Maxi Player Loop")
            highestVal = -1000
            print("7th Col State: " + str(board.grid[0][6].state))
            for i in range(len(validLocations)):
                r = board.obtainNextAvailRow(i)
                selfCopy = copy.copy(board)
                selfCopy.grid[r][i].state = board.turn
                value = self.minimax(selfCopy, (depth - 1), bestVal, minVal, False)[1]
                if value > highestVal:
                    highestVal = value
                    col = i
                bestVal = max(bestVal, highestVal)
                if bestVal >= minVal:
                    break
                return col,highestVal

            # for i in range(7):
            #     print("Available Spot: [" + str(minValueRow[i]) + "," + str(minValueCol[i]) + "]")
            # placeholder = 0
            # for i in range(7):
            #         if self.grid[minValueRow[i]][minValueCol[i]].state is "black":
            #             self.button_position = minValueRow[i]
            #             if self.check_valid_move():
            #                 self.grid[minValueRow[i]][minValueCol[i]].state = self.turn
            #                 if(depth < 2):
            #                     print("Thinking for Spot: " + str(i) + " " + str(j))
            #                     bestVal = max(bestVal, self.minimax(depth-1, False))
            #                     print("I reset the slot?\n")
            #                     val = i
            #                 self.grid[minValueRow[i]][minValueCol[i]].state = "black"
            # return minValueRow[i]
            # print("Val: " + str(bestVal))

        else:
            print("Entering Mini Player Lopp")
            highestVal = 1000
            col = 0
            # placeholder = 0
            # for i in range(7):
            #     print("Available Spot: [" + str(minValueRow[i]) + "," + str(minValueCol[i]) + "]")

            for i in range(len(validLocations)):
                r = board.obtainNextAvailRow(i)
                selfCopy = copy.copy(board)
                selfCopy.grid[r][i].state = board.turn
                value = self.minimax(selfCopy, (depth - 1), bestVal, minVal, True)[1]
                if value < highestVal:
                    highestVal = value
                    col = i
                minVal = min(highestVal, minVal)
                if bestVal >= minVal:
                    break
                return col, highestVal
                # self.grid[i][j].state = self.turn
                # if self.grid[minValueRow[i]][minValueCol[i]].state is "black":
                #     self.button_position = minValueRow[i]
                #     if self.check_valid_move():
            #                 if(depth < 2):
            #                     print("Thinking for Spot: " + str(i) + " " + str(j))
            #                     bestVal = min(bestVal, self.minimax(depth-1, True))
            #                     print("I reset the value\n")
            #                     val = i
            #                 self.grid[minValueRow[i]][minValueCol[i]].state = "black"
            #             else:
            #                 break
            # return minValueRow[i]
            # print("Val: " + str(bestVal))