# The question here is to find the double spaces in the string and replace them with single ones.
# The problem I am facing here is that no matter how I change the data the output is always coming out to be 48. Confused !!

notice = '''All Class 12 Students of Hem Sheela Model School  are hereby informed that 
they are going to have special  summer classes starting from 5th  June to 19th  June.
All students are requested to attend these classes regularly without  fault.'''

k = notice.find("  ")

print(k)