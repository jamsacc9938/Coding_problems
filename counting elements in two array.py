def bin_search(arr, n, x): 
    l = 0
    h = n - 1
    while(l <= h): 
        mid = int((l + h) / 2) 
        if arr[mid] <= x: 
            l = mid + 1;
        else: 
            h = mid - 1
    return h 
def countEleLessThanOrEqual(arr1,n1,arr2,n2):
    arr2.sort()
    res=[]
    for i in arr1:
        index=bin_search(arr2, n2, i)
        res.append(index+1)
    return res
