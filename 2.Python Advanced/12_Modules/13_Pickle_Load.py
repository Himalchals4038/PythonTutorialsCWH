import pickle

f = open('writedata.txt', 'rb') # rb stands for read binary
l = pickle.load(f)
print(l)

# Load function in pickle module deserializes the data in the txt file.