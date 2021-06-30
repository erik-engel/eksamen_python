import os

os.mkdir('os_exercise')
os.chdir('os_exercise')

# open('exersice.py', 'w')

x = input('Skriv noget til Pythonfilen: ')


with open('exercise.py', 'w') as f:
    f.write(x)

