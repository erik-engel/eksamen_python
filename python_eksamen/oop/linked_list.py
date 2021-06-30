#linked_list.py (solution))

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

    def __repr__(self):
        return f'{self.__dict__}'



# Linked List class contains Node objects
class LinkedList:

    def __init__(self):
        self.head = None
   
    def __len__(self):
        temp = self.head
        count = 0
        while temp: 
            temp = temp.next
            count += 1 
        return count

    def __getitem__(self, key):
        temp = self.head
        count = 0
       
        if type(key) == slice:
            for i in range(key[0], key[1]):
                raise NotImplementedError('To be implemented')
       

        # if key/index is -x l[-1]
        if key < 0: 
            x = len(self) + key
            for i in range(x+1):
                if i == x:
                    return temp
                else:
                    temp = temp.next
                
        else: 
            while temp: 
                if count == key:
                    return temp
                temp = temp.next
                count += 1 

        raise IndexError('index out of range')


    def __setitem__(self, key, val):
        if len(self) < key:
            raise IndexError('index out of range')
        else:    
            temp = "self.head" + ".next" * key + ".data = val"
            exec(temp)
    