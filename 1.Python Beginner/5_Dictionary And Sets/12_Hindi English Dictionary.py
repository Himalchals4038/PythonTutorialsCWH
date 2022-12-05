# Write a program to convert the hindi version of different tastes to english language.

D1 = {
    "Karwa": "Bitter",
    "Teekha": "Spicy",
    "Meetha": "Sweet",
    "Khatta": "Sour",
    "Namkeen": "Salty"
}

print("The different tastes are: ", D1.keys())
a = input("Enter the taste im Hindi Language:\n\t")

# print("Translation of that word in English is: ", D1[a])
# Above line shows error if the value is not present in the set dictionary.

print("Translation of that word in English id: ", D1.get(a))
# Use above line if you don't want any error shown if the value is not present in the set dictionary.