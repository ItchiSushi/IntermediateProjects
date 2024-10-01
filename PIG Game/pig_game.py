# Import the random library that will be used to randomise integers.
import random
# Define a function that will roll the dice between 1 and 6 each time the function is called.
def roll():
    # Set appropriate variables for the min and max value of a die.
    min_value = 1
    max_value = 6
    # Create a variable that will perform a random function using the min and max variables.
    roll_dice = random.randint(min_value, max_value)
    return roll_dice
# Create a while loop that will repeatedly ask the user how many players they would like have until the user chooses between 2 and 4.
while True:
    players = input("Input the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, please try again")
# Set a max_score variable that will be used as a stopping point in the program.
max_score = 20
# Create a list and inside that list create a loop for the length of players by assigning a 0 to each player.
player_scores = [0 for i in range(players)]
# Create a while loop that will continue to loop until one of the players reaches the max_score
while max(player_scores) < max_score:
    # Create a for loop to loop through each player's turn. Display the current player's score.
    for players_i in range(players):
        print("Player", players_i + 1, "turn has started! \n")
        print("Your total score is: ", player_scores[players_i], "\n")
        current_score = 0
        # Create a while loop to simulate one player's turn. Prompt them to play or give up their turn
        while True:
            # If the player chooses no, then the turn will be handed over to the next player.
            should_roll = input("Would you like to roll? (yes): ")
            if should_roll.lower() != "y":
                break
            # Create value variable and call the roll() function inside it if the player chooses yes to roll the dice.
            value = roll()
            # If the player rolls a 1, then the player's score will reset to 0 and their turn will be given up.
            if value == 1:
                print("You rolled a 1!. Your turn is done!")
                current_score = 0
                break
            # If the player rolls greater than 1, then the value will be added to the current score.
            else:
                current_score += value
            print("Your current score is: ", current_score)
        # The current score of that turn will be added to the current player's score and will be displayed.
        player_scores[players_i] += current_score
        print("Your total score is:", player_scores[players_i])
# Create a variable max_score and set it to the maximum value in the player_scores list.
max_score = max(player_scores)
# Create a variable winning_idx and set it to the position of the max score. The position indicates which player has the highest score.
winning_idx = player_scores.index(max_score)
# Display the winning player and their score.
print("Player number", winning_idx + 1, "is the winner with a score of: ", max_score)