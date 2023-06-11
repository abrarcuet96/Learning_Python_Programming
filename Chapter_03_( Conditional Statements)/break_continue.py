# To break Loop we use break keyword.

for i in range(1,11):
    if i==5:
        break
    print(i)

# Print 1 to 10, but not 5.

for i in range(1,11):#<---
    if i==5:         #   |
        continue # -------
    print(i)