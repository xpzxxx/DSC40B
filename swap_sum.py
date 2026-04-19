def swap_sum(A,B):
    sumA=sum(A)
    sumB=sum(B)

    if (sumA-sumB+10)%2 !=0:
        return None
    target = (sumA-sumB+10)/2
    i=0
    j=0

    while i<len(A) and j<len(B):
        diff= A[i]-B[j]
        if diff == target:
            return(i,j)
        elif diff<target:
            i+=1
        else:
            j+=1

    return None

