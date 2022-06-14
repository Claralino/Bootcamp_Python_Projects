
size = input("wich size of you you want: s, m, l?")
add_pepe = input("do you want to add peperoni: y or n?")
extra_cheese = input("do you want to add cheese: y or n?")
bill = 0

if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
else:
    bill += 25

if add_pepe == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3
else:
    bill = bill 

if extra_cheese == 'y':
    bill += 1
else: bill = bill

print(f"you total bill is {bill}")




