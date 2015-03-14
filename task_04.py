#! usr/bin/env python
# *-* coding: utf-8 *-*
"""This is a looping module."""

TOTAL_SUM = ['1', '2', '3']


def process_data(data):
    """Looping list with for loop.

    Args:
        data(list): A list or tuple of numbers.

    Returns:
        tuple: A tuple containing the sums of the data and
        average with floating point precision.

    Example:
        >>>process_data([1,2,3])
        (6, 2.0)
        """  
    return data

t_sum = 0

for list_item in TOTAL_SUM:        
    t_sum += t_sum+1
    print list_item
