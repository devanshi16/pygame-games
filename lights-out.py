def nextMove(player,board):
    x = 0
    for i in board:
        y = 0
        for j in i:
            if j == "1":
                print(x,y)   
                return
            y+=1
        x+=1

player = input()
#The board is a 8x8 array filled with 1 or 0.
board = []
for i in range(8):
    board.append(input())

nextMove(player,board)