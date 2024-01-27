# a7.py
# PUT YOUR NETID(S) HERE
# Sources/people consulted: FILL IN OR WRITE "NONE"
# PUT DATE YOU COMPLETED THIS HERE
# Skeleton by Prof. Bracy, AWB93, April, 2023

import dice, a6

class Rules():
    """A class to store some of the basic assumptions and rules of the game."""

    NUM_DICE = 5

    # numbers for each of the 13 categories
    CHANCE = 0
    ONES = 1
    TWOS = 2
    THREES = 3
    FOURS = 4
    FIVES = 5
    SIXES = 6
    THREE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 8
    FULL_HOUSE = 9
    SM_STRAIGHT = 10
    LG_STRAIGHT = 11
    YAHTZEE = 12
    NUM_CATEGORIES = 13

    """
    Remember it is bad form to have `magic numbers` in your code.  Instead,
    you can create a variable whose name offers a meaningful description of
    what that number is. Here are some constants below that we want you to use.
    """
    FULL_HOUSE_PTS = 25
    SM_STRAIGHT_PTS = 30
    LG_STRAIGHT_PTS = 40
    YAHTZEE_PTS = 50

    # STUDENTS: if you want to make your own constants/variables, create
    # your new class attributes here:

    # STUDENTS: Notice that
    # CHANCE has the value 0 above, and CHANCE goes in location [0]
    names = ["Chance", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",\
             "3 of a kind", "4 of a kind", "Full House", "Small Straight",\
             "Large Straight", "Yahtzee (5x!)"]

    # STUDENTS: Notice that
    # CHANCE has the value 0 above,   and CHANCE  goes in location [0]
    # ...
    # YAHTZEE has the value 12 above, and YAHTZEE goes in location [12]
    descriptions = [" -- sum all 5 dice ",
                    "   -- sum 1s only    ",
                    "   -- sum 2s only    ",
                    " -- sum 3s only    ",
                    "  -- sum 4s only    ",
                    "  -- sum 5s only    ",
                    "  -- sum 6s only    ",
                    " -- sum all 5 ",
                    " -- sum all 5 ",
                    "     -- "+str(FULL_HOUSE_PTS)+" pts ",
                    " -- "+str(SM_STRAIGHT_PTS)+" pts",
                    " -- "+str(LG_STRAIGHT_PTS)+" pts",
                    "  -- "+str(YAHTZEE_PTS)+" pts"]

# STUDENTS: do not modify Basic!
class Basic():
    """Basic is the simplest way to score a hand in Yahtzee.
    Any 5-dice hand meets the criteria to count for Basic.
    The score is the sum of the values of all the dice in the hand.
    """

    def __init__(self, index):
        """Creates an instance of a Basic with the following attributes:

        index:      [int] which scorecard entry this is associated with
        is_filled:  [bool] whether a hand has been assigned to this Basic
                    (this is always False in the beginning)
        points:     [int] once a hand as been associated with this category,
                    the points attribute will reflect the score
        max_points: [int] the best score one can get with this category. this
                    field will be used for the scoreboard to let users know
                    how many points they stand to earn under this category

        Precondition: 0 <= index [int] <= Rules.YAHTZEE
        """
        assert index >= 0, "index must be a positive integer"
        assert index <= Rules.YAHTZEE, \
            "index must be no larger than"+str(Rules.YAHTZEE)
        self.index = index
        self.is_filled = False
        self.points = 0
        self.max_points = Rules.NUM_DICE * dice.Die.NUM_SIDES

    def score(self, hand):
        """When Basic is scored, simply sum the value of all dice in the hand.
        Also mark the category as filled. Each category can only be used once.
        """
        self.points = hand.score()
        self.is_filled = True

    def __str__(self):
        """This method should be sufficient for this class and any of its
        subclasses."""
        end = "/"+str(self.max_points)+"]"
        if not self.is_filled:
            scoretext = " [ "+end
        else:
            scoretext = " ["+str(self.points)+end
        return str(self.index) + ": "+ Rules.names[self.index]+\
            Rules.descriptions[self.index] + scoretext

# STUDENTS: if you create any new classes, add them here.
class Single(Basic):
    """This class scores the ONEs, TWOs...SIXes categories and fills out the
    Scorecard categories"""

    def __init__(self, index):
        """Initializes the variables for the calculations that will be done
        in this class. Sets the index variable and the sets the max points possible
        for this categorization """
        super().__init__(index)
        self.max_points = self.index * Rules.NUM_DICE


    def score(self, hand):
        """Scores this hand based on the index that this object is initialized as
        [Index will be between 1-6]
        """
        hand_list = hand.get_dice()
        score = 0
        if self.index == 1:
            for die in hand_list:
                if die.value == 1:
                    score += die.value
        elif self.index == 2:
            for die in hand_list:
                if die.value == 2:
                    score += die.value
        elif self.index == 3:
            for die in hand_list:
                if die.value == 3:
                    score += die.value
        elif self.index == 4:
            for die in hand_list:
                if die.value == 4:
                    score += die.value
        elif self.index == 5:
            for die in hand_list:
                if die.value == 5:
                    score += die.value
        else:
            for die in hand_list:
                if die.value == 6:
                    score += die.value
        self.points = score
        self.is_filled = True

class OfAKind(Basic):
    """This class scores the ONEs, TWOs...SIXes categories and fills out the
    Scorecard categories"""

    def __init__(self, index):
        """Initializes the variables for the calculations that will be done
        in this class. Sets the index variable and the sets the max points possible
        for this categorization """
        super().__init__(index)
        self.max_points = dice.Die.NUM_SIDES * Rules.NUM_DICE

    def score(self, hand):
        """Scores the THREE_OF_A_KIND and FOUR_OF_A_KIND categories
        based on the index chosen [Index will be either 7-8]
        """
        score = 0
        exist = {}
        hand_list = hand.get_dice()
        """Puts all the Die values in the 'Hand' object (hand) in the
        dictionary (exist) """
        for die in hand_list:
            if die.value not in exist:
                exist[die.value] = 1
            else:
                exist[die.value] += 1

        """Checks to see if the 'index' is either 7 or 8. If it is either,
        confirms that in the dictionary 'exist' a key has a value of
        at least 3 or greater and then adds all of the die values in the
        hand to the score"""
        if self.index == 7:
            for key, value in exist.items():
                if value >= 3:
                    for die in hand_list:
                        score += die.value
        elif self.index == 8:
            for key, value in exist.items():
                if value >= 4:
                    for die in hand_list:
                        score += die.value
        self.points = score
        self.is_filled = True

class Special(Basic):
    """This class scores the ONEs, TWOs...SIXes categories and fills out the
    Scorecard categories"""

    def __init__(self, index):
        """Initializes the variables for the calculations that will be done
        in this class. Sets the index variable and the sets the max points possible
        for this categorization """
        super().__init__(index)
        self.max_points = 50

    def score(self, hand):
        """Scores the FULL_HOUSE, SM_STRAIGHT, LG_STRAIGHT and Yahtzee
        [Index will be between 9-10 included]
        """
        score = 0
        exist = {}
        freq = []
        hand_list = hand.get_dice()
        """Adds all the Die values in 'hand' [Hand object] into the exist
        dictionary with the frequencies of how many times they appear in the
        hand"""
        for die in hand_list:
            if die.value not in exist:
                exist[die.value] = 1
            else:
                exist[die.value] += 1

        """For each key and value in the 'exist' Die dictionary, appends the
        frequency of each key into the 'freq list'"""
        for key, value in exist.items():
            freq.append(value)

        """Depending on index, compares the frequency to see if each category
        condition is satisfied. FULL_HOUSE = [2,3], SM_STRAIGHT = [1,1,1,2],
        LG_STRAIGHT = [1,1,1,1,1] and YAHTZEE = [5]. Adds the corresponding max_points
        depending on the category. """
        if self.index == 9:
            if [2,3] == sorted(freq):
                score += 25
            else:
                score = 0
        elif self.index == 10:
            if [1,1,1,2] == sorted(freq) or [1,1,1,1,1] == sorted(freq0):
                score += 30
            else:
                score = 0
        elif self.index == 11:
            if [1,1,1,1,1] == sorted(freq):
                score += 40
            else:
                score = 0
        else:
            if [5] == sorted(freq):
                score += 50
            else:
                score = 0
        self.points = score
        self.is_filled = True

class Scorecard():
    """The scorecard tells you what categories there are, what points can be
    earned, which ones have been filled, and what your total score is so far.
    """

    def __init__(self):
        """
        Instance attributes:
          total_score: [int] tells you how  many points have been earned
          categories: [list of Basic] there are 13 categories in the game
                  and this list keeps track of each of them
        """
        self.total_score = 0
        self.categories = [None]*Rules.NUM_CATEGORIES
        self.categories[Rules.CHANCE] = Basic(Rules.CHANCE)
        self.categories[Rules.ONES] = Single(Rules.ONES)
        self.categories[Rules.TWOS] = Single(Rules.TWOS)
        self.categories[Rules.THREES] = Single(Rules.THREES)
        self.categories[Rules.FOURS] = Single(Rules.FOURS)
        self.categories[Rules.FIVES] = Single(Rules.FIVES)
        self.categories[Rules.SIXES] = Single(Rules.SIXES)
        self.categories[Rules.THREE_OF_A_KIND] = OfAKind(Rules.THREE_OF_A_KIND)
        self.categories[Rules.FULL_HOUSE] = Special(Rules.FULL_HOUSE)
        self.categories[Rules.SM_STRAIGHT] = Special(Rules.SM_STRAIGHT)
        self.categories[Rules.LG_STRAIGHT] = Special(Rules.LG_STRAIGHT)
        self.categories[Rules.YAHTZEE] = Special(Rules.YAHTZEE)
        # STUDENTS: does Basic meet the needs of the Chance Category?
        # if so, categories[0] is complete.
        # You will need to append 12 more categories to this scorecard.
        # If you wanted 12 more Basic's you would do this:
        # self.categories[Rules.ONES] = Basic(Rules.ONES)
        # ...
        # self.categories[Rules.YAHTZEE] = Basic(Rules.YAHTZEE)
        # You can change the class that you create, but do not change
        # the index or your game will not function properly.
        # The next 12 lines of code should be the ONLY lines you need to add
        # to the Scorecard class. Everything else has been done for you.

    # --------- STUDENTS: Do not modify any of the code below ---------


    def cat_prompt(self):
        print(self)
        print("How would you like to categorize these dice?")

    def set_hand(self, hand, choice):
        """Associates a hand with one of the game categories."""
        self.categories[choice].score(hand)
        s = self.categories[choice].points
        print("You just earned "+str(s)+" points!\n")
        self.total_score += s

    def __str__(self):
        """Prints out the scorecard, one category (row) at a time."""
        result = ""
        for c in self.categories:
            result += str(c)+"\n"
        return result

    def choice_okay(self, choice):
        """
        Makes the game more usable by not letting the user select a category
        that has already been chosen or that is not valid.
        """
        if not choice.isnumeric():
            print("Please enter a number.")
            return False
        choice = int(choice)
        if (choice < 0):
            print("category index must be a positive integer.")
            return False
        if (choice > Rules.YAHTZEE):
            print("The largest category index in Yahtzee is "+str(Rules.YAHTZEE))
            return False
        if (self.categories[choice] == None):
            print("This category has not been implemented yet.")
            return False
        if (self.categories[choice].is_filled):
            print("That category has already been filled.")
            return False
        return True

    def get_choice(self):
        """Prompts the user to pick a category that they wish apply
        their current hand to.
        """
        choice = input("Your choice: ")
        while(not self.choice_okay(choice)):
            choice = input("Your choice: ")
        return int(choice)

def get_hand():
    """Rolls the dice and allows the user to re-roll up to 2 more times."""
    print("Rolling the dice...")
    hand = a6.Hand(Rules.NUM_DICE)
    if hand.initiate_reroll():
        hand.initiate_reroll()
    return hand

if __name__=='__main__':
    sc = Scorecard()
    print("Welcome to Yahtzee!")
    print(sc)
    n_turns = Rules.NUM_CATEGORIES - sc.categories.count(None)

    while (n_turns > 0):
        print("You have "+str(n_turns)+" rolls left.")
        hand = get_hand()
        sc.cat_prompt()
        choice = sc.get_choice()
        sc.set_hand(hand, choice)
        print(sc)
        print("Current score = "+str(sc.total_score))
        print("--------------------------------------------")
        n_turns -= 1

    print("FINAL SCORE = "+str(sc.total_score)+"\nThanks for playing!")
