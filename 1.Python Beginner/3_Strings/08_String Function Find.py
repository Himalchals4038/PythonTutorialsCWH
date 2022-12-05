name = "MichaelTheSaint"
story = '''Once upon a time there was the great saint known as Michael
who spread the values of Christianity through his preachings.
He travelled far and wide to spread the messages and teachings of Jesus'''

print(name.find("The"))
print(story.find("was"))

# This function finds the required letter, word or phrase in the given string 
# and prints its position according to numbering starting from 0. 

print(story.find("Saint"))
# This will print the result as -1 because "Saint" word is not present in story string.

print(story.find("the"))
# Thiss will display the result as 17 i.e. it will only detect the first "the" in the string and show its number. 
# It will not print the position of second "the" present in the story string.

print(story.find("the", 20))
# Adding a number after the phrase to be found denotes the index number from which the search is to be started.
# 'the' was present at index no. 17 but as we started searching from 20 so 27 was displayed as it was the next 'the'.