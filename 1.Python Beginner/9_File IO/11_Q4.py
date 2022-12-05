'''Write a program to censor a single word in a file.'''

with open('blind typing.txt') as f :
    content = f.read()

content = content.replace("God", "$#&&%@&$")

with open('blind typing.txt', 'w') as f :
    f.write(content)
