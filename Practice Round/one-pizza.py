import os, sys
import math
import time

input_data=open(sys.argv[1], 'r').read().splitlines()

pizza=set()
ingredients=set()
good_ingredients = dict()
bad_ingredients = dict()

customers=int(input_data.pop(0))
for i in range(0,2*customers,2):
    for like_ingredient in input_data[i].split()[1:]:
        ingredients.add(like_ingredient)
        if like_ingredient in good_ingredients.keys():
            good_ingredients[like_ingredient] += 1
        else:
            good_ingredients[like_ingredient] = 1
    for dislike_ingredient in input_data[i+1].split()[1:]:
        ingredients.add(dislike_ingredient)
        if dislike_ingredient in bad_ingredients.keys():
            bad_ingredients[dislike_ingredient] += 1
        else:
            bad_ingredients[dislike_ingredient] = 1

for i in ingredients:
    if i in good_ingredients.keys():
        g_num=good_ingredients[i]
    else:
        g_num=0
    if i in bad_ingredients.keys():
        b_num=bad_ingredients[i]
    else:
        b_num=0
    if(g_num>b_num):
        pizza.add(i)

print(open(sys.argv[2], 'w').write(str(len(pizza))+' '+' '.join(map(str, pizza))))