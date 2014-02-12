#!/usr/bin/python
"""
Implement two types of sorting algorithms: Merge sort and bubble sort.
"""

def merge_sorted_lists(lst1, lst2):
    index1, index2 = 0, 0
    res = []

    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] < lst2[index2]:
            res.append(lst1[index1])
            index1 += 1
        else:
            res.append(lst2[index2])
            index2 += 1

    if index1 < len(lst1):
        res += lst1[index1:]
    else:
        res += lst2[index2:]

    return res

def merge_sort(lst):
    length = len(lst)
    if length == 1:
        return lst
    else:
        pivot = length // 2
        lst1 = lst[:pivot]
        lst2 = lst[pivot:]
        return merge_sorted_lists(merge_sort(lst1), merge_sort(lst2))
    

def bubble_sort(lst):
    last_i = len(lst) - 1
    cur_i = 0
    swapped = True

    while swapped:
        swapped = False

        while cur_i < last_i:
            if lst[cur_i] > lst[cur_i+1]:
                lst[cur_i], lst[cur_i+1] = lst[cur_i+1], lst[cur_i]
                swapped = True
            cur_i += 1

        last_i -= 1
        cur_i = 0

    return lst

def main():
    lst = [9,8,7,3,4,6,5,2,1,0]
    print(merge_sort(lst))
    print(bubble_sort(lst))

if __name__ == '__main__':
    main()
