# strings are immutable

string="string"
#string[1]="T", we can't replace like this

print(string.replace('t','T'))
#but,
print(string) #it'll remain same
