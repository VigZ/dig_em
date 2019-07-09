from util import parse_response

class Player:
    players = []

    def __init__(self, gold_to_hide=3):
        self.score = 0
        self.gold_to_hide = gold_to_hide
        Player.players.append(self)
        self.player_id = len(Player.players)

    def hide_gold(self, board):
        locations = []
        for x in range(self.gold_to_hide):
            print("You have {} gold to hide remaining.\n".format(self.gold_to_hide - x))
            hiding_location = raw_input("It's player {}'s turn to hide their gold! Enter your location as a comma separated pair (Coloumn,Row), then hit enter.\n".format(self.player_id))
            if int(parse_response(hiding_location)[0]) > board.height or int(parse_response(hiding_location)[0]) > board.width or int(parse_response(hiding_location)[1]) > board.height or int(parse_response(hiding_location)[1]) > board.width:
                print("The hiding location must be on the board. Please re-enter your combination")
                self.hide_gold(board)
            locations.append(hiding_location)
        return locations

    def take_turn(self, board):
        board.print_board()

        while(self.score < board.get_area() and board.gold_remaining > 0 ):
            player_guess = raw_input("It's player {}'s turn to hunt for gold! Please select a location as a comma seperated pair (Coloumn,Row), then hit enter.\n".format(self.player_id))
            parsed_guess = parse_response(player_guess)
            if player_guess in board.locations:
                board.gold_remaining -= 1
                print("You found a piece of gold! There are {} remaining!\n".format(board.gold_remaining))
            board.update_board(parsed_guess)
            self.score += 1

        board.reset_board()
        board.print_board()
