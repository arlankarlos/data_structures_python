# hash table algorithm in python


class HashTable:
    def __init__(self, table_size):

        if table_size < 1:
            raise ValueError("Table size must be greater than 0")
        self.table_size = table_size
        self.data = [[] for i in range(self.table_size)]

    def hash_func(self, key):
        return key % self.table_size
        # hash = 0
        # for i in range(len(key)):
        #     hash = (hash + ord(key[i]) * i) % self.size
        # return hash

    def insert(self, key):
        self.data[self.hash_func(key)].append(key)

    def show(self):
        for linked_list in self.data:
            if linked_list:
                for key in linked_list:
                    print(f"{key}", end=" ")
                print(" ")

    def search(self, key):
        if key in self.data[self.hash_func(key)]:
            return True
        else:
            return False


data = HashTable(9)

data.insert(19)
data.insert(28)
data.insert(20)
data.insert(5)
data.insert(33)
data.insert(15)

data.show()

data2 = HashTable(1)
