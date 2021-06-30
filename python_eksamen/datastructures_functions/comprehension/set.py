#syntaks
#{expression for element in set if condition}
tags = {'Django', 'Pandas', 'Numpy'}

lowercase_tags = set()
for tag in tags:
    lowercase_tags.add(tag.lower())

print(lowercase_tags)

#samme som: 

lowercase_tags = {tag.lower() for tag in tags}
print(lowercase_tags)