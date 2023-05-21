fruits=['grapes','mango','apple']
fruits.sort()
print(fruits)
# we can use sort only in list.
# for tuple:
fruits1=('grapes','mango','apple')
print(sorted(fruits1)) # will give a sorted list
# similarly for sets:
fruits2={'grapes','mango','apple'}
print(sorted(fruits2)) # will give a sorted list

## 
guitars=[
    {'model':'yamaha1','price': 1000},
    {'model':'yamaha2','price': 3000},
    {'model':'yamaha3','price': 2000}
]
sorted_guitars=sorted(guitars, key=lambda d: d['price'])
print(sorted_guitars) # will print from min to max price
sorted_guitars=sorted(guitars, key=lambda d: d['price'], reverse=True)
print(sorted_guitars) # will print from max to min price