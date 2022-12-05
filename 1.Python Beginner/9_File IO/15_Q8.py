'''Copy a prevoiusly written program and store it with a new name.'''

with open('log.txt') as f :
    content = f.read()

with open ('log_copy.txt', 'w') as f :
    f.write(content)
