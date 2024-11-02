#Count occuruences of an element in a list
def count_occurrences(l, element):
    count = l.count(element)
    return count
mylist = [1,2,3,4,5,6,7,8,91,2,3,4,63,2,4,5,24,8,9,]
element_to_count = int(input("Enter element to count: "))
occurrences = count_occurrences(mylist, element_to_count)
print(f"The element {element_to_count} appears {occurrences} times in the list.")