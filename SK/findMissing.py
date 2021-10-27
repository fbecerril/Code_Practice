def findMissing(arr):
    for x, y in enumerate(arr):
        if x != y:
	    return x
    raise ValueError(msg= "No missing element")

