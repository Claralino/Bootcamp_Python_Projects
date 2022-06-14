
print("welcome to the tip calculator!")

v_total = input("what was the total bill?: ")
v_total_float = float(v_total)

tip = input("what percentage would you like to give?: 10, 12 ou 15?: ")
tip_float = float(tip)

people = input("how many peoople to split the bill?: ")
people_float = float(people)

if tip_float == 10:
    v_total_float *= 1.10
    v_total_float = round(v_total_float / people_float, 2)
    print(f"each person should pay: {v_total_float}$")
elif tip_float == 12:
    v_total_float *= 1.12
    v_total_float = round(v_total_float / people_float, 2)
    print(f"each person should pay: {v_total_float}$")
else:
    v_total_float *= 1.15
    v_total_float = round(v_total_float / people_float, 2)
    print(f"each person should pay: {v_total_float}$")
