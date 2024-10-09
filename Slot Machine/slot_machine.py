import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_columns(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = " | ")

        print()


def get_deposit():
    while True:
        deposit_amount = input("How much would you like to deposit? R")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("That is not a valid amount!")

    return deposit_amount

def get_number_of_lines():
    while True:
        lines = input("Enter the amount of lines to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("That is not a valid amount!")

    return lines

def get_bet():
    while True:
        bet_amount = input("What would you like to bet? R")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} and {MAX_BET}!")
        else:
            print("That is not a valid amount!")
    return bet_amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You dont have enough to bet. Your Balance is {total_bet}")
        else:
            break

    print(f"You are betting R {bet} on {lines} lines.  The total bet is R{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_columns(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}!")
    print("You won on lines: ", *winning_lines)

    return  winnings - total_bet

def main():
    balance = get_deposit()
    while True:
        print(f"Current balance is {balance}")
        answer = input("Press enter to play or q to quit:")
        if answer.lower() == "q":
            break
        balance += spin(balance)

    print(f"You left with R{balance}")
main()