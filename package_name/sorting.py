def bubble_sort(items):
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]
    return items

    def merge_sort(items):
    if len(items) > 1:
        left, right = map(lambda l: list(reversed(merge_sort(l))), (items[::2], items[1::2]))
        items.clear()
        while left and right:
            items.append(left.pop() if left[-1] < right[-1] else right.pop())
        items.extend(left[::-1])
        items.extend(right[::-1])
    return items


    def quick_sort(items):
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quick_sort(items[:i])
        second_part = quick_sort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part
