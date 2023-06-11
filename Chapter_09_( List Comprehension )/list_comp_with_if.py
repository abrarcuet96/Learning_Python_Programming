# List comprehension with if statement.

# Normal Way:
numbers=list(range(1,11))
even_num1=[]
for i in numbers:
    if i%2==0:
        even_num1.append(i)
print(even_num1)

# List comprehension way:
even_num2=[i for i in numbers if i%2==0]
print(even_num2)
# Or,
even_num3=[i for i in range(1,11) if i%2==0]
print(even_num3)
odd_num=[i for i in range(1,11) if i%2!=0]
print(odd_num)