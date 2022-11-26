import re


with open("day21_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.read().strip().split("\n")

# Create list of all food (all ingredients in all rows) and list of allergens
all_food = []
allergens = []
for line in input_data:
    result = re.match(r"^([a-z ]+)\(contains ([a-z, ]*)\)$", line).groups()
    all_food.extend(result[0].strip().split())
    allergens.extend(result[1].split(", "))

allergens = list(set(allergens))

# Create empty dictionary for results
RESULTS = {}
for a in allergens:
    RESULTS[a] = []

# For all allergens find row with this allergen and add list of ingredients
# into dictionary RESULTS
for a in allergens:
    for row in input_data:
        result = re.match(r"^([a-z ]+)\(contains ([a-z, ]*)\)$", row).groups()
        if a in result[1].split(", "):
            RESULTS[a].append(result[0].strip().split())

# Find what this rows for each allergen have common (which ingredients
# are common)
for a, ingredients in RESULTS.items():
    RESULTS[a] = list(set.intersection(*[set(x) for x in ingredients]))


# Create dictionary where ingredient is key and allergen is value
# If allergen in RESULTS is in 1 ingredient, move this couple into new
# dictionary.
# If ingredient with allergen is in new dictionary, delete this ingredient
# from possible ingredients in list RESULTS (decrease list of possible
# intredients for each allergen)
INGREDIENTS_AND_ALLERGENS = {}
while RESULTS:
    for allergen, ingredients in RESULTS.items():
        if len(ingredients) == 1:
            INGREDIENTS_AND_ALLERGENS[ingredients[0]] = allergen

    for ingredient, allergen in INGREDIENTS_AND_ALLERGENS.items():
        if allergen in RESULTS:
            del RESULTS[allergen]

    for allergen, ingredients in RESULTS.items():
        for item in ingredients:
            if item in INGREDIENTS_AND_ALLERGENS:
                RESULTS[allergen].remove(item)


# Find out how many ingredients doesn contain allergens
for ingredient in INGREDIENTS_AND_ALLERGENS:
    while ingredient in all_food:
        all_food.remove(ingredient)

print("How many times do any of those ingredients appear?")
print(f"= {len(all_food)}")
print()

# PART 2
final = []
for ingredient, allergen in INGREDIENTS_AND_ALLERGENS.items():
    final.append((allergen, ingredient))

final.sort()
result = []
for allergen, ingredient in final:
    result.append(ingredient)

print("What is your canonical dangerous ingredient list?")
print("=", ",".join(result))
