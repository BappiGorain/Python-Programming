def merge(s, e, arr):
    mid = (s + e) // 2  
    main_index = s  
    len1 = mid - s + 1  
    len2 = e - mid  

    first = [0] * len1  
    second = [0] * len2  

    for i in range(len1):
        first[i] = arr[main_index]
        main_index += 1  

    main_index = mid + 1  
    for i in range(len2):
        second[i] = arr[main_index]
        main_index += 1  

    i, j, main_index = 0, 0, s  

    while i < len1 and j < len2:
        if first[i] < second[j]:
            arr[main_index] = first[i]
            i += 1
        else:
            arr[main_index] = second[j]
            j += 1
        main_index += 1  

    while i < len1:
        arr[main_index] = first[i]
        i += 1
        main_index += 1  

    while j < len2:
        arr[main_index] = second[j]
        j += 1
        main_index += 1  


def merge_sort(s, e, arr):
    if s >= e:
        return  
    mid = (s + e) // 2  

    merge_sort(s, mid, arr)  
    merge_sort(mid + 1, e, arr)  
    merge(s, e, arr)  

arr = [10, 3, 1, 5, 2, 9, 8]
n = len(arr)
merge_sort(0, n - 1, arr)
print(" ".join(map(str, arr)))
