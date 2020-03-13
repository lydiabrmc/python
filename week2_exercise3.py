# ## Section C
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango
# 2. Add "Grapes" to the list
# 3. Change "Pears" to "Strawberries"
# 4. Remove "Apples" from the list
# 5. Print out the current length of the list
# 6. Print out the list
# 7. Order the list alphabetically
# 8. Print out the list again

fruit = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
fruit.append("Grapes")
print(fruit)

fruit[2] = "Strawberries"
print(fruit)

del(fruit[0])
print(fruit)

print(len(fruit))

print(fruit)

fruit.sort()
print(fruit)