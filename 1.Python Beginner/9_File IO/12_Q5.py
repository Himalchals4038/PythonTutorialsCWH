'''Write a program to censor specific words in a file.'''

words = ['God', 'computer', 'hard', 'stressful']

with open('blind typing.txt') as f :
    content = f.read()

for word in words :
    content = content.replace(word, "$#&&%@&$")

with open('blind typing.txt', 'w') as f :
    f.write(content)
