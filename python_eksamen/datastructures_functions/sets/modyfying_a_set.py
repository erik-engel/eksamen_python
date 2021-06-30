# Modificere et set



# update
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1.update(x2)
print(x1)

#update vha. union
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1 |= x2
print(x1)

# update med et ite
x3 = {1,2,3,4}
x3.update((1,5,6))
print(x3)

# intersection_update
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1&= x2
print(x1)
#eller
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1.intersection_update(x2)
print(x1)

# difference_update
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1.difference_update(x2)
print(x1)
# eller
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1-=x2
print(x1)

# symmetric_differenceupdate
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1.symmetric_difference_update(x2)
print(x1)
# eller
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1^=x2
print(x1)


# add
x1 = {'foo', 'bar', 'baz'}
x1.add('hello')
print(x1)

# remove
x1 = {'foo', 'bar', 'baz'}
x1.remove('foo') #hvis f.eks. remove('fuusdsad') kommer en fejl
print(x1)

# discard
x1 = {'foo', 'bar', 'baz'}
x1.discard('foo')
x1.discard('fuusdsad')
print(x1)

# pop
x1 = {'foo', 'bar', 'baz'}
x1.pop() #fjerner vilkårlig element
print(x1)

# clear
x1 = {'foo', 'bar', 'baz'}
x1.clear()
print(x1)