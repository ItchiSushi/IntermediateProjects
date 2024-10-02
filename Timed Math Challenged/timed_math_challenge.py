# Import random library to be used in the operations of the program.
import random
# Import time library to be used at the start and end of the program.
import time
# Create list that will store the basic math operators.
OPERATORS = ["+", "-", "*"]
# Create 2 variables and set one to a low value and one to a high value.
MIN_OPERAND = 3
MAX_OPERAND = 12
# Create a problem variable that will act as the amount of math problems that will occur in the program.
TOTAL_PROBLEMS = 10
# Create a function that will perform the math operations.
def generate_problem():
    # Create a left and right variables. Call the random.randint function in both and parse the MIN and MAX variables in them.
    left =  random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    # Create an operator variable and call the random.choice function which will choose a random operator inside the OPERATOR list.
    operator = random.choice(OPERATORS)
    # Create an expression variable called expr that will store the left, operator, and right variable as a string.
    expr = str(left) + " " + operator + " " + str(right)
    # Create an answer variable that will use the eval() function to evaluate the expr string and return the answer of that expression.
    answer = + eval(expr)
    return expr, answer
# Prompt the user to enter any key button to begin the program.
input("Press any key to start: ")
print("------------------------")
# Create a time variable that will call the time.time() function which start a timer as soon as the user presses any key.
start_time = time.time()
# Create a for loop that will loop the amount of times that the TOTAL_PROBLEMS variable was set to.
for i in range(TOTAL_PROBLEMS):
    # Create two variable and call the generate_problem() function which the value will pass the returned values into those variables.
    expr, answer =generate_problem()
    # Create a while loop that will loop until condition inside the loop is false.
    while True:
        # Prompt the user to answer the math expression and store it in a variable guess.
        guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
        # If the guess variable is equal to the answer then break out of the while loop.
        if guess == str(answer):
            print("Correct!")
            break
        else:
            # If the answer is wrong, display a message continue to the loop until it is correction.
            print("That's wrong try again!")
# Create an end_time variable that will call the time.time() function once the for loop ends.
end_time = time.time()
# Subtract the 2 times from each other which will shave off the excess time that accumulated at the end of the challenge. And round it to two decimal places.
total_time = round(end_time - start_time, 2)
print("------------------------")
# Display the message with the users final time it took them to complete the challenge.
print("Good Job! Your total time was " + str(total_time) + " seconds!")