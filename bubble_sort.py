#testing bubble sort algorithm.

def bubble_sort(lst):
    n = len(lst)
    for x in range(n):
        for i in range(n-x-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i +1] = lst[i+1], lst[i]
    return lst

lst = [1, 4, 6 ,7 ,5 ,3 , 7, 4 ,3 ,6 ,2 ,7]

print(lst)
bubble_sort(lst)
print(lst)