# Import fernet from the cryptography package.
from cryptography.fernet import Fernet
# Create a function that can create a key using fernet. This can be commented if it has been called once.
def write_key():
    # Create a key variable and initialise it to fernet that generates a random key.
    key = Fernet.generate_key()
    # Create a .key file as key_file that will store the key
    with open("key.key", "wb") as key_file:
        key_file.write(key)
# Call the write_key() function once to create the .key file. This can be removed/commented out once called (optional).
write_key()
# Create function that will load the key from the .key file
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key
# Store the loaded key into a variable 'key'
key = load_key()
# Parse the key variable into the Fernet function where it will be encrypted.
fer = Fernet(key)
# Create function that will allow the user to view an account when called
def view():
    # 'r' stands for read, which restricts the user to reading a file only and in no way can they edit the file.
    with open('passwords.txt', 'r') as f:
        # Create a for loop to loop through the txt file to return each line.
        for line in f.readlines():
            # Store each line in a variable 'data' and rstrip() to strip/remove the new line that gets automatically gets added to each line.
            data = line.rstrip()
            # Create variables and initialise them to the data variable that contains the accounts.
            # We use .split to separate the text into each variable when the program looks for a specific character '|'.
            user, passw = data.split("|")
            # Decrypt and display the list of records in the txt file using the 2 variables.
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())
# Create function that will add an account when called
def add():
    name = input("Account Name: ")
    user_password = input("Password: ")
    # This allows us to create and open a file using 'with' and the function open() allows us to specify the name of this file. This also closes the file automatically.
    # 'a' stands for append so we can add something to end of the file.
    # 'w' stands for write which will override that file that already exists.
    with open('passwords.txt', 'a') as f:
        #Write to the file to add the name and password. Use fer.encrypt to encrypt the password in the file. The \n will allow each new account to be added on a new line.
        f.write(name + "|" + str(fer.encrypt(user_password.encode()).decode()) + "\n")

# Create a while loop that will prompt the user to store a password or to add a new one, or to quit the program.
while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add, quit): ").lower()
    #Create if and elif to get the appropriate answers otherwise else if the none of the options were selected then the while loop will continue.
    if mode == "quit":
        # Quit the program if the user chooses quit.
        print("Goodbye!")
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