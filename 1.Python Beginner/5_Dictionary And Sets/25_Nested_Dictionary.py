# Nested Dictionary means putting one dictionary inside another dictionary. 

myDict = {
    'python':{'duration':'4 months', 'fees':'7000'},
    'javascript':{'duration':'8 months', 'fees':'15000'},
    'c++':{'duration':'6 months', 'fees':'10000'}
}
print(myDict)

myDict['javascript']['duration'] = '9 months'
print(myDict)

print(myDict['c++'])
print(myDict['python']['fees'])

for a,b in myDict.items() :
    print(a,b)
    
for a,b in myDict.items() :
    print(a,b['duration'], b['fees'])