from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    #setup
    f = open(file, mode)
    yield f
    #teardown
    f.close()

with open_file('sample_func.txt', 'w') as f:
    f.write('Testing')

print(f.closed)