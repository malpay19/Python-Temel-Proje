def reverse(l):
    l.reverse()
    for element in l:
        if isinstance(element,list):
            reverse(element)
    return l

print(reverse([[1, 2], [3, 4], [5, 6, 7]]))
