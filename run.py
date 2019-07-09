from util import parse_response
from board import GameBoard
from player import Player

num_players = 2
rounds = 2

print("You will be playing {} rounds. The lower score wins! Good Luck!".format(rounds))

for _ in range(num_players):
    Player()

response = raw_input("How large would you like your grid? Please type two comma seperated numbers.\n")

height, width = parse_response(response)

board = GameBoard(height, width)

for _ in range(rounds):
    board.print_board()
    player_1 = Player.players[0]
    player_2 = Player.players[1]

    board.set_gold(player_1.hide_gold(board))
    player_2.take_turn(board)

    board.set_gold(player_2.hide_gold(board))
    player_1.take_turn(board)

print("Player 1's score was {}. Player 2's score was {}".format(player_1.score, player_2.score))

if player_1.score < player_2.score:
    print("Player 1 wins!")
elif player_2.score < player_1.score:
    print("Player 2 wins!")
else:
    print("It's a draw!")
