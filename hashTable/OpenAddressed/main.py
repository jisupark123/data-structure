from HashTable import HashTable

a = HashTable(11)
a.insert(10)
a.insert(31)
a.insert(10)
a.insert(14)
a.insert(22)
a.insert(63)
a.insert(1)
a.insert(1)
a.insert(1)
a.insert(1)
a.insert(1)

item = 22
slot = a.search(item)
print(slot)
