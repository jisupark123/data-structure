from HashTable import HashTable

a = HashTable(10)
a.insert(10)
a.insert(10)
a.insert(25)
a.insert(27)
a.insert(31)
a.insert(42)
a.insert(16)
a.insert(34)

print(a.search(10))
