import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        shotguns = 0
        times = 1
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotguns']

            # LEAVE ONLY ONE BOT CHOICE UNCOMMENTED TO TRY IT OUT

            # A bot that, after the first roll, randomly decides if it will continue or stop
            if random.randint(0, 1) == '0':
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break

            # A bot that stops rolling after it has rolled two brains
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

            # A bot that stops rolling after it has rolled two shotguns
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

            # A bot that initially decides it’ll roll the dice one to four times,
            # but will stop early if it rolls two shotguns
            if times < 4:
                if shotguns < 2:
                    diceRollResults = zombiedice.roll()  # roll again
                    times += 1
                else:
                    break

            # A bot that stops rolling after it has rolled more shotguns than brains
            if brains > shotguns:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)
