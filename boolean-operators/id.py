a=True
b=False
x=('bear', 'bunny', 'tree', 'sky', 'rain')
y='bear'

if y is x[0]:
    print('expression is true')
else:
    print('expression is not true')
    
    
print (id(y))
print (id(x[0]))

#same object therefore id is same