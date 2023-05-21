# square--> {1:1, 2:4, 3:9}

###
square1={num:num**2 for num in range(1,11)}
print(square1)

###
square2={f"square of {num} is":num**2 for num in range(1,11)}
print(square2)

###
square3={f"square of {num} is":num**2 for num in range(1,11)}
for k,v in square3.items():
    print(f"{k} : {v}")

###
## word count:
string="Abrar Haider"
word_count={char:string.count(char) for char in string}
print(word_count)
