from assets import ninja, my_pets


sushi = my_pets.Cats('Sushi', 'Flips', 100, 100, 'cat')
jared = ninja.Ninja('Jared', 'Campos', 25, 'Tuna Fish', sushi)

shadow = my_pets.Raccoons('Shadow', 'Spins', 200, 300, 'Raccoon')
cait = ninja.Ninja('Cait', 'Artese', 10, 'Garbage Bins', shadow)

bruno = my_pets.Dogs('Bruno', 'Backflip', 850, 1000, 'dog')
jape = ninja.Ninja('Jape', '0413', 100, 'Quail Eggs', bruno)


jared.walk().feed(5).bathe()
print("\n")
cait.walk().feed(10).bathe()
print("\n")
jape.walk().feed(200).bathe()
