'''If a comment consists of sentences like 'make a lot of money', 'buy now', 'subscribe this', 'click this'.
Mark it as a spam comment otherwise mark it as a normal comment.'''

text = input("Enter your comment: ")

if (text == "make a lot of money"):
    print("Spam Comment")
elif (text == "buy now"):
    print("Spam Comment")
elif (text == "subscribe this"):
    print("Spam Comment")
elif (text == "click this"):
    print("Spam Comment")
else:
    print("Normal Comment")
