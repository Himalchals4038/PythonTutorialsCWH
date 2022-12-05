name = "Mason"
# a = f"This is {name}"
a = "This is {}".format(name)
print(a)

channel = "Sky News"
# b = f"Anchor at {channel}"
b = "Anchor at {}".format(channel)
print(b)

# c = f"This is {name} and welcome to {channel}"
c = "This is {} and welcome to {}".format(name, channel)
print(c)

'''
In older versions of Python when f-strings were not introduced 
format command was used to put variables inside a string.
The variables were put orderwise one after another as stated in the string.

We can also use numbers to denote the order and then state inside format orderwise.
'''

type = "World News"

d = "The channel is {1} which shows {2} and its anchor is {0}".format(name, channel, type)
print(d)
