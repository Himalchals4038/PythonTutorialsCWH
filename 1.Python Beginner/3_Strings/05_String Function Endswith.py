name = "MichaelTheSaint"
story = '''Once upon a time there was a great saint known as Michael
who spread the values of Christianity through his preachings.
He travelled far and wide to spread the messages and teachings of Jesus'''

print(len(story))
# len is used to print the length of the string.
print(story.endswith("Saint"))
# This with give false as story didn't end with Saint.
print(story.endswith("Jesus"))
# This will give true as story ends with Jesus.
print(story.endswith("sus"))
# This will also give output as true as the word Jesus ends with "sus".

