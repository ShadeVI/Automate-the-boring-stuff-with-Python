import zombiedice
import random


class RandomChoice:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        while diceRollResults is not None:
            if random.randint(0, 1) == 1:
                diceRollResults = zombiedice.roll()
            else:
                break


class StopsAfterRolledTwoBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class StopsAfterRolledTwoShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break


class OneToFourOrShotgunsIsTwo:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        roll = 1
        rolls = random.randint(1, 4)
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if roll <= rolls and shotguns < 2:
                diceRollResults = zombiedice.roll()
            else:
                break
            roll += 1


class StopsShotgunsMoreThanBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()

        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotguns > brains:
                break
            diceRollResults = zombiedice.roll()


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(
        name='Until 1 Shotgun', minShotguns=1),
    RandomChoice(name='Random Choice'),
    # Add any other zombie players here.
    StopsAfterRolledTwoBrains(name="Stops After Rolled 2 Brains"),
    StopsAfterRolledTwoShotguns(name="Stops After Rolled 2 Shotguns"),
    OneToFourOrShotgunsIsTwo(name="Run 1 - 4 or Stop After 2 Shotguns"),
    StopsShotgunsMoreThanBrains(name="Stop If Shotguns More Than Brains")
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=10000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
