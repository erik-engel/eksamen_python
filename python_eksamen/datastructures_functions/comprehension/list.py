fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

#Følgenede loop:
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

# er det samme som:
newlist = [x for x in fruits if "a" in x]
print(newlist)

# et andet eksempel:
newlist = [x for x in range(1,10) if x < 5]
print(newlist)

# sæt alle elementer i fruits
newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits] 
print(newlist)