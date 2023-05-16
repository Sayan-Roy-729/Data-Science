numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while (n := len(numbers)) > 0:
    print(numbers.pop())


## without walrus operator
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

## with walrus operator
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
    