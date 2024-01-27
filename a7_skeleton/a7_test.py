# a7_test.py
# Prof. Bracy, AWB93
# Mar 10, 2023

import cornellasserts as ca
import inspect  # to print the name of a (test) function that is running

import a7, dice, a6, printer

# helper written by Prof. Lee, LJL2
def print_testing(start_or_end):
    """If start_or_end is 'start',
        print message about starting function that called this function
       If start_or_end is 'end'
        print message about ending function that called this function

    Precondition: start_or_end is either 'start' or 'end'"""
    caller = inspect.currentframe().f_back.f_code.co_name
    if start_or_end == 'start':
        print("Starting " + caller)
    elif start_or_end == 'end':
        print(caller + " seems to have passed (didn't crash/stop mid-way).")
        print("\n")

def test_a_hand(value_list, category, expected):
    """ This is a helper function that we strongly encourage you to use
    and even more strongly encourage you NOT TO MODIFY.

    Please look at how this function is called in the examples below.

    value_list: [int list] of the 5 dice you want in your hand
    category:   [int] a number from 0 to 12 (CHANCE to YAHTZEE) indicating
                     how you would like to categorize that hand
    expected:   [int] the score this hand earns in this category
    """
    error_msg = "failed test: " +str(value_list)+ ", " +str(category)+ ", "+\
        str(expected)+" @ line "+str(inspect.currentframe().f_back.f_lineno)

    sc = a7.Scorecard()
    dice_list = []
    for n in value_list:
        dice_list.append(dice.Die(n))
    hand = a6.Hand(a7.Rules.NUM_DICE, dice_list)
    if sc.categories[category] != None:
        sc.categories[category].score(hand)
    else:
        cat_msg = str(category)+" (\'"+a7.Rules.names[category]+"\')"
        ca.quit_with_error("Scorecard @ index " +cat_msg+ " is None. \n"+\
        "Cannot test this category until it is properly initialized.\n" +\
        "See Scorecard __init__() method in a7.py\n"+error_msg)

    points = sc.categories[category].points
    print(points)
    error_msg += f"\nexpected score: {expected}\ncomputed score: {points}\n"
    ca.assert_equals(expected, points, error_msg)

# ---------------------------------------------------------
# SOME test code for you A7 is below.
# You are encouaged to add more test cases.
# ---------------------------------------------------------

def test_ones():
    print_testing('start')
    # [1,1,1,4,5] as Ones should yield 3 points
    test_a_hand([1,1,1,4,5], a7.Rules.ONES, 3)
    # [1,3,4,5,1,2] as Ones should yield 2 points
    test_a_hand([1,3,4,5,1], a7.Rules.ONES, 2)
    print_testing('end')

def test_twos():
    print_testing('start')
    # [1,1,1,4,5] as Twos should yield 3 points
    test_a_hand([2,2,2,4,5], a7.Rules.TWOS, 6)
    # [1,3,4,5,1,2] as Twos should yield 2 points
    test_a_hand([2,3,4,5,2], a7.Rules.TWOS, 4)
    # [9,3,4,5,1] as Twos should yield 0 points
    test_a_hand([6,3,4,5,1], a7.Rules.TWOS, 0)


def test_threes():
    print_testing('start')
    # [1,1,1,4,5] as Ones should yield 3 points
    test_a_hand([3,3,3,4,5], a7.Rules.THREES, 9)
    # [1,3,4,5,1,2] as Ones should yield 2 points
    test_a_hand([3,3,4,3,3], a7.Rules.THREES, 12)

def test_fours():
    print_testing('start')
    # [1,1,1,4,5] as Ones should yield 3 points
    test_a_hand([4,4,4,4,5], a7.Rules.FOURS, 16)
    # [1,3,4,5,1,2] as Ones should yield 2 points
    test_a_hand([1,3,4,4,1], a7.Rules.FOURS, 8)

def test_fives():
    print_testing('start')
    # [1,1,1,4,5] as Ones should yield 3 points
    test_a_hand([1,1,1,4,5], a7.Rules.FIVES, 5)
    # [1,3,4,5,1,2] as Ones should yield 2 points
    test_a_hand([1,5,4,5,1], a7.Rules.FIVES, 10)

def test_sixes():
    print_testing('start')
    # [1,1,1,4,5] as Ones should yield 3 points
    test_a_hand([1,1,1,4,5], a7.Rules.SIXES, 0)
    # [1,3,4,5,1,2] as Ones should yield 2 points
    test_a_hand([1,6,4,6,6], a7.Rules.SIXES, 18)

def test_3ofakind():
    print_testing('start')
    # [1,1,1,2,1] as Three of a Kind should yield 6 points
    test_a_hand([1,1,1,2,1], a7.Rules.THREE_OF_A_KIND, 6)
    # [2,4,1,2,1] as Three of a Kind should yield 0 points
    test_a_hand([2,4,1,2,1], a7.Rules.THREE_OF_A_KIND, 0)
    # [4,4,4,4,4] as Three of a Kind should yield 20 points
    test_a_hand([4,4,4,4,4], a7.Rules.THREE_OF_A_KIND, 20)
    # [4,5,4,2,4] as Three of a Kind should yield 20 points
    test_a_hand([4,5,4,2,4], a7.Rules.THREE_OF_A_KIND, 19)
    print_testing('end')

def test_4ofakind():
    print_testing('start')
    # [1,1,1,2,1] as Four of a Kind should yield 6 points
    test_a_hand([1,1,1,2,1], a7.Rules.FOUR_OF_A_KIND, 6)
    # [2,1,1,2,1] as Four of a Kind should yield 0 points
    test_a_hand([2,1,1,2,1], a7.Rules.FOUR_OF_A_KIND, 0)
    # [4,4,4,4,4] as Four of a Kind should yield 20 points
    test_a_hand([4,4,4,4,4], a7.Rules.FOUR_OF_A_KIND, 20)
    # [4,4,4,4,0] as Four of a Kind should yield 16 points
    test_a_hand([4,4,4,4,1], a7.Rules.FOUR_OF_A_KIND, 17)
    print_testing('end')

def test_full_house():
    print_testing('start')
    # [1,1,1,2,1] as Full House should yield 0 points
    test_a_hand([1,1,1,2,1], a7.Rules.FULL_HOUSE, 0)
    # [2,1,1,2,1] as Full House should yield 25 points
    test_a_hand([2,1,1,2,1], a7.Rules.FULL_HOUSE, a7.Rules.FULL_HOUSE_PTS)
    # [4,4,4,4,4] as Full House should yield 0 points
    test_a_hand([4,4,4,4,4], a7.Rules.FULL_HOUSE, 0)
    print_testing('end')

def test_small_straight():
    print_testing('start')
    # [1,1,1,2,1] as Small Straight should yield 0 points
    test_a_hand([1,1,1,2,1], a7.Rules.SM_STRAIGHT, 0)
    # [2,4,3,2,1] as Small Straight should yield 30 points
    test_a_hand([2,4,3,2,1], a7.Rules.SM_STRAIGHT, a7.Rules.SM_STRAIGHT_PTS)
    # [1,5,2,3,4] as Small Straight should yield 30 points
    test_a_hand([1,5,2,3,4], a7.Rules.SM_STRAIGHT, a7.Rules.SM_STRAIGHT_PTS)
    print_testing('end')

def test_large_straight():
    print_testing('start')
    # [1,1,1,2,1] as Large Straight should yield 0 points
    test_a_hand([6,6,6,6,6], a7.Rules.LG_STRAIGHT, 0)
    # [2,4,3,2,1] as Large Straight should yield 40 points
    test_a_hand([2,4,3,5,1], a7.Rules.LG_STRAIGHT, a7.Rules.LG_STRAIGHT_PTS)
    # [1,5,2,3,4] as Large Straight should yield 40 points
    test_a_hand([1,5,2,3,4], a7.Rules.LG_STRAIGHT, a7.Rules.LG_STRAIGHT_PTS)
    print_testing('end')

def test_yahtzee():
    print_testing('start')
    #[4,4,4,4,4] as Yahtzee should yield 50 points
    test_a_hand([4,4,4,4,4], a7.Rules.YAHTZEE, 50)
    #[1,2,3,4,5] as Yahtzee should yield 0 points
    test_a_hand([1,2,3,4,5], a7.Rules.YAHTZEE, 0)
    #[1,1,1,1,1] as Yahtzee should yield 50 points
    test_a_hand([1,1,1,1,1], a7.Rules.YAHTZEE, 50)
    print_testing('end')
if __name__ == '__main__':

    # you can turn printing back on if you want to see the dice,
    # but we kind of liked testing with the dice turned off....
    printer.print_f = False

    # STUDENTS: You should test all 13 categories. We've done 4 for you.
    # test_chance()
    # ...
    # test_ones()
    # test_twos()
    # test_threes()
    # test_fours()
    # test_fives()
    # test_sixes()
    # test_3ofakind()
    # test_4ofakind()
    # test_full_house()
    # test_small_straight()
    # test_large_straight()
    test_yahtzee()
