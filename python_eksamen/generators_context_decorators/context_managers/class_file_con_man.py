class Open_File():
    #filename er navnet på vores fil, mode er åbning af filen, til read, write osv.
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    #setup part of our manager
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file # Det objekt vi arbejder med inde i vores context manager

    #exit part, what will be run when we exit or context manager
    #De ekstra parametre er der til hvis vi kaster en exception og de kan bruges til at tilgå den information
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File('sample.txt', 'w') as f:
    f.write('Testing')

print(f.closed) #tester at vores context manager virker som den skal