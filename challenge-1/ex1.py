''' Create a function which takes a min and max number and sums all the integers inbetween (inclusive of min and max)
    If the min is larger than the max it should return incorrect range '''

def range_sum(min, max):
    """
    Takes  and returns the
    """

    total = 0
    for i in range(min, max):
        new_total = total + i

    if min > max:
        return 'Incorrect range'

    return new_total




