
listTuples = [(1,2), (2,3), (3,4)]

lst = []

lst = [list(tuple) for tuple in listTuples]

print(lst)