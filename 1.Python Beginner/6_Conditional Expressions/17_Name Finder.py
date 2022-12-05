text = input("Enter your thoughts: ")
Harry = False

if ("Harry" in text):
    Harry = True
elif ("harry" in text):
    Harry = True
else:
    Harry = False

if (Harry):
    print("The comment is about Harry.")
else:
    print("The comment is not about Harry.")