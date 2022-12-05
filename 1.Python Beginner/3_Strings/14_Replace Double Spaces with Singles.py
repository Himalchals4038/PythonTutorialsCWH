# Continuation of previous problem. Here we replace the double spaces with the single ones to rectify the notice. 

notice = '''All Class 12 Students of Hem Sheela Model School  are hereby informed that 
they are going to have special  summer classes starting from 5th  June to 19th  June.
All students are requested to attend these classes regularly without fault.'''

notice = notice.replace("  ", " ")

print(notice)

noticed = '''All Class 12 Students of Hem Sheela   Model    School  are hereby informed that 
they are going to have special  summer classes starting from 5th  June to 19th  June.
All students are requested to attend these classes regularly without fault.'''

noticed = noticed.replace("  ", " ")

print(noticed)
# Here the triple and quadruple spaces have not been fully converted into single spaces
# As python changes a double space into single but doesn't recheck if that space is single only or not.
# So in quadruple spaces two double spaces are changed into single spaces which leads to a double space.
# In triple spaces python detects only one double space and converts it to single space but atlast there is a double space in there.
# So this method is not fool-proof and we need to loop this sequence to remove every multiple spacing from the string.