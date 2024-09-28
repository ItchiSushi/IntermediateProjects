master_password = input("What is the master password")
# Create function that will allow the user to view an account when called
def view():
    # 'r' stands for read, which restricts the user to reading a file only and in no way can they edit the file.
    with open('passwords.txt', 'r') as f:
        # Create a for loop to loop through the txt file to return each line.
        for line in f.readlines():
            # Store each line in a variable 'data' and rstrip() to strip/remove the new line that gets automatically gets added to each line.
            data = line.rstrip()

            user, passw = data.split("|")
# Create function that will add an account when called
def add():
    name = input("Account Name: ")
    user_password = input("Password: ")
    # This allows us to create and open a file using 'with' and the function open() allows us to specify the name of this file. This also closes the file automatically.
    # 'a' stands for append so we can add something to end of the file.
    # 'w' stands for write which will override that file that already exists.
    with open('passwords.txt', 'a') as f:
        #Write to the file to add the name and password.  The \n will allow each new account to be added on a new line.
        f.write(name + "|" + user_password + "\n")

# Create a while loop that will prompt the user to store a password or to add a new one, or to quit the program.
while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add, quit): ").lower()
    #Create if and elif to get the appropriate answers otherwise else if the none of the options were selected then the while loop will continue.
    if mode == "quit":
        # Quit the program if the user chooses quit.
        quit()
    elif mode == "view":

        view()
    elif mode == "add":
        # Call the add() function if the user inputs add.
        add()
    else:
        # If neither of the options were chosen then an error message is displayed and the program loop will continue to prompt.
        print("Invalid Mode!")
        continue