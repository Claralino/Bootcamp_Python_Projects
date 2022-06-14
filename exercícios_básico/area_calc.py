from math import ceil

def area_function(height, width, coverage):
    n_of_cans = ceil((height * width) / coverage)
    print(f"the number of cans needed is: {n_of_cans}")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage_can = 5

area_function(test_h, test_w, coverage_can)


 