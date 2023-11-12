import numpy as np
from PIL import ImageColor


def hex_to_rgb(hex):
    '''
    Converts a hex color code to an RGB array.
    '''
    hex = hex.lstrip('#')
    hlen = len(hex)
    return np.array([int(hex[i:i+hlen//3], 16) for i in range(0, hlen, hlen//3)])

def rgb_to_hex(rgb):
    '''
    Converts an RGB array to a hex color code.
    '''
    return "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


def rgb_to_cmy(rgb):
    '''
    Converts an RGB array to a CMY array.
    The CMY array is normalized to 100.
    '''
    return(1 - rgb/255)

def cmy_to_rgb(cmy):
    '''
    Converts a CMY array to an RGB array.
    The CMY array is normalized to 100.
    Floor is used to get int rgb values.
    '''
    return np.floor((1 - cmy) * 255)
    

def rgb_to_cmyk(rgb):
    '''
    Converts an RGB array to a CMYK array.
    CMYK array is normalized between 0 and 1
    '''  
    k = 1 - np.max(rgb/255.)
    cmy = (1 - rgb/255. - k)/(1 - k)
    return np.append(cmy, k)

def cmyk_to_rgb(cmyk):
    '''
    Converts a CMYK array to an RGB array.
    CMYK array is normalized between 0 and 1
    '''
    return np.floor((1 - cmyk[:3]) * (1 - cmyk[3]) * 255)


def rgb_to_hsv(rgb):
    '''
    Converts an RGB array to an HSV array.
    '''
    r, g, b = rgb/255
    cmax = np.max(rgb/255)
    cmin = np.min(rgb/255)
    delta = cmax - cmin
    if delta == 0:
        h = 0
    elif cmax == r:
        h = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60 * (((b - r) / delta) + 2)
    elif cmax == b:
        h = 60 * (((r - g) / delta) + 4)
    if cmax == 0:
        s = 0
    else:
        s = delta / cmax
    v = cmax
    return np.array([h, s, v])

def hsv_to_rgb(hsv):
    '''
    Converts an HSV array to an RGB array.
    '''
    h, s, v = hsv
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    if h < 60:
        r, g, b = c, x, 0
    elif h < 120:
        r, g, b = x, c, 0
    elif h < 180:
        r, g, b = 0, c, x
    elif h < 240:
        r, g, b = 0, x, c
    elif h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    rgb_norm = np.array([r, g, b]) + m
    return np.floor(rgb_norm * 255)

if __name__ == "__main__":
    print("This file contains functions for converting between color spaces.")
    hex_p_blue = "#000f89"
    rgb_p_blue = np.array([0, 15, 137])
    cmyk_p_blue = np.array([1, 0.89, 0, 0.46])
    cmy_p_blue = np.array([1, 0.94, 0.46])
    hsv_p_blue = np.array([233.4, 1, 0.537])

    # Test hex_to_rgb
    print("hex_to_rgb:")
    print(hex_to_rgb(hex_p_blue))
    print(f"Real rgb: {rgb_p_blue}, hex_to_rgb: {hex_to_rgb(hex_p_blue)}")
    print()

    # Test rgb_to_hex
    print("rgb_to_hex:")
    print(rgb_to_hex(rgb_p_blue))
    print(f"Real hex: {hex_p_blue}, rgb_to_hex: {rgb_to_hex(rgb_p_blue)}")
    print()

    # Test rgb_to_cmy
    print("rgb_to_cmy:")
    print(rgb_to_cmy(rgb_p_blue))
    print(f"Real cmy: {cmy_p_blue}, rgb_to_cmy: {rgb_to_cmy(rgb_p_blue)}")
    print()

    # Test cmy_to_rgb
    print("cmy_to_rgb:")
    print(cmy_to_rgb(cmy_p_blue))
    print(f"Real rgb: {rgb_p_blue}, cmy_to_rgb: {cmy_to_rgb(cmy_p_blue)}")
    print()

    # Test rgb_to_cmyk
    print("rgb_to_cmyk:")
    print(rgb_to_cmyk(rgb_p_blue))
    print(f"Real cmyk: {cmyk_p_blue}, rgb_to_cmyk: {rgb_to_cmyk(rgb_p_blue)}")
    print()

    # Test cmyk_to_rgb
    print("cmyk_to_rgb:")
    print(cmyk_to_rgb(cmyk_p_blue))
    print(f"Real rgb: {rgb_p_blue}, cmyk_to_rgb: {cmyk_to_rgb(cmyk_p_blue)}")
    print()

    # Test rgb_to_hsv
    print("rgb_to_hsv:")
    print(rgb_to_hsv(rgb_p_blue))
    print(f"Real hsv: {hsv_p_blue}, rgb_to_hsv: {rgb_to_hsv(rgb_p_blue)}")
    print()

    # Test hsv_to_rgb
    print("hsv_to_rgb:")
    print(hsv_to_rgb(hsv_p_blue))
    print(f"Real rgb: {rgb_p_blue}, hsv_to_rgb: {hsv_to_rgb(hsv_p_blue)}")
    print()