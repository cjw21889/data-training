''' Create a function which takes a min and max number and sums all the integers inbetween (inclusive of min and max)
    If the min is larger than the max it should return incorrect range '''


def range_sum(start, stop):
    """
    Takes start and stop params and returns their incusive sum
    """
    if start > stop:
        return 'incorrect range'

    return sum(range(start, stop+1))
