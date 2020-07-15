from world import World


class NonPlayableCharacter:
    def __init__(self):
        self.inventory = []
        self.alive = True
        self.visit = 0


class OldLady(NonPlayableCharacter):
    def __init__(self):
        super().__init__()
        self.name = 'Old Lady'
        self.candle = 0
        self.shook = False
        self.poem = ''

    def give_candle(self):
        self.candle += 1
        input('''For the loved ones, lost ones, the sacred,
The sad ones, the tortured, massacred.''')
        b5 = World.choice('''(G)ive more matches.
(L)eave her be.
Hmm: ''', ['G', 'L'])
        if b5 == 'G':
            self.give_candle()


class PrettyGirl(NonPlayableCharacter):
    def __init__(self):
        super().__init__()
        self.name = 'Pretty Girl'
        self.dance = False


class LittleKid(NonPlayableCharacter):
    def __init__(self):
        super().__init__()
        self.name = 'Little Kid'
        self.good = False

    @property
    def inventory_check(self):
        return 'Matches' in self.inventory and 'Knife' in self.inventory


class AngryMan(NonPlayableCharacter):
    def __init__(self):
        super().__init__()
        self.name = 'Angry Man'
        self.saved = False
        self.reason = False

    @property
    def saved_check(self):
        return 'Candy' in self.inventory and 'Hourglass' in self.inventory
