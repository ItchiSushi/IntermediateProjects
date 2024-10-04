# Open the txt file to access the stings. Best practice for opening files.
with open('story.txt', 'r') as f:
    # Read the txt file and store it in a variable.
    story = f.read()
# Create a set() function inside a variable that will only store unique elements and not d
words = set()
start_of_word = -1
target_start = "<"
target_end = ">"
# Create a for loop that will loop through the story using enumerate. Gives access to the position as well as element at that position.
for i, char in enumerate(story):
    # Create if statements to check if the char equals "<" in the txt file
    if char == target_start:
        start_of_word = i
    # Created another if statement to check for the ">" and extract that characters between the two chars "<>". Store that word into the set list "words"
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# Create a dictionary
answers = {}
# Use a for loop to prompt use to enter a replacement word and store it in the dictionary to access later.
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer
# Use a for loop to that will cycle through each unique word and replace it with the given word.
for word in words:
    story = story.replace(word,answers[word])
# Display the new story.
print(story)