# generators are iterator.
# l=[1,2,3] --> iterable (To apply loop in iterable, at first it coverts to iterator)
# map(lambda a: a**2,l) --> iterator (In case of iterator loop apply directly)

# If we want to use a sequence repeatedly than we use List.
# List--> whole sequence requires a single memory
# If we want to use item of a sequence once at a time than we use Generator.
# Generator--> item of a sequence requires a memory.