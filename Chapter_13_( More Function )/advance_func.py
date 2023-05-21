# pass two list and find the average.
def average_finder(l1,l2):
    average=[]
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average
print(average_finder([1,2,3],[4,5,6]))

# pass multiple list and find the average.
def average_finder1(*args):
    average=[]
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
print(average_finder1([1,2,3],[4,5,6],[2,3,4]))

# using lambda:
average_finder2=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(average_finder2([1,2,3],[4,5,6],[2,3,4]))
