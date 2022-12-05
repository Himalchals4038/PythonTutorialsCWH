list1 = [25, 12.5, True, "Gotcha"]
index = 1
# for item in list1 :
#     print(item, index)
#     index += 1

for index, item in enumerate(list1) :
    print(index, item)
# Enumerate function adds counter to an iterable and returns it.