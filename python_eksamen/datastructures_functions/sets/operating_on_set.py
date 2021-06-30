

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x3 = {1,2,3,4, 'baz'}

# Union

#operator
print(x1|x2)
#method
print(x1.union(x2))
#set and tuple
#ok
print(x1.union(('this','is','tuple')))
#not ok
#print(x1|('this','is','tuple'))

# multiple sets
print(x1|x2|x3)
print(x1.union(x2,x3))

# Intersection

#operator
print(x1 & x2)
#method
print(x1.intersection(x2))

#set and tuple
print(x1.intersection((1,2,3,'baz')))

# multiple sets
print(x1&x2&x3)
print(x1.intersection(x2,x3))

# Difference

#operator
print(x1-x2)
#method
print(x1.difference(x2))
#set and tuple
print(x1.difference(('baz', 'bar', 2,3)))
#multiple sets
print(x1-x2-x3)

#Symmetric difference

#operator
print(x1^x2)
#method
print(x1.symmetric_difference(x2))
#set and tuple
print(x1.symmetric_difference(('foo', 3, 5)))
#multiple sets
print(x1^x2^x3)

# isdisjointed
print(x1.isdisjoint(x2)) #False hvis der ikke er nogen elementer tilfælles
print(x1.isdisjoint(('tottaly', 'different', 'values'))) # True hvis alle elementerne er vidt forskellige

#issubset
print(x1.issubset(x2)) #False hvis ikke alle elementer af x1 indgår i x2
print(x1<x2)
print(x1.issubset(('foo', 'bar', 'baz', 'hej'))) #True hvis alle elementer af x1 indgår i x2


#issuperset
print(x1.issuperset(x2)) #False hvis ikke alle elementer af x2 indgår i x1 
print(x1<x2) 
print(x1.issuperset(('foo', 'bar'))) # Returnerer true hvis alle elementer af x2 indgår i x1

