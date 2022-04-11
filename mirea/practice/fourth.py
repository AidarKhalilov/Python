class HashElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_element(self):
        return self.key, self.value

    def __repr__(self):
        return str(self.key) + ': ' + str(self.value)

    def get_value(self):
        return self.value


class HashTable:
    hash_table = []
    size = 0

    def __init__(self):
        print('HashTable has been created')

    def add_elem(self, key, value):
        self.hash_table.append(HashElement(key, value))
        self.size += 1

    def get_all(self):
        return [item for item in self.hash_table]

    def get_size(self):
        return 'The size of your hashTable is ' + str(self.size)


def main():
    dictionary = {}
    hash_table = HashTable()
    dictionary['first'] = 1
    dictionary['second'] = 2
    hash_table.add_elem('first', 1)
    hash_table.add_elem('second', 2)
    assert dictionary.values() == hash_table.get_all()


main()
