class World:
    achievements = {'Rite with the old lady': 'LOCKED',
                    'Beautiful visits': 'LOCKED',
                    'A bad boy': 'LOCKED',
                    'Salvation of a man': 'LOCKED',
                    'Iggy Pop': 'LOCKED',
                    'Groundhog day': 'LOCKED'
                    }
    replays = 0

    @classmethod
    def give(cls, giver, item, receiver):
        giver.inventory.remove(item)
        receiver.inventory.append(item)

    @classmethod
    def choice(cls, prompt: str, valid: list):
        a = str(input(prompt).upper())
        if a not in valid:
            input('This is not doable. Do something doable.')
            return World.choice(prompt, valid)
        else:
            return a
