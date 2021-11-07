x= (1,'two', 3.0, [4, 'four'], 5)
y= (1, 'two',3.0,[4, 'four'], 5)
print('x is {}'. format(x))
print(id(x[1]))
#return the same value because for x[1] only one object has been created
print(id(y[1]))

if isinstance(x, tuple):
    print('yep')
# x is a tuple but not a list
# y is not a tuple but a list
else:
    print('nope')




