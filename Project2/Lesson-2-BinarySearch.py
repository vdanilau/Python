# поиск элемента в отсортированном массиве. Массив как бы делится на две части и каждый раз искомая цифра сравнивается
# с цифрой которая как бы посредине. Если меньше, то пополам уже делится левая часть, если больше, то правая
# и так до тех пор пока начало, конец и средина диапазона не совпадут в искомом числе, а при следующем ране старт становится
# больше стопа, то означает, что нашли


def binarysearch(mylist, target, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if target == mylist[mid]:
            return mid
        elif target < mylist[mid]:
            return binarysearch(mylist, target, start, mid -1)
        else:
            return binarysearch(mylist, target, mid + 1, stop)


mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
target = 42
start = 0
stop = len(mylist)

x = binarysearch(mylist, target, start, stop)

if x == False:
    print("Item ", target, " Not Found!")
else:
    print("Item ", target, "Found at Index ", x)


#######################
if target in mylist:
    print("Item", target, " with index", mylist.index(target))