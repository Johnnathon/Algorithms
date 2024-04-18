

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst[1:] if x <= pivot]
    right = [x for x in lst[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

lst = [4, 1,4 ,6 ,7, 4, 7, 3, 8, 8 ,9,1 ,3 ,2]
print(lst)
new_list = quick_sort(lst)
print(new_list)

news= enumerate(lst)
print(news)