import re
from itertools import combinations_with_replacement
__author__ = 'Géraud'


def get_ingredients_from_file(filename):
    ingredients = []
    with open(filename, 'r') as file:
        ingredients_list = file.readlines()
        regex = r'^(.+):\s*capacity\s*(-?\d+),\s*durability\s*(-?\d+),\s*flavor\s*(-?\d+)' \
                r',\s*texture\s*(-?\d+),\s*calories\s*(-?\d+)'
        for line in ingredients_list:
            found = re.findall(regex, line)
            if found:
                found = found[0]
                ingredients.append({
                    'capacity': int(found[1]),
                    'durability': int(found[2]),
                    'flavor': int(found[3]),
                    'texture': int(found[4]),
                    'calories': int(found[5])
                })
    return ingredients


def get_recipe_score(recipe):
    capacity = sum(ingredient['capacity'] for ingredient in recipe)
    durability = sum(ingredient['durability'] for ingredient in recipe)
    flavor = sum(ingredient['flavor'] for ingredient in recipe)
    texture = sum(ingredient['texture'] for ingredient in recipe)
    calories = sum(ingredient['calories'] for ingredient in recipe)

    if any([x < 1 for x in [capacity, durability, flavor, texture, calories]]):
        return 0, 0
    else:
        return (capacity * durability * flavor * texture), calories


if __name__ == '__main__':
    ingredients = get_ingredients_from_file('input.txt')
    all_ingredients_combinations = combinations_with_replacement(ingredients, 100)

    scores = []
    scores_with_500_cal = []
    for recipe in all_ingredients_combinations:
        score, calories = get_recipe_score(recipe)
        scores.append(score)
        if calories == 500:
            scores_with_500_cal.append(score)
    print("puzzle 1: %s" % max(scores))
    print("puzzle 2: %s" % max(scores_with_500_cal))
