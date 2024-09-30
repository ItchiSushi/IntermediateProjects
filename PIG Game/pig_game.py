import random

def roll():
    min_value = 1
    max_value = 6
    roll_dice = random.randint(min_value, max_value)

    return roll_dice

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

max_score = 20
player_scores = [0 for i in range(players)]
while max(player_scores) < max_score:
    for players_i in range(players):
        print("Player", players_i + 1, "turn has started! \n")
        print("Your total score is: ", player_scores[players_i], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll? (yes): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1!. Your turn is done!")
                current_score = 0
                break
            else:
                current_score += value
            print("Your current score is: ", current_score)

        player_scores[players_i] += current_score
        print("Your total score is:", player_scores[players_i])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of: ", max_score)