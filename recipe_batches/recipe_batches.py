#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  if set(recipe) == set(ingredients):
    new_list = []
    for i in recipe:
      # print("i: ***", i)
      if ingredients[i] >= recipe[i]:
        new_ammount = ingredients[i] // recipe[i]
        new_list.append(new_ammount)
        # print("x: appended ***", new_list)
        # print("min(x): ***", min(new_list))
    return min(new_list)
  else:
    return 0

print("FINAL RESULT***", recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))


# IF "the function should output the maximum number of whole batches that can be made for
# the supplied recipe using the ingredients available to you", THEN logically our Limit,
# or "end result" will be the output of the smallest amount of ingredients available
# divided by the amount needed from the recipe.



# first compare the recipe with the ingredients to see if we have the same amount of key/values

# if not then return 0

# create a new list that will hold the compared values

# iterate through the *recipe* list and compare each key/value to the same [i] in the
# *ingredients* list

# if the ingredients[i] is >= the recipe[i], then store the result of
# ingredients[i] // recipe[i] and append the result to the new list

# this should repeat until it's compared every key/value and added the divided difference
# it to the new list

# then we want to return the smallest value on the list








# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))