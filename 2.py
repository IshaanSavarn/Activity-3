list = ['Apple','Guava','Mango','Banana', 'kiwi']

print("Length of list:", len(list))
print("First  element:",list[0])
print("Last element:" , list[-1])

list.append('Papaya')
print("Updated List :",list)

list.remove('Guava')
print("Updated List :", list)

list.sort( )
print("Sorted List:",list)

list.pop(1)
print("Updated List :", list)

list.reverse( )
print("Reversed LIst :",list)

list.clear( )
