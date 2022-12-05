'''Alteration of the previous question.'''

text = input("Enter your comment: ")
spam = False

if ("make a lot of money" in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("subscribe this" in text):
    spam = True
elif ("click this" in text):
    spam = True

if (spam):
    print("The comment is spam.")
else:
    print("The comment is not spam.")