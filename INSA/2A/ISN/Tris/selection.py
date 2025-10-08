def min_index(l, start):
    min_idx = start
    for i in range(start + 1, len(l)):
        if l[i] < l[min_idx]:
            min_idx = i
    return min_idx


def selection_sort(l):
    for i in range(len(l)):
        min_idx = min_index(l, i)
        if min_idx != i:
            l[i], l[min_idx] = l[min_idx], l[i]
    return l
