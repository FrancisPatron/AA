def merge_sort(a, inversions):
    n = len(a)
    if n == 1:
        return a

    left = a[:n//2]
    right = a[n//2:]
    left = merge_sort(left, inversions)
    right = merge_sort(right, inversions)
    return merge(left, right, inversions)

def merge(a, b, inversions):
    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
            inversions["inv"]+=len(a)       

    while len(a) > 0:
        c.append(a.pop(0))      

    while len(b) > 0:
        c.append(b.pop(0))
        
    return c

def sort_and_count(arr):
    inv = {"inv":0}
    return merge_sort(arr, inv), inv["inv"]