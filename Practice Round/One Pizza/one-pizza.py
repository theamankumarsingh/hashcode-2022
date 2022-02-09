import os, sys
from pickle import TRUE
import itertools
import math
import time
start_time = time.time()
input_data=open(sys.argv[1], 'r').read().splitlines()

ingredient_set = set()
ingredients= dict()

customers = []

pizza_ingredients = set()
pizza_customers = 0

customers_count=int(input_data.pop(0))

def count_customers(ing_set):
    cc = 0
    #ing_set = set(ing_list)
    for customer in customers:
        will_come = True
        if not customer['likes'].issubset(ing_set):
            continue
        if ing_set.intersection(customer['dislikes']):
            continue
        cc += 1
    
    return cc

def keywithval(d, val):
     v = list(d.values())
     k= list(d.keys())
     return k[v.index(val)]

def printshit():
    for customer in customers:
        print(customer)

    for ingredient in ingredients.keys():
        print(ingredient, "   " ,ingredients[ingredient])

    print(ingredient_set)
    print(customers_count)
    
for i in range(0,2*customers_count,2):
    customer = {'id': i//2,'likes':set(), 'dislikes':set()}
    customer['likes'] = set(input_data[i].split()[1:])
    customer['dislikes'] = set(input_data[i+1].split()[1:])


    for like_ingredient in input_data[i].split()[1:]:
        
        ingredient_set.add(like_ingredient)

        if like_ingredient in ingredients.keys():
            ingredients[like_ingredient]['liked_by'].append(customer)
        else:
            ingredients[like_ingredient] = {'liked_by':[customer], 'disliked_by':[]}

    for dislike_ingredient in input_data[i+1].split()[1:]:

        ingredient_set.add(dislike_ingredient)

        if dislike_ingredient in ingredients.keys():
            ingredients[dislike_ingredient]['disliked_by'].append(customer)
        else:
            ingredients[dislike_ingredient] = {'liked_by':[], 'disliked_by':[customer]}

    customers.append(customer)

#pizza_ingredients = list(ingredient_set)
for key,value in ingredients.items():
    if len(value['liked_by']) > len(value['disliked_by']):
        pizza_ingredients.add(key)
customers_count = count_customers(pizza_ingredients)

print(f"Customers = {len(customers)}")
print(f"Total Ingredient = {len(ingredient_set)}")

customers_count = count_customers(pizza_ingredients)
print(f"Initial Customers = {customers_count}")
print(f"Initial Ingrdients count = {len(pizza_ingredients)}")

ing_count = len(pizza_ingredients)
max_comb = ing_count

for i in range(1, ing_count//2):
    if math.comb(ing_count,i) > 200000:
        max_comb = i - 1
        break
        
print(f"Max comb = {max_comb}")

loop = True


while loop:
    for i in range(1, max_comb + 1):
        dt = {}
        for ings in itertools.combinations(pizza_ingredients, i):
            pizza = set(x for x in pizza_ingredients if x not in ings)
            #print(pizza)
            cc = count_customers(pizza)
            if cc > customers_count:
                dt[ings] = cc
                #print(cc)

        if dt:
            maxval = max(dt.values())
            customers_count = maxval
            print(f"New customer count = {maxval}")
            keys = keywithval(dt,maxval)
            for key in list(keys):
                pizza_ingredients.remove(key)
            print(f"New Ingredients count = {len(pizza_ingredients)}")
            break

        if i == max_comb:
            loop = False
            break
        

print(f"Final Customer Count = {customers_count}")
open(sys.argv[2], 'w').write(str(len(pizza_ingredients))+' '+' '.join(map(str, pizza_ingredients)))

print("--- %s seconds ---" % (time.time() - start_time))

