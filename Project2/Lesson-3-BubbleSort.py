# Проверяет два соседних элемента массива и какой больше передвигает направо

oldlist = [10, 75, 43, 15, 25, -4, 27]

def bubble_sort(mylist):
    last_item_index = len(mylist) - 1
    for i in range(0, last_item_index):  # считает сколько элементов
        for r in range(0, last_item_index-i):  # этот уже сравнивает и меняет, но последний элемент не надо сортировать, поэтому -i
            print(mylist)
            if mylist[r] > mylist[r+1]:
                mylist[r], mylist[r+1] = mylist[r+1], mylist[r]  # меняем местами
    return mylist

print("Original list: ", oldlist)
sorted_list = bubble_sort(oldlist).copy() # copy именно чтобы все элементы скопировались как надо, а не просто клон получился бы
print("Sorted list: ", sorted_list)