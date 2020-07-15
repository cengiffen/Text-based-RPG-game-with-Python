class Player:
    def __init__(self):
        self.fear_level = 5
        self.love_level = 5
        self.inventory = ['Matches', 'Knife', 'Candy', 'Hourglass']

    def show_situation(self):
        input(f"Fear: {self.fear_level*'X' + (10-self.fear_level)*'-'}\nLove: {self.love_level * 'X' + (10 - self.love_level) * '-'}")

    def show_inventory(self):
        input(', '.join(self.inventory))

    def result(self):
        print('...except for love.')
        input(f"Current love = '{self.love_level * 'X' + (10 - self.love_level) * '-'}'")
        print('You have nothing to fear.')
        input(f"Current fear = '{self.fear_level * 'X' + (10 - self.fear_level) * '-'}'")
        if self.fear_level > 5:
            input("You have too much to fear.")
        elif self.fear_level <= 5:
            input("You are brave. Good for you.")
        if self.love_level >= 5:
            input("You have love. Good for you.")
        elif self.love_level < 5:
            input("Your love is too small.")
