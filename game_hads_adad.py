#javab ersali baray maktabkhooneh
'''import random
min = 1
max = 99
hads = random.randint(min,max)
print(hads)
javab = input('javab dorosteh??')
while javab != 'd':
    if javab == 'b':
        min = hads + 1
    else:
        max = hads - 1
    hads = random.randint(min,max)
    print(hads)
    javab = input('javab dorosteh??')
#print('afarin javab dorsteh', hads)'''

#javab behbood shodeh
import random
min = 1
max = 99
hads = random.randint(min,max)
print(hads)
javab = input('javab dorosteh??')
while javab != 'd':
    if javab == 'b':
        min = hads + 1
    elif javab == 'k':
        max = hads - 1
    else:
        print('lotafan dorost rahnamaii konid k = koochaktar , b = bozorgtar , d = dorost')
        javab = input('javab dorosteh??')
        continue
        
    hads = random.randint(min,max)
    print(hads)
    javab = input('javab dorosteh??')
print('----------------------------------------------------')
print('afarin javab ', hads, ' bood barikalaaaaa')
print('----------------------------------------------------')