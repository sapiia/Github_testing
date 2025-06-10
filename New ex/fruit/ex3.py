fruit=['banana', 'coconut', 'manago','jackfruit']
position=0
for i in range (len(fruit)):
    if fruit[i]=="manago":
        position+=i
print(position)