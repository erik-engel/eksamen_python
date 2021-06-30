#clear()
d = {'a': 10, 'b': 20, 'c': 30}
d.clear()
print(d)

#get()
d = {'a': 10, 'b': 20, 'c': 30}

print(d.get('a'))

#items()
d = {'a': 10, 'b': 20, 'c': 30}
print(d.items())

#keys()
d = {'a': 10, 'b': 20, 'c': 30}
print(d.keys())

#values()
d = {'a': 10, 'b': 20, 'c': 30}
print(d.values())

#pop()
d = {'a': 10, 'b': 20, 'c': 30}
print(d.pop('a'))

#popitem()
d = {'a': 10, 'b': 20, 'c': 30}
print(d.popitem())

#update
d = {'a': 10, 'b': 20, 'c': 30}
d1 = {'d':40,'f':200}
d.update(d1)
d.update([('g', 400), ('h', 600)])
d.update(b=100000)
print(d)