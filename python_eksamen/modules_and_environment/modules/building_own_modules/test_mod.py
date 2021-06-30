# import statementet finder modulet og sørger for vi nu kan bruge kode fra mod
import mod

# vi kan f.eks. tilgå mod's variabler
print(mod.s)

l = mod.a

print(l)

for l in l:
    print(l)

# vi kan bruge mod's funktioner
mod.foo(['quux', 'corge', 'grault'])

# vi kan bruge mods klasser.
x = mod.Foo()
print(x)
