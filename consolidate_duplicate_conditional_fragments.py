# by Kami Bigdely
# Consolidate duplicate conditional fragments
def add(mix, something):
    mix.append(something)
    return mix

def mixer_ice_with_cream():
    print('mixed ice with cream.')
    return ['ice', 'cream']

def make_drink(drink, addons):
    mix = []
    mix = add(mix, drink)
    mix = add(mix, addons)
    if 'strawberry milkshake' in drink:
        mix = mixer_ice_with_cream()
    return mix

drink=[]  
if 'coffee' in drink:
       make_drink()

       



# final_drink = make_drink(drink='coffee',addons='none'),
milk_shake = make_drink(drink='strawberry milkshake', addons=['milk', 'sugar'])

# print(final_drink)
print(milk_shake)