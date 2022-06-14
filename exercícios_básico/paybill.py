import random

names_string = input("give everybody names: ")
names = names_string.split(",") #separa os nomes e bota eles em uma lista

result = random.randint(0, (len(names) -1)) #-1 pq a lista começa com 0 

print(f"{names[result]} will pay the bill")

