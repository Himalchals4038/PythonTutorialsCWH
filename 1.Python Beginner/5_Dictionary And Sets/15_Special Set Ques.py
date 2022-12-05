S = set()
S.add(45)
S.add(45.0)
S.add("45")
print(S)
print(len(S))

# Here 45 and 45.0 though being integer and float number are considered to be the same.