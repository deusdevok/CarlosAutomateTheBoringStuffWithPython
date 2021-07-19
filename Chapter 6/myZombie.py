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


        
        # 1) AFTER THE FIRST ROLL, RANDOMLY DECIDES IF IT WILL CONTINUE OR STOP
        '''
        while diceRollResults is not None:
            if random.randint(0, 1) == 1:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
        '''

        # 2) ORIGINAL EXAMPLE: STOPS ROLLING AFTER IT HAS ROLLED TWO BRAINS
        '''
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
        '''

        # 3) STOPS ROLLING AFTER IT HAS ROLLED TWO SHOTGUNS
        '''
        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
        '''

        # 4) INITIALLY DECIDES IT'LL ROLL ONE TO FOUR TIMES,
        # BUT WILL STOP EARLY IF IT ROLLS TWO SHOTGUNS
        '''
        shotguns = 0
        rolls = 1
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2 and rolls < 5:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
        '''

        # 5) STOPS ROLLING AFTER IT HAS ROLLED MORE SHOTGUNS THAN BRAINS
        
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']

            if shotguns < brains:
                diceRollResults = zombiedice.roll() # roll again
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
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
