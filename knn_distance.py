import random
def knn_distance(arr, q, k):
    dist_arr=[(abs(x-q),x) for x in arr]

    result = quickselect(dist_arr,k,0,len(dist_arr))
    return (result[0],result[1])

def quickselect(arr,k,start,stop):
    pivot_ix=random.randrange(start,stop)
    pivot_ix= partition(arr,start,stop,pivot_ix)
    pivot_order=pivot_ix+1
    if pivot_order==k:
        return arr[pivot_ix]
    elif pivot_order<k:
        return quickselect(arr,k,pivot_ix+1,stop)
    else:
        return quickselect(arr,k,start,pivot_ix)

def partition(arr,start,stop,pivot_ix):
    pivot=arr[pivot_ix]
    arr[pivot_ix],arr[stop-1]=arr[stop-1],arr[pivot_ix]
    store_ix = start
    for i in range(start, stop - 1):
        if arr[i] < pivot:
            arr[i], arr[store_ix] = arr[store_ix], arr[i]
            store_ix += 1
    arr[store_ix], arr[stop - 1] = arr[stop - 1], arr[store_ix]
    return store_ix
