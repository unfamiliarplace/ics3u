# From 1987 to 2013
# https://dmoj.ca/problem/ccc13s1

def is_distinct(year: int) -> bool:
    """
    Return True iff the given year has distinct digits.

    >>> is_distinct(1987)
    True
    >>> is_distinct(1988)
    False
    """
    year = str(year)
    
    for digit in year:
        if year.count(digit) > 1:
            return False
            
    return True

year = int(input()) + 1

while not is_distinct(year):
    year += 1

print(year)
