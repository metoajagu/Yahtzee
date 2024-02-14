# Yahtzee
A replicated Yahtzee game programmed in Python

[School Project Completed at Cornell University]

Instructions:
[Ensure you have Python downloaded on your machine]
1.  Clone the Repository in your terminal [git clone https://github.com/metoajagu/Yahtzee]
2.  Locate the a7_skeleton folder on your machine and go to that repository using your command tools on machine [cd path/to/a7_skeleton]
3.  Run the a7.py file using the python command [python a7.py]
4.  A welcoming message will appear with instructions on how to play the game that looks like this:

                                                         Welcome to Yahtzee!
                                                    0: Chance -- sum all 5 dice  [ /30]
                                                    1: Ones   -- sum 1s only     [ /5]
                                                    2: Twos   -- sum 2s only     [ /10]
                                                    3: Threes -- sum 3s only     [ /15]
                                                    4: Fours  -- sum 4s only     [ /20]
                                                    5: Fives  -- sum 5s only     [ /25]
                                                    6: Sixes  -- sum 6s only     [ /30]
                                                    7: 3 of a kind -- sum all 5  [ /30]
                                                    None
                                                    9: Full House     -- 25 pts  [ /50]
                                                    10: Small Straight -- 30 pts [ /50]
                                                    11: Large Straight -- 40 pts [ /50]
                                                    12: Yahtzee (5x!)  -- 50 pts [ /50]
                                                    
                                                    You have 12 rolls left.
                                                    Rolling the dice...
                                                    .-------..-------..-------..-------..-------.
                                                    | O   O || O   O || O   O || O   O || O   O |
                                                    |       ||   O   ||       ||       ||   O   |
                                                    | O   O || O   O || O   O || O   O || O   O |
                                                    .-------..-------..-------..-------..-------.

                                                    Which dice would you like to re-roll?
                                                    For each die, 0 means keep, 1 means re-roll.
                                                    Press Return for '00000'.
                                                    Your reroll mask: 
5.  The program will roll the dice first when you open it and you have a choice of rerolling or using your current roll to get your score.
6.  To reroll type a reroll mask in the terminal as a set of 0's and 1's to determine which die you would like to reroll, '1' means reroll and '0' means keep.
    Every index of the mask that you type in represents the die you would like to reroll. For example, in the instructions above the first die is represented as the 
    0th element in the reroll mask: '00000' 
7.  Once you enter your reroll mask the program will reroll your die and give you another set of die.
8.  To score your die, press RETURN to keep your die, another instruction message will appear that looks like this:
                                                    
                                                    0: Chance -- sum all 5 dice  [ /30]
                                                    1: Ones   -- sum 1s only     [ /5]
                                                    2: Twos   -- sum 2s only     [ /10]
                                                    3: Threes -- sum 3s only     [ /15]
                                                    4: Fours  -- sum 4s only     [ /20]
                                                    5: Fives  -- sum 5s only     [ /25]
                                                    6: Sixes  -- sum 6s only     [ /30]
                                                    7: 3 of a kind -- sum all 5  [ /30]
                                                    None
                                                    9: Full House     -- 25 pts  [ /50]
                                                    10: Small Straight -- 30 pts [ /50]
                                                    11: Large Straight -- 40 pts [ /50]
                                                    12: Yahtzee (5x!)  -- 50 pts [ /50]
                                                    
                                                    How would you like to categorize these dice?
                                                    Your choice: 
9.   To pick a category simply enter a number that corresponds to the category score your want to apply to your dice. 
10.  To get your ending score, you must fill in a score for each of the 13 categories that at the end will be tallied up to get your final score.
11.  Whoever has the highest score wins the game. 

[Note]: This can be a two player game but requires both players to download the program on their separate systems or you can take turns filling out your scores on one system
        and see who gets the highest score




https://github.com/metoajagu/Yahtzee/assets/157914585/26f839aa-f096-4baa-8604-57a8a357617d


