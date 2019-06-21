game_size = 6

"""
for i in range(game_size):
    row = []
    for i in range(game_size):
        row.append(0)
        game.append(row)"""


game_size = input("What size of tic tac toe? ")
game = [[0 for i in range(game_size)] for i in range(game_size)]
print(game)