def merge_list(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_list(lst[:mid])
    right = merge_list(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    x = i = 0
    while x < len(left) and i < len(right):
        if left[x] <= right[i]:
            result.append(left[x])
            x += 1
        else:
            result.append(right[i])
            i += 1
    result.extend(left[x:])
    result.extend(right[i:])
    return result

lst = [1, 5, 3, 7, 3, 8, 9, 4, 2 ,6 , 7, 3 ,5]
print(lst)
new_list = merge_list(lst)
print(new_list)


