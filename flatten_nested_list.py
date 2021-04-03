l = [2, 3, 4, [3, 4, 5, [1, 2]]]
output = []

def removeNestings(l):
    for i in l:
        if type(i) == list:
            removeNestings(i)
        else:
            output.append(i)

removeNestings(l)
print(l)
print(output)
