l = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
for index, item in enumerate(l):
    if index == 2 or index == 4 or index == 6 :
        print(index,item)
    else :
        continue

m = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
for index, item in enumerate(m):
    if index == 2 or index == 4 or index == 6 :
        print(f'The {index+1}th ekement is {item}')
    else :
        continue 