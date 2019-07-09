class GameBoard:

    def __init__(self, height, width):
        self.grid = self.create_board(height, width)
        self.height = int(height)
        self.width = int(width)
        self.locations = {}
        self.gold_remaining = 0

    def create_board(self, height, width):
        grid = []
        for _ in range(int(height)):
            grid.append(['O']*int(width))
        return grid

    def get_area(self):
        return self.height * self.width

    def print_board(self):
        for x in self.grid:
            print(x)
        print("\n")
        
    def set_gold(self, locations):
        self.gold_remaining = len(locations)
        for location in locations:
            self.locations[location] = True

    def update_board(self, guess):
        if self.grid[int(guess[1])-1][int(guess[0])-1] == "X":
            player_guess = raw_input("That space has already been dug! Please select a valid location as a comma seperated pair (Coloumn,Row), then hit enter.\n")
            parsed_guess = parse_response(player_guess)
            self.update_board(parsed_guess)

        self.grid[int(guess[1])-1][int(guess[0])-1] = "X"
        self.print_board()

    def reset_board(self):
        self.grid = self.create_board(self.height, self.width)
        self.locations = {}
        self.gold_remaining = 0
