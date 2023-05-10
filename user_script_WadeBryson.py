"""
Purpose: Calculate basic statistics for a team's points scored.

Author: Wade Bryson

The user will input a team's prior points scored.

The script will produce basic statistics over the user's input.

The script will print an analysis of the statistics.

"""


from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# PART ONE
# User Inputs Game 1 Score - Input is a string
# I added a blank new line to terminal to look cleaner
game1_string = input("\nPlease enter the score for your 1st game: ")

# Convert Game 1 Score from a string to a number
game1 = float(game1_string)

# User Inputs Game 2 Score - Input is a string
game2_string = input("Please enter the score for your 2nd game: ")

#Convert Game 2 Score from a string to a number
game2 = float(game2_string)

# User Inputs Game 3 Score - Input is a string
game3_string = input("Please enter the score for your 3rd game: ")

#Convert Game 3 Score from a string to a number
game3 = float(game3_string)

# PART TWO - Finding Basic Statistics
# Creat functions to help with calculations
number_list = [game1, game2, game3]
length = len(number_list)

# 1. Find the Sum
sum = game1 + game2 + game3
# 2. Find the Average and then round the number to twp decimal places
average = sum / length
nice_average = round(average,2)
# 3. Find the Product
product = game1*game2*game3
#4 Find the Smallest
smallest = min(number_list)
#5 Find the Largest
largest = max(number_list)
#6 Find the Range
range = largest - smallest

#Logging all the information from Part Two
logger.info(f"Below I have a statistical analysis of your first three basketball games.")
logger.info(f"1. Sum = {sum}.")
logger.info(f"2. Average points per game = {nice_average}")
logger.info(f"3. Product = {product}")
logger.info(f"4. Least points scored = {smallest}")
logger.info(f"5. Most points scored = {largest}")
logger.info(F"6. Range = {range}")


# PART THREE - Decision making conditions
# Condition 1 = Range
if range > 10:
    logger.info(f"Wow! Your scores are really spread out!")
else:
    logger.info(f"You are very consistent with your scores!")

# Condition 2 - Low Score
if smallest < 20:
    logger.info(f"Your lowest score was {smallest}..... Did you even try?")

# Condition 3 = Best Game
if game2 > game1 or game3 > game2:
    logger.info(f"Congratulations! You are showing improvement with your scores!")

with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())
