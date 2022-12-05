l = ["Forex", "Lizz", "Johnsom", "Monica", "Andreas", "Ricco", "Finessa", "Hamilton"]
m = ("Forex", "Lizz", "Johnsom", "Monica", "Andreas", "Ricco", "Finessa", "Hamilton")

sentence = "~~".join(l)
print(sentence)
sentence = " and ".join(l)
print(sentence)
sentence = " or ".join(m)
print(sentence)
sentence = "\n".join(m)
print(sentence)
print(type(sentence))

# Join command is used to connect the different elements of an iterable arrangement.
# That connection can be done by a string variable.
# Join operator only works with string, thats the drawback of this operator.

