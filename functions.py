import os
import webbrowser

def youtube_recipe(name):
    url = 'https://www.youtube.com/results?search_query='
    iname = name + '+' + 'recipe'
    webbrowser.open(url + iname)

def check_dish():
    with open('inventory.txt', 'r') as inventory:
        content = inventory.readlines()
        inventory = {}
        for record in content:
            data = record.rstrip('\n').split('#')
            inventory[data[0]] = data[1]

    with open('recipe.txt', 'r') as recipe:
        content = recipe.readlines()
        dish = []
        for record in content:
            make = True
            data = record.rstrip('\n').split('@')
            for t in data[1:]:
                    i, q = t.split('#')
                    try:
                        if int(inventory[i]) < int(q):
                            make = False
                    except KeyError:
                        make = False

            if make:
                dish.append(data[0])

    print('+' + '-'*30 + '+')
    print('|{:^30s}|'.format('Dish'))
    print('+' + '-'*30 + '+')
    for item in dish:
        print('|{:^30s}|'.format(item))
    print('+' + '-'*30 + '+')

def dish_checker():
    with open('inventory.txt', 'r') as inventory:
        content = inventory.readlines()
        inventory = {}
        for record in content:
            data = record.rstrip('\n').split('#')
            inventory[data[0]] = data[1]
    with open('recipe.txt', 'r') as recipe:
        content = recipe.readlines()
        iname = input('Enter what you want to make: ')
        name = ''.join(iname.split()).lower()
        less_item = []
        found = False
        make = True
        for record in content:
            data = record.rstrip('\n').split('@')
            if data[0] == name:
                found = True
                for t in data[1:]:
                    i, q = t.split('#')
                    try:
                        if int(inventory[i]) < int(q):
                            make = False
                            less_item.append(i + '#' + str(int(q) - int(inventory[i])))
                    except KeyError:
                        less_item.append(i + '#' + q)
                        make = False


    if make and found:
        print('All ingredients are present!')
        ans = input('Do you want YouTube Recipe: (y/n)? ')
        if ans == 'y':
            youtube_recipe(name)

    elif found and not make:
        print('+' + '-'* 36 + '+')
        print('|{:^30s}|{:^5s}|'.format('Items', 'Req'))
        print('+' + '-'* 36 + '+')
        for ing in less_item:
            data = ing.split('#')
            print('|{:^30s}|{:^5s}|'.format(data[0], data[1]))
        print('+' + '-'* 36 + '+')
        ans = input('Do you want YouTube Recipe: (y/n)? ')
        if ans == 'y':
            youtube_recipe(name)

    else:
        print('No Recipe for {}'.format(iname))
        ans = input('Do you want YouTube Recipe: (y/n)? ')
        if ans == 'y':
            youtube_recipe(name)

def inventory_check():
    with open('inventory.txt', 'r') as inventory:
        content = inventory.readlines()
        list_less = []
        for record in content:
            data = record.rstrip('\n').split('#')
            if int(data[1]) <= 1:
                list_less.append(data[0])
    print('+' + '-'*15 + '+')
    print('|{:^15s}|'.format('Ingredients'))
    print('+' + '-'*15 + '+')
    for ing in list_less:
        print('|{:^15s}|'.format(ing))
    print('+' + '-'*15 + '+')

def item_entry():
    while True:
        file = open('inventory.txt','r')
        new = open('new.txt','a')
        content = file.readlines()
        n = input('Enter Ingredient: ')
        n = ''.join(n.split()).lower()
        q = input('Enter Quantatity: ')
        chk = 0
        for record in content:
            data = record.rstrip('\n').split('#')
            if data[0] == n:
                data[1] = str(int(data[1]) + int(q)) + '\n'
                chk = 1
            else:
                data[1] += '\n'
            data = '#'.join(data)
            new.write(data)
        if chk == 0:
            ans = input('Do you want to enter this item? (y/n) ')
            if ans == 'y':
                data = n + '#' + q + '\n'
                new.write(data)
        file.close()
        new.close()
        os.remove('inventory.txt')
        os.rename('new.txt', 'inventory.txt')

        loop = input("Do you want to enter more items? (y/n): ")
        if loop == 'n':
            break

def recipe_entry():
    with open('recipe.txt', 'a') as recipe:
        ch = 'y'
        list_req = []
        while ch == 'y':
            iname = ''.join(input('Enter Dish Name: ').split()).lower()
            ans = 'y'
            while ans == 'y':
                req = ''.join(input('Enter Ingrediants: ').split()).lower()
                qty = input('Enter Quantatiy: ')
                list_req.append(req + '#' + qty)
                ans = input('Do you wanna enter more ingredieants? (y/n) ')
            data = iname + '@' + '@'.join(list_req) + '\n'

            recipe.write(data)
            ch = input('Do you want to add more dishes? (y/n) ')

def view_inv():
    with open('inventory.txt', 'r') as inventory:
        content = inventory.readlines()
        print('+' + '-'*36 + '+')
        print('|{:30s}|{:^5s}|'.format('Item Name', 'Qty'))
        print('+' + '-'*36 + '+')
        for record in content:
            data = record.rstrip('\n').split('#')
            print('|{:30s}|{:^5s}|'.format(data[0], data[1]))
        print('+' + '-'*36 + '+')

def view_rec():
    with open('recipe.txt', 'r') as recipe:
        content = recipe.readlines()
        print('+' + '-'*30 + '+')
        print('|{:^30s}|'.format('Recipes Available'))
        print('+' + '-'*30 + '+')
        for record in content:
            print('|{:^30s}|'.format(record.split('@')[0]))
        print('+' + '-'*30 + '+')

def item_used():
    recipes = []
    with open("recipe.txt", 'r') as file:
        content = file.readlines()
        for record in content:
            recipes.append(record)

    dish = ''.join(input('Enter What You Made: ').split()).lower()
    found = False

    for c in recipes:
        if c.split("@")[0] == dish:
            recipe = c
            found = True

    if found:
        file = open("inventory.txt", 'r')
        new = open("new.txt", 'w')
        content = file.readlines()
        recipe_ingredients = recipe.split("@")[1:]
        recipe = []

        for ingredient in recipe_ingredients:
            recipe.append(str(ingredient.split('#')[0]))

        for record in content:
            item, qty = record.rstrip('\n').split('#')
            if item in recipe:
                index = recipe.index(item)
                after_qty = int(qty) - int(recipe_ingredients[index].split('#')[1])
                if after_qty < 0:
                    after_qty = 0
                new.write(item + "#" + str(after_qty) + "\n")
            else:
                new.write(item + "#" + str(qty) + "\n")
        print("Items Updated!")
        file.close()
        new.close()
        os.remove("inventory.txt")
        os.rename("new.txt", "inventory.txt")

    else:
        print("Recipe is not Available for {}".format(dish))
        ans = input("Do you want to enter manually? (y/n): ")
        recipe_list = [dish]
        if ans == 'y':
            chk = 'y'
            while chk == 'y':
                ingredient = input("Enter Ingredient: ")
                qty = input("Enter Quantaty: ")
                recipe_list.append(ingredient + '#' + qty)
                chk = input("Do you want to enter more? (y/n): ")
            ingredient = []

            for c in recipe_list:
                ingredient.append(c.split('#')[0])

            file = open("inventory.txt", 'r')
            new = open("new.txt", 'w')
            content = file.readlines()
            item_in_inventory = []
            for record in content:
                item, qty = record.rstrip('\n').split('#')
                if item in ingredient:
                    item_in_inventory.append(item)
                    index = ingredient.index(item)
                    after_qty = int(qty) - int(recipe_list[index].split('#')[1])
                    if after_qty < 0:
                        after_qty = 0
                    new.write(item + '#' + str(after_qty) + '\n')
                else:
                    new.write(item + '#' + qty + '\n')

            for item in ingredient[1:]:
                if item not in item_in_inventory:
                    index = ingredient.index(item)
                    new.write(recipe_list[index].split('#')[0] + '#' + '0' + '\n')
            print("Items Updated!")
            file.close()
            new.close()
            os.remove("inventory.txt")
            os.rename("new.txt", "inventory.txt")
            ans = input("Do you want to enter the recipe for {}? (y/n): ".format(dish))
            if ans == 'y':
                file = open("recipe.txt", 'a')
                file.write('@'.join(recipe_list) + '\n')
                print("Recipe Added!")
