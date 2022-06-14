
name1 = input("what is your name? ").lower()
name2 = input("what is your lover name? ").lower()

name1_lower = (name1.lower())
name2_lower = (name2.lower())

name1_t = int(name1_lower.count('t'))
name1_r = int(name1_lower.count('r'))
name1_u = int(name1_lower.count('u'))
name1_e = int(name1_lower.count('e'))

name2_t = int(name2_lower.count('t'))
name2_r = int(name2_lower.count('r'))
name2_u = int(name2_lower.count('u'))
name2_e = int(name2_lower.count('e'))

add_true = name1_t + name2_t + name1_r + name2_r + name1_u + name2_u + name1_e + name2_e

name1_l = int(name1_lower.count('l'))
name1_o = int(name1_lower.count('o'))
name1_v = int(name1_lower.count('v'))
name1_e = int(name1_lower.count('e'))

name2_l = int(name2_lower.count('l'))
name2_o = int(name2_lower.count('o'))
name2_v = int(name2_lower.count('v'))
name2_e = int(name2_lower.count('e'))

add_love = name1_l + name2_l + name1_o + name2_o + name1_v + name2_v + name1_e + name2_e

score = int(str(add_true) + str(add_love))


if score < 10 or score > 90:
    print(f"you score is {score}, you go together like coke and mentos")
elif score > 40 and score < 50:
    print(f"your score is {score}, you are alright together")
else:
    print(f"your score is {score}")



