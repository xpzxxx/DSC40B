def histogram(points,bins):
    n=len(points)
    k=len(bins)

    counts=[0]*k
    j=0

    for point in points:
        while j<k-1 and point >=bins[j][1]:
            j+=1
        counts[j]+=1
    densities=[]
    for i in range(k):
        a,b = bins[i]
        width=b-a
        density=counts[i]/ (n*width)
        densities.append(density)
    return densities
