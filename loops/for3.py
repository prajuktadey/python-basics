animals= ('bear', 'bunny', 'tiger', 'velociraptor', 'cat', 'dog')

for pet in animals: #assigns each item to variable pet
    if pet=='dog': continue
    if pet=='velociraptor': break
    print(pet)
else:
    print('that is all of the animals')