def mode(numbers):
    counts={}
    for num in numbers:
        if num in counts:
            counts[num]+=1
        else :
            counts[num]=1
    mode_value=None
    max_count=0
    for num , count in counts.items():
        if count>max_count:
            mode_value=num
            max_count=count

    return mode_value
