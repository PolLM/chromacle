import numpy as np

def combine_color_array(color_array, weights):
    '''
    Combines an array of cmy or cmyk arrays into a single array.
    '''
    base_array = np.zeros(len(color_array[0]))
    for i in range(len(color_array)):
        base_array = base_array + color_array[i]*weights[i]
    base_array = base_array/sum(weights)
    return base_array